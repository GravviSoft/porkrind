# -*- coding: utf-8 -*-
import ssl
from json import JSONDecodeError

import psycopg2

import itertools
import pymongo
import requests
from bson import ObjectId

import scrapy
# scrapy crawl LEADSRAIN_RVM -a user_id=131
# scrapy crawl LEADSRAIN_RVM -a user_id=129
# scrapy crawl LEADSRAIN_RVM -a user_id=128
# scrapy crawl LEADSRAIN_RVM -a user_id=127
# scrapy crawl LEADSRAIN_RVM -a user_id=29
# scrapy crawl LEADSRAIN_RVM -a user_id=76
# scrapy crawl LEADSRAIN_RVM -a user_id=131
# scrapy crawl LEADSRAIN_RVM -a user_id=52
# scrapy crawl LEADSRAIN_RVM -a user_id=67

from pymongo.errors import DuplicateKeyError

from ..items import FbaboutItem2

# scrapy crawl FBBOOK -a citylist1="Grayslake,-IL|Barrington,-IL|Cary,-IL|Lake-Villa,-IL|Mchenry,-IL|Park-Ridge,-IL|Elk-Grove-Village,-IL|Highland-Park,-IL|Buffalo-Grove,-IL|Highwood,-IL|Great-Lakes,-IL|Winnetka,-IL|Lincolnshire,-IL|Schaumburg,-IL|Waukegan,-IL|Wauconda,-IL|Round-Lake,-IL|Rolling-Meadows,-IL|Lake-Bluff,-IL|Draper,-UT|Mount-Prospect,-IL|Des-Plaines,-IL|Island-Lake,-IL|Arlington-Heights,-IL|Prospect-Heights,-IL|Glenview,-IL|Glencoe,-IL|Libertyville,-IL|Deerfield,-IL|Hoffman-Estates,-IL|Gurnee,-IL|Fox-River-Grove,-IL|Northbrook,-IL|Sandy,-UT|Ingleside,-IL|North-Chicago,-IL|Mundelein,-IL|Vernon-Hills,-IL|Wheeling,-IL|Palatine,-IL|" -a database="EricLandoll126" -a industrylist1="Appliance-Repair-Service|Architectural-Designer|Cabinets|Carpenter|Carpet-Cleaner|Chimney-Sweeper|Roofing|Cleaning-Service|Concrete-Contractor|Construction-Company|Contractor|Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Demolition-&-Excavation-Company|Doors|Electrician|Elevator-Service|Fence-&-Gate-Contractor|Fireplaces|Flooring|Furniture|Garage-Door-Service|Gardener|Roofing-Contractor|Gutter-Cleaning-Service|Handyman|Heating-Ventilating-&-Air-Conditioning-Service|Home-Audio-Visual|Home-Remodeling|Home-Security-Company|House-Painting|Interior-Design-Studio|Janitorial-Service|Landscaping|Lighting|Lumber-Yard|Masonry-Contractor|Moving-Service|Painters|Paving-&-Asphalt-Service|Pest-Control-Service|Roofing|Plumbing-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Swimming-Pool-&-Hot-Tub-Service|Tiling-Service|Tree-Cutting-Service|Vinyl-Siding-Company|Water-Treatment-Service|Well-Water-Drilling-Service|Window-Services" -a industrylist1_admin="Appliance-Repair-Service|Appliance-Sales|Appliance-Installation|Appliance-Repair|Cooktop,-Range-&-Stove-Installation|Oven-Installation|Range-Hood-Installation|Appliance-Removal|Oven-Repair|Cooktop,-Range-&-Stove-Repair|Dishwasher-Installation|Architectural-Designer|Cabinets|Custom-Kitchen-Cabinets|Custom-Cabinets|Custom-Bathroom-Vanities|Custom-Cabinet-Doors|Custom-Built-ins|Cabinet-Installation|Cabinet-Sales|Custom-Entertainment-Centers|Custom-Bookcases|Custom-Pantries|Carpenter|Handyman|Carpentry|Custom-Built-ins|Custom-Shelving|Custom-Bookcases|Custom-Cabinets|Finish-Carpentry|Custom-Furniture|Custom-Entertainment-Centers|Custom-Pantries|Custom-Fireplace-Mantels|Carpet-Cleaner|Chimney-Sweeper|Cleaning-Service|Commercial-Cleaning|House-Cleaning|Concrete-Contractor|Concrete-Sales|Patio-Construction|Hardscaping|Stone-Masonry|Retaining-Wall-Construction|Paver-Installation|Masonry|Concrete-Construction|Stone-Installation|Concrete-Driveway-Installation|Driveway-Sealing|Concrete-Driveway-Installation|Concrete-Construction|Hardscaping|Driveway-Repair|Driveway-Resurfacing|Asphalt-Paving|Land-Leveling-&-Grading|Paver-Installation|Masonry|Construction-Company|Contractor|General-Contracting|Home-Remodeling|Kitchen-Remodeling|Bathroom-Remodeling|Home-Additions|Home-Extensions|Custom-Homes|New-Home-Construction|Basement-Remodeling|Deck-Building|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Countertops|Custom-Countertops|Tile-Sales|Countertop-Sales|Countertop-Installation|Backsplash-Installation|Tile-Installation|Natural-Stone-Countertops|Quartz-Countertops|Granite-Countertops|Marble-Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Pergola-Construction|Deck-Building|Patio-Construction|Porch-Design-&-Construction|Gazebo-Design-&-Construction|Sunroom-Design-&-Construction|Deck-Design|Trellis-Construction|Patio-Design|Pool-Deck-Design-&-Construction|Demolition-&-Excavation-Company|Doors|Door-Dealer|Custom-Exterior-Doors|Door-Sales|Exterior-Door-Installation|Custom-Interior-Doors|Custom-Folding-Doors|Interior-Door-Installation|Sliding-Door-Installation|Bifold-Doors|Custom-Retractable-Screens|Door-Repair|Electrician|Electricians|Electrical-Installation|Electrical-Repair|Electrical-Inspection|Circuit-Breaker-Installation-&-Repair|Lighting-Design|Electrical-Outlet-&-Light-Switch-Installation|Exhaust-Fan-Installation|House-Wiring|Deck-Lighting-Installation|Home-Energy-Audit|Elevator-Service|Fence-&-Gate-Contractor|Fence-Contractors|Driveway-Gate-Installation|Fence-Installation|Gate-Installation|Fence-Repair|Chain-Link-Fence-Installation|Gate-Repair|Fence-Sales|Wrought-Iron-Fence-Installation|Aluminum-Fence-Installation|Wood-Fence-Installation|Fireplaces|Fireplace-Installation|Fireplace-Sales|Custom-Fireplaces|Gas-Fireplace-Installation|Custom-Fireplace-Mantels|Custom-Fire-Pits|Wood-Stove-Installation|Electric-Fireplace-Installation|Outdoor-Fireplace-Construction|Fireplace-Repair|Flooring|Carpet-Installation|Carpet-Sales|Custom-Rugs|Custom-Flooring|Carpet-Repair|Carpet-Stretching|Rug-Cleaning|Carpet-Cleaning|Flooring-Installation|Laminate-Flooring-Installation|Custom-Flooring|Wood-Floor-Installation|Vinyl-Flooring-Installation|Wood-Flooring-Sales|Flooring-Sales|Tile-Installation|Laminate-Flooring-Sales|Vinyl-Flooring-Sales|Stair-Installation|Railing-Installation|Baluster-Installation|Staircase-Design|Railing-Repair|Stair-Repair|Glass-Railings|Furniture|Antique-Restoration|Furniture-Refinishing|Upholstery-Repair|Custom-Upholstery|Custom-Furniture|Furniture-Repair|Wall-Upholstery|Custom-Drapery|Leather-Repair|Upholstery-Cleaning|Furniture-Repair-&-Upholstery-Service|Custom-Furniture|Pool-Table-Repair|Furniture-Repair|Furniture-Refinishing|Upholstery-Repair|Antique-Restoration|Custom-Tables|Sandblasting|Furniture-Sales|Custom-Furniture|Outdoor-Furniture-Sales|Furniture-Delivery|Custom-Rugs|Custom-Tables|Lighting-Sales|Custom-Pool-Tables|Antique-Furniture-Sales|Custom-Framing|Garage-Door-Service|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Sales|Custom-Garage-Doors|Gardener|Glass-Service|Shower-Door-Installation|Shower-Door-Sales|Mirror-Installation|Glass-Installation|Shower-Door-Repair|Stained-Glass-Repair-&-Design|Window-Installation|Glass-Cutting|Glass-Repair|Window-Repair|Gutter-Cleaning-Service|Handyman|Closet-Design|Custom-Walk-in-Closets|Closet-Organization|Space-Planning|Custom-Cabinets|Professional-Organizing|Garage-Storage|Decluttering|Custom-Storage|Sports-Equipment-Storage|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Heating-Ventilating-&-Air-Conditioning-Service|Air-Conditioning-&-Heating|Heating-&-Cooling-Sales-&-Repair|HVAC|Air-Conditioning-Installation|Heat-Pump-Installation|HVAC-Installation|Air-Conditioning-Repair|Furnace-Installation|Oil-to-Gas-Conversion|HVAC-Inspection|Heating-System-Installation|Ventilation-Installation-&-Repair|Thermostat-Repair|Home-Audio-Visual|Home-Automation|Home-Theater-Installation|Outdoor-Audio-Installation|Surround-Sound-Installation|Home-Theater-Design|Security-Camera-Installation|TV-Installation|Smart-Homes|Home-Security-Companies-&-Installation|Home-Audio-Systems|Home-Remodeling|Kitchen-&-Bath-Contractor|Custom-Homes|Home-Remodeling|New-Home-Construction|Home-Additions|Kitchen-Remodeling|Home-Extensions|Bathroom-Remodeling|Architectural-Design|Kitchen-Design|Bathroom-Design|Kitchen-Remodeling|Bathroom-Remodeling|Home-Remodeling|Home-Additions|Cabinet-Installation|Custom-Cabinets|Custom-Kitchen-Cabinets|Home-Extensions|Custom-Bathroom-Vanities|Custom-Countertops|Home-Improvement|Home-Security-Company|House-Painting|Custom-Artwork|Texture-Painting|Decorative-Painting|Mural-Painting|Wall-Stenciling|Faux-Painting|Stained-Glass-Repair-&-Design|Custom-Framing|Art-Installation|Custom-Furniture|Interior-Design-Studio|Home-Staging|Furniture-Selection|Space-Planning|Color-Consulting|Decluttering|Downsizing|Art-Selection|Furniture-Rental|Holiday-Decorating|Feng-Shui-Design|Interior-Design|Kitchen-Design|Bathroom-Design|Bedroom-Design|Living-Room-Design|Space-Planning|Color-Consulting|Furniture-Selection|Kids-Bedroom-Design|Dining-Room-Design|Janitorial-Service|Landscaping|Landscape-Company|Landscape-Architects-&-Landscape-Designers|Landscape-Contractors|Gardeners-&-Lawn-Care|Landscape-Construction|Hardscaping|Landscape-Maintenance|Garden-Design|Patio-Construction|Custom-Fire-Pits|Custom-Water-Features|Paver-Installation|Outdoor-Fireplace-Construction|Pool-Landscaping|Planting|Lawn-Care|Irrigation-System-Installation|Weed-Control|Tree-Pruning|Brush-Clearing|Drought-Tolerant-Landscaping|Lawn-Aeration|Yard-Waste-Removal|Drip-Irrigation-Installation|Lighting|Lighting-Sales|Lighting-Design|Outdoor-Lighting-Design|Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Deck-Lighting-Installation|Recessed-Lighting-Installation|Ceiling-Fan-Installation|Pool-Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Lighting-Installation|Deck-Lighting-Installation|Outdoor-Lighting-Design|Lighting-Design|Lighting-Sales|Home-Automation|Pool-Lighting-Installation|Outdoor-Audio-Installation|Lumber-Yard|Masonry-Contractor|Moving-Service|Piano-Moving|Local-Moving|Long-Distance-Moving|Painters|Painting|Door-Painting|Drywall-Repair|Interior-Painting|Drywall-Texturing|Baseboard-Installation|Interior-Door-Installation|Door-Repair|Ceiling-Painting|Paint-Removal|Backsplash-Installation|Paint-Sales|Wallcovering-Sales|Paving-&-Asphalt-Service|Pest-Control-Service|Plumbing-Service|Plumbers|Plumber|Faucet-Installation|Emergency-Plumbing|Faucet-Repair|Water-Heater-Repair|Plumbing-Repair|Drain-Cleaning|Garbage-Disposal-Repair|Garbage-Disposal-Installation|Water-Heater-Installation|Tankless-Water-Heater-Installation|Water-Heater-Installation-&-Repair-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Roof-Replacement|Gutter-Installation|Roof-Installation|Asphalt-Shingle-Roofing|Roof-Repair|Metal-Roofing|Roof-Inspection|Composition-Roofing|Gutter-Repair|Soffit-Installation|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Solar-Energy-Systems|Solar-Panel-Installation|Home-Energy-Audit|Solar-Panel-Repair|Solar-Panel-Cleaning|Passive-Solar-Heating-&-Cooling|Solar-Pool-Heating|Solar-Water-Heating|Solar-Tube-Installation|Skylight-Installation|Skylight-Repair|Swimming-Pool-&-Hot-Tub-Service|Swimming-Pool-Cleaner|Hot-Tub-Installation|Hot-Tub-Sales|Custom-Hot-Tubs|Sauna-Installation|Sauna-Sales|Sauna-Repair|Pool-Liner-Replacement|Pool-and-Spa-Repair|Pool-Cleaning-&-Maintenance|Sauna-Repair|Solar-Pool-Heating|Aboveground-Pools|Aboveground-Pool-Liner-Replacement|Pool-Covers|Natural-Swimming-Pools|Swimming-Pool-Design|Swimming-Pool-Construction|Pool-Deck-Design-&-Construction|Pool-Lighting-Installation|Pool-Remodeling|Custom-Hot-Tubs|Natural-Swimming-Pools|Hot-Tub-Installation|Pond-Construction|Sauna-Installation|Tiling-Service|Tree-Cutting-Service|Tree-Pruning|Tree-Removal|Stump-Removal|Tree-Planting|Wood-Chipping|Stump-Grinding|Hedge-Trimming|Mulching|Land-Clearing|Vinyl-Siding-Company|Water-Treatment-Service|Mold-Removal-&-Remediation|Water-Removal|Historic-Building-Conservation|Water-Testing|Indoor-Air-Quality-Testing|Basement-Waterproofing|Attic-Restoration|Fire-Damage-Restoration|Land-Surveying|Popcorn-Ceiling-Removal|Well-Water-Drilling-Service|Window-Services|Window-Replacement|Window-Installation|Custom-Windows|Window-Sales|Window-Repair|Egress-Windows|Bifold-Windows|Trim-Work|Skylight-Installation|Window-Screen-Installation|Window-Installation-Service|Home-Window-Service|Custom-Blinds-&-Shades|Motorized-Blinds|Blinds-&-Shades-Sales|Custom-Drapery|Blind-Installation|Plantation-Shutters|Interior-Shutters|Custom-Retractable-Screens|Exterior-Shades|Exterior-Shutters" -a klentyCadence="Cadence1" -a klentyapikey="60AD20DF50832D00294CD58D" -a klentymail="eric.landoll@n2pub.com" -a stateslist1="None" -a user_id="126" -a vmdapi="3528899"


class LeadsrainRvmSpider(scrapy.Spider):
    name = 'LEADSRAIN_RVM'
    start_urls = ['https://scrapethissite.com/pages/simple/']

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'Docdash.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,
            # 'Docdash.pipelines.PhonyDuplicatesPipeline': 200,
            # 'Docdash.pipelines.BRIANSCHULLERCityFilterPipeline': 300,

        },
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'scrapy_crawlera.CrawleraMiddleware': 610,
        #
        # },
        #
        # 'CRAWLERA_ENABLED': True,
        # 'CRAWLERA_APIKEY': 'c79ed6d3bb814597b4b26b17dfa299d5',
        # 'CRAWLERA_URL': 'http://gravvisoft.crawlera.com',

        # 'DONT_FILTER': True,

    }

    def parse(self, response, **kwargs):
        global emailwhatwhat, datadebounce

        # url = f'https://www.gravvisoft.com/api/lead/user/126'
        # x2 = requests.get(url)
        # print(x2)
        # data2 = x2.json()
        # pagination = data2["next"]
        #
        # print(data2)


        connyo = pymongo.MongoClient("mongodb+srv://benslow:Grannyboy1@cluster0.kuvzf.mongodb.net",
                                     ssl_cert_reqs=ssl.CERT_NONE)
        dbyo = connyo[f"GRAVVIBOY"]

        email1 = []

        citylist = []

        industrylist = []

        collectionyo = dbyo["users_profile"]
        # cursor = collectionyo.update_many({'active_client': {'$exists': False}}, {'$set': {"active_client": False}})

        id_start = getattr(self, "id_start", "")
        id_end = getattr(self, "id_end", "")
        user_id = getattr(self, "user_id", "")



        # for dbases in collectionyo.find({"user_id": int(user_id)}):

        for dbases in itertools.islice(collectionyo.find(), int(id_start), int(id_end)):
            if dbases["active_client"] == True:
                ademail = dbases["klentyemail"]
                print(ademail)
                adklentyapikey = dbases["klenty_api_key"]
                adcadenceName = dbases["cadence_name"]
                ringlessvm_id = dbases["ringlessvm_id"]
                if ringlessvm_id is None:
                    pass
                else:

                    conn = psycopg2.connect(host="node67749-gravvisoft-clone2.w1-us.cloudjiffy.net", port=5432,
                                            database="postgres3", user="webadmin", password="VRDylt04210")

                    # Create a cursor object
                    cur = conn.cursor()

                    # A sample query of all data from the "vendors" table in the "suppliers" database
                    cur.execute(f"""SELECT * FROM api_lead WHERE user_id = '{dbases['user_id']}' AND date > timestamp '2021-10-12 00:00:00'; """)
                    query_results = cur.fetchall()
                    for leads in query_results:
                        # print(leads)
                        lead_id = leads[0]
                        user_id = leads[1]
                        date = leads[2]
                        company = leads[3]
                        city = leads[4]
                        industry = leads[5]
                        phone = leads[6]
                        email = leads[7]
                        url = leads[8]
                        lead_source = leads[9]
                        notes = leads[10]
                        rvm_drop = leads[11]
                        email_drop = leads[12]
                        dnc_email = leads[13]
                        dnc_phone = leads[14]
                        tags = leads[15]
                        phone_carrier = leads[16]
                        free_email = leads[17]
                        valid_email = leads[18]
                        facebook = leads[19]
                        instagram = leads[20]
                        linkedin = leads[21]
                        twitter = leads[22]
                        whatsapp = leads[23]
                        otherlinks = leads[24]
                        houzz = leads[25]
                        yelp = leads[26]
                        bbb = leads[27]
                        yp = leads[28]
                        zillow = leads[29]
                        realtor = leads[30]
                        google = leads[31]
                        first_name = leads[32]
                        cadence_name = leads[33]
                        opens = leads[34]
                        clicks = leads[35]
                        replies = leads[36]
                        unsubscribes = leads[37]
                        rvm_sent = leads[38]
                        rvm_lead_id = leads[39]
                        rvm_message = leads[40]
                        # print(user_id, email, email_drop, valid_email)
                        # EMAAIL FILTER
                        # if email is not None:
                        #     if "@" in email:
                        #         if "Valid" not in email_drop:
                        #             print(leads)
                        #             try:
                        #                 addprospect = requests.post(
                        #                     f"https://api.debounce.io/v1/?api=5f43170b7690e&email={email}")
                        #                 datadebounce = json.loads(addprospect.content)
                        #             except JSONDecodeError:
                        #                 pass
                        #
                        #             if datadebounce:
                        #                 print(datadebounce['debounce']['send_transactional'])
                        #                 processemail = datadebounce['debounce']['send_transactional']
                        #
                        #                 # item['free_email'] = datadebounce['debounce']['free_email']
                        #                 # item['valid_email'] = datadebounce['debounce']['reason']
                        #                 try:
                        #                     emailurl1 = f'https://www.gravvisoft.com/api/lead/phone/{phone}/'
                        #                     emaildata1 = {
                        #                         "free_email": datadebounce['debounce']['send_transactional'],
                        #                         "valid_email": datadebounce['debounce']['reason'],
                        #                     }
                        #                     email_y = requests.patch(emailurl1, data=emaildata1)
                        #                     print(email_y)
                        #
                        #                     # data2 = json.loads(y)
                        #                     print(email_y.json())
                        #                 except JSONDecodeError:
                        #                     pass
                        #
                        #                 if processemail != "1":
                        #                     pass
                        #
                        #                 elif processemail == "1":
                        #
                        #                     try:
                        #                         emailurl2 = f'https://www.gravvisoft.com/api/lead/phone/{phone}/'
                        #                         emaildata2 = {
                        #                             "email_drop": "Valid",
                        #                         }
                        #                         email_y2 = requests.patch(emailurl2, data=emaildata2)
                        #                         print(email_y2)
                        #
                        #                         # data2 = json.loads(y)
                        #                         print(email_y2.json())
                        #                     except JSONDecodeError:
                        #                         pass
                        #
                        #                     addprospect = requests.post(
                        #                         f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
                        #                         json={"Email": f"{email}",
                        #                               "Company": f"{company}",
                        #                               "City": f"{city}",
                        #                               "Phone": f"{phone}",
                        #                               },
                        #                         headers={'x-api-key': adklentyapikey})
                        #                     try:
                        #                         data = json.loads(addprospect.content)
                        #                         print(data)
                        #                     except JSONDecodeError:
                        #                         pass
                        #                     addtocadence = requests.post(
                        #                         f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
                        #                         json={"Email": f"{email}",
                        #                               "cadenceName": adcadenceName},
                        #                         headers={'x-api-key': adklentyapikey})
                        #                     try:
                        #                         data2 = json.loads(addtocadence.content)
                        #                         print(data2)
                        #                     except JSONDecodeError:
                        #                         pass

                        #PHONE FILTER
                        if dnc_phone is False:
                            if rvm_sent is False:
                                if "not a Mobile Number." not in rvm_message:
                                    print(leads)
                                    api_key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
                                    check_duplicate = "CHECK_DUPLICATE_IN_LIST"
                                    Integration_Key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
                                    Encoded_Integration_Key = "f66e83d5f117f20a778a7c3647609e65"
                                    #     phone_number = "8018150852"
                                    #
                                    #     # IF NO DUPLICATE PHONE IN MONGO + THE CITY IS IN THE LIST OF CITIES THEN PROCESS THE PHONE NUMBER.  SEND THE PHONE NUMBER INTO THE CLIENTS VOICEMAIL DROP API
                                    #     vmdapi = "692074"

                                    url_lr = "https://s2.leadsrain.com/ringless/api/add_posted_lead.php"
                                    myobj = {
                                        'api_key': api_key,
                                        'username': "23100",
                                        'list_id': int(dbases["ringlessvm_id"]),
                                        'check_duplicate': check_duplicate,
                                        'phone_number': phone,

                                    }
                                    try:
                                        x = requests.post(url_lr, data=myobj)
                                        data = x.json()
                                        print(data)
                                        print(data["lead_id"])
                                        print(data["message"])
                                        rvm_message1 = data["message"]

                                        if "Duplicate Phone Number" in rvm_message1:


                                            url1 = f'https://www.gravvisoft.com/api/lead/update/{lead_id}/'
                                            data1 = {
                                                "rvm_sent": True,
                                            }
                                            y = requests.patch(url1, data=data1)
                                            print(y)
                                            # data2 = json.loads(y)
                                            print(y.json())

                                        elif "Lead Successfully added" in rvm_message1:
                                            url2 = f'https://www.gravvisoft.com/api/lead/update/{lead_id}/'
                                            data2 = {
                                                "rvm_sent": True,
                                                "rvm_message": data["message"]
                                            }
                                            y2 = requests.patch(url2, data=data2)
                                            print(y2)
                                            # data2 = json.loads(y)
                                            print(y2.json())

                                        else:
                                            url3 = f'https://www.gravvisoft.com/api/lead/update/{lead_id}/'
                                            data3 = {
                                                "rvm_sent": False,
                                                "rvm_message": data["message"]
                                            }
                                            y3 = requests.patch(url3, data=data3)
                                            print(y3)
                                            # data2 = json.loads(y)
                                            print(y3.json())
                                    except JSONDecodeError:
                                        pass

                    cur.close()
                    conn.close()
        connyo.close()


















        # url = f'https://www.gravvisoft.com/api/lead/user/{dbases["user_id"]}'
        # x2 = requests.get(url)
        # print(x2)
        # data2 = x2.json()
        # print(data2)
        # phone filter
        # if "False" not in dnc_phone:
        #     if rvm_sent is False:
        #         if "not a Mobile Number." not in rvm_message:
        #             print(leads)
        #             pass
        #




        # email filter
        # if "@" in leads['email']:
        #     if "Valid" not in leads['email_drop']:
        #         if "" in leads['valid_email']:
        #             try:
        #                 addprospect = requests.post(
        #                     f"https://api.debounce.io/v1/?api=5f43170b7690e&email={leads['email']}")
        #                 datadebounce = json.loads(addprospect.content)
        #             except JSONDecodeError:
        #                 pass
        #
        #             if datadebounce:
        #                 print(datadebounce['debounce']['send_transactional'])
        #                 processemail = datadebounce['debounce']['send_transactional']
        #
        #                 # item['free_email'] = datadebounce['debounce']['free_email']
        #                 # item['valid_email'] = datadebounce['debounce']['reason']
        #                 try:
        #                     emailurl1 = f'https://www.gravvisoft.com/api/lead/phone/{leads["phone"]}/'
        #                     emaildata1 = {
        #                         "free_email": datadebounce['debounce']['send_transactional'],
        #                         "valid_email": datadebounce['debounce']['reason'],
        #                     }
        #                     email_y = requests.patch(emailurl1, data=emaildata1)
        #                     print(email_y)
        #
        #                     # data2 = json.loads(y)
        #                     print(email_y.json())
        #                 except JSONDecodeError:
        #                     pass
        #
        #
        #                 if processemail != "1":
        #                     pass
        #
        #                 elif processemail == "1":
        #
        #                     try:
        #                         emailurl2 = f'https://www.gravvisoft.com/api/lead/phone/{leads["phone"]}/'
        #                         emaildata2 = {
        #                             "email_drop": "Valid",
        #                         }
        #                         email_y2 = requests.patch(emailurl2, data=emaildata2)
        #                         print(email_y2)
        #
        #                         # data2 = json.loads(y)
        #                         print(email_y2.json())
        #                     except JSONDecodeError:
        #                         pass
        #
        #
        #                     addprospect = requests.post(
        #                         f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
        #                         json={"Email": f"{leads['email']}",
        #                               "Company": f"{leads['company']}",
        #                               "City": f"{leads['city']}",
        #                               "Phone": f"{leads['phone']}",
        #                               },
        #                         headers={'x-api-key': adklentyapikey})
        #                     try:
        #                         data = json.loads(addprospect.content)
        #                         print(data)
        #                     except JSONDecodeError:
        #                         pass
        #                     addtocadence = requests.post(
        #                         f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
        #                         json={"Email": f"{leads['email']}",
        #                               "cadenceName": adcadenceName},
        #                         headers={'x-api-key': adklenpikey})
        #                     try:
        #                         data2 = json.loads(addtocadence.content)
        #                         print(data2)
        #                     except JSONDecodeError:
        #                         pass


        #     rvm_message = d["rvm_message"]
        #     rvm_sent = d["rvm_sent"]
        #     if rvm_sent is False and rvm_message is "":
        #         print(rvm_sent, rvm_message)
        #         #     # SEND LEADS TO LEADS RAIN
        #         api_key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
        #         check_duplicate = "CHECK_DUPLICATE_IN_LIST"
        #         Integration_Key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
        #         Encoded_Integration_Key = "f66e83d5f117f20a778a7c3647609e65"
        #         #     phone_number = "8018150852"
        #         #
        #         #     # IF NO DUPLICATE PHONE IN MONGO + THE CITY IS IN THE LIST OF CITIES THEN PROCESS THE PHONE NUMBER.  SEND THE PHONE NUMBER INTO THE CLIENTS VOICEMAIL DROP API
        #         #     vmdapi = "692074"
        #
        #         url = "https://s2.leadsrain.com/ringless/api/add_posted_lead.php"
        #         myobj = {
        #             'api_key': api_key,
        #             'username': "23100",
        #             'list_id': int(dbases["ringlessvm_id"]),
        #             'check_duplicate': check_duplicate,
        #             'phone_number': d["phone"],
        #
        #         }
        #         try:
        #             x = requests.post(url, data=myobj)
        #             data = x.json()
        #             print(data)
        #             print(data["lead_id"])
        #             print(data["message"])
        #             rvm_message1 = data["message"]
        #
        #
        #             if "Duplicate Phone Number" in rvm_message1:
        #
        #
        #                 url = f'https://www.gravvisoft.com/api/lead/phone/{d["phone"]}/'
        #                 data = {
        #                     "rvm_sent": True,
        #                 }
        #                 y = requests.patch(url, data=data)
        #                 print(y)
        #                 # data2 = json.loads(y)
        #                 print(y.json())
        #
        #
        #             elif "Lead Successfully added" in rvm_message1:
        #                 url = f'https://www.gravvisoft.com/api/lead/phone/{d["phone"]}/'
        #                 data = {
        #                     "rvm_sent": True,
        #                 }
        #                 y = requests.patch(url, data=data)
        #                 print(y)
        #                 # data2 = json.loads(y)
        #                 print(y.json())
        #         except JSONDecodeError:
        #             pass


        # PAGINATION

        # if data2['next']:
        #     return scrapy.Request(url=data2['next'], callback=self.pagination, meta={"ademail": ademail, "adklentyapikey": adklentyapikey, "adcadenceName": adcadenceName})












        #         databasename = dbases["databasename"]
        #         print(databasename)
        #         ringlessvm_id = dbases['ringlessvm_id']
        #         print(ringlessvm_id)
        #         klentyemail = dbases['klentyemail']
        #         industrylist1 = dbases['industrylist1']
        #         industrylist1_admin = dbases['industrylist1_admin']
        #         if industrylist1 == None:
        #             print(databasename)
        #         # leadstoskip = int(dbases["vmd_leads_loaded"]) - int(dbases["vmd_leads_remaining"])
        #         # print(leadstoskip)
        #         conn1 = pymongo.MongoClient("mongodb+srv://benslow:Grannyboy1@cluster0.kuvzf.mongodb.net",
        #                                     ssl_cert_reqs=ssl.CERT_NONE)
        #         db1 = conn1[f'{dbases["databasename"]}']
        #         # db = conn[f"GRAVVISOFT"]
        #         ph_list = []
        #         collection = db1['LEADS']
        #         # cursor = collection.update_many({'rvm_lead_id': {'$exists': False}}, {'$set': {"rvm_lead_id": ""}}).limit(10000)
        #         # cursor = collection.update_many({'rvm_message': {'$exists': False}}, {'$set': {"rvm_message": ""}}).limit(10000)
        #         # cursor = collection.update_many({'rvm_sent': {'$exists': False}}, {'$set': {"rvm_sent": False}}).limit(10000)
        #         # cursor = collection.update_many({'dnc_phone': {'$exists': False}}, {'$set': {"dnc_phone": "False"}}).limit(10000)
        #         # cursor = collection.update_many({'dnc_email': {'$exists': False}}, {'$set': {"dnc_email": "False"}}).limit(10000)
        #
        #         # CHECK FOR UNSENT RVM LEADS
        #         # DELETE_DUPLICATE_PHONE_NUM
        #         phone_list = []
        #         duplicate_ids = []
        #
        #         for dupphone in collection.find().limit(100000):
        #             try:
        #                 for match in phonenumbers.PhoneNumberMatcher(dupphone["phone"], "US"):
        #                     phoneage = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
        #                     if phoneage not in phone_list:
        #                         phone_list.append(phoneage)
        #                     else:
        #                         duplicate_ids.append(dupphone["_id"])
        #             except KeyError:
        #                 pass
        #         print(phone_list)
        #         print(duplicate_ids)
        #
        #         collection.delete_many({"_id": {"$in": duplicate_ids}})
        #         collection.update_many({'rvm_sent': {'$exists': False}}, {'$set': {"rvm_sent": False}})
        #         collection.update_many({'dnc_phone': {'$exists': False}}, {'$set': {"dnc_phone": "False"}})
        #         # collection.update_many({'lead_id': {'$exists': False}}, {'$set': {"lead_id": ""}})
        #         # collection.update_many({'lead_message': {'$exists': False}}, {'$set': {"lead_message": ""}})
        #         collection.update_many({'rvm_lead_id': {'$exists': False}}, {'$set': {"rvm_lead_id": ""}})
        #         collection.update_many({'rvm_message': {'$exists': False}}, {'$set': {"rvm_message": ""}})
        #
        #         for c in collection.find({'$and': [{"rvm_sent": False}, {"dnc_phone": "False"}, {"rvm_message": ""}]}):
        # for c in collection.find( {"dnc_phone": "False"}):
    #
    # def pagination(self, response, **kwargs):
    #     global datadebounce
    #     print(response.request.url)
    #     ademail = response.meta["ademail"]
    #     adklentyapikey = response.meta["adklentyapikey"]
    #     adcadenceName = response.meta["adcadenceName"]
    #
    #     x2 = requests.get(response.request.url)
    #     print(x2)
    #     data2 = x2.json()
    #     print(data2)
    #     #phone filter
    #     full_list = []
    #     #PAGINATION
    #     if data2['next']:
    #         full_list.append(response.request.url)
    #         return scrapy.Request(url=data2['next'], callback=self.pagination, meta={"ademail": ademail, "adklentyapikey": adklentyapikey, "adcadenceName": adcadenceName})
    #
    #     if not data2["next"]:
    #         print(full_list)

    # for leads in data2["results"]:
    #     # phone filter
    #     if "False" not in leads['dnc_phone']:
    #         if leads["rvm_sent"] is False:
    #             if "not a Mobile Number." not in leads["rvm_message"]:
    #                 # print(leads)
    #                 pass
    #
    #
    #
    #     # email filter
    #     if "@" in leads['email']:
    #         if "Valid" not in leads['email_drop']:
    #             if "" in leads['valid_email']:
    #                 try:
    #                     addprospect = requests.post(
    #                         f"https://api.debounce.io/v1/?api=5f43170b7690e&email={leads['email']}")
    #                     datadebounce = json.loads(addprospect.content)
    #                 except JSONDecodeError:
    #                     pass
    #
    #                 if datadebounce:
    #                     print(datadebounce['debounce']['send_transactional'])
    #                     processemail = datadebounce['debounce']['send_transactional']
    #
    #                     # item['free_email'] = datadebounce['debounce']['free_email']
    #                     # item['valid_email'] = datadebounce['debounce']['reason']
    #                     try:
    #                         emailurl1 = f'https://www.gravvisoft.com/api/lead/phone/{leads["phone"]}/'
    #                         emaildata1 = {
    #                             "free_email": datadebounce['debounce']['free_email'],
    #                             "valid_email": datadebounce['debounce']['reason'],
    #                         }
    #                         email_y = requests.patch(emailurl1, data=emaildata1)
    #                         print(email_y)
    #
    #                         # data2 = json.loads(y)
    #                         print(email_y.json())
    #                     except JSONDecodeError:
    #                         pass
    #
    #                     if processemail != "1":
    #                         pass
    #
    #                     elif processemail == "1":
    #
    #                         try:
    #                             emailurl2 = f'https://www.gravvisoft.com/api/lead/phone/{leads["phone"]}/'
    #                             emaildata2 = {
    #                                 "email_drop": "Valid",
    #                             }
    #                             email_y2 = requests.patch(emailurl2, data=emaildata2)
    #                             print(email_y2)
    #
    #                             # data2 = json.loads(y)
    #                             print(email_y2.json())
    #                         except JSONDecodeError:
    #                             pass
    #
    #                         addprospect = requests.post(
    #                             f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
    #                             json={"Email": f"{leads['email']}",
    #                                   "Company": f"{leads['company']}",
    #                                   "City": f"{leads['city']}",
    #                                   "Phone": f"{leads['phone']}",
    #                                   },
    #                             headers={'x-api-key': adklentyapikey})
    #                         try:
    #                             data = json.loads(addprospect.content)
    #                             print(data)
    #                         except JSONDecodeError:
    #                             pass
    #                         addtocadence = requests.post(
    #                             f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
    #                             json={"Email": f"{leads['email']}",
    #                                   "cadenceName": adcadenceName},
    #                             headers={'x-api-key': adklentyapikey})
    #                         try:
    #                             data2 = json.loads(addtocadence.content)
    #                             print(data2)
    #                         except JSONDecodeError:
    #                             pass













    #
    #     print(c)
    #     print(c["_id"])
    #     print(c["phone"])
    #     print(c["rvm_lead_id"])
    #     print(c["rvm_message"])
    #
    #     # SEND LEADS TO LEADS RAIN
    #     api_key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
    #     check_duplicate = "CHECK_DUPLICATE_IN_LIST"
    #     Integration_Key = "e2e6bf6c93bc7431aa243fade9af49b20665656c"
    #     Encoded_Integration_Key = "f66e83d5f117f20a778a7c3647609e65"
    # #     phone_number = "8018150852"
    # #
    # #     # IF NO DUPLICATE PHONE IN MONGO + THE CITY IS IN THE LIST OF CITIES THEN PROCESS THE PHONE NUMBER.  SEND THE PHONE NUMBER INTO THE CLIENTS VOICEMAIL DROP API
    # #     vmdapi = "692074"
    #
    #     url = "https://s2.leadsrain.com/ringless/api/add_posted_lead.php"
    #     myobj = {
    #         'api_key': api_key,
    #         'username': "23100",
    #         'list_id': int(ringlessvm_id),
    #         'check_duplicate': check_duplicate,
    #         'phone_number': c["phone"],
    #
    #     }
    #     try:
    #         x = requests.post(url, data=myobj)
    #         data = x.json()
    #         print(data)
    #         print(data["lead_id"])
    #         print(data["message"])
    #         print(databasename)
    #
    #                     url = 'https://www.gravvisoft.com/api/lead/'
    #                     payload = {
    #                         'rvm_sent': True,
    #                         'rvm_lead_id': data["lead_id"],
    #                         'rvm_message': data["message"]
    #                     }
    #
    #                     import requests
    #
    #                     url_gravvisoft = f'http://www.gravvisoft.com/api/lead/?search={c["phone"]}'
    #
    #                     x_url_gravvisoft = requests.get(url_gravvisoft)
    #                     data1 = x_url_gravvisoft.json()
    #                     print(data1["results"][0]["id"])
    #
    #                     the_id = data1["results"][0]["id"]
    #
    #
    #
    #                     if "Lead Successfully added" in data["message"]:
    #                         # FIND ONE ITEM AND UPDATE ITEM
    #                         collection.find_one_and_update(
    #                             {"_id": ObjectId(c["_id"])},
    #                             {'$set': {'rvm_sent': True,
    #                                       'rvm_lead_id': data["lead_id"],
    #                                       'rvm_message': data["message"]}})
    #                         #
    #                         # url2 = f'http://www.gravvisoft.com/api/lead/update/{the_id}/'
    #                         #
    #                         # payload = {'rvm_sent': True,
    #                         #            'rvm_lead_id': data["lead_id"],
    #                         #            'rvm_message': data["message"]}
    #                         # y = requests.put(url=url2, data=payload)
    #                         # print(y)
    #
    #                     elif "Duplicate" in data["message"]:
    #                         # FIND ONE ITEM AND UPDATE ITEM
    #                         collection.find_one_and_update(
    #                             {"_id": ObjectId(c["_id"])},
    #                             {'$set': {'rvm_sent': True, }})
    #                         #
    #                         # url2 = f'http://www.gravvisoft.com/api/lead/update/{the_id}/'
    #                         #
    #                         # payload = {'rvm_sent': True}
    #                         # y = requests.put(url=url2, data=payload)
    #                         # print(y)
    #                     else:
    #                         collection.find_one_and_update(
    #                             {"_id": ObjectId(c["_id"])},
    #                             {'$set': {'rvm_sent': False,
    #                                       'rvm_lead_id': data["lead_id"],
    #                                       'rvm_message': data["message"]}})
    #
    #                         url2 = f'http://www.gravvisoft.com/api/lead/update/{the_id}/'
    #
    #                         payload = {'rvm_sent': False,
    #                                    'rvm_lead_id': data["lead_id"],
    #                                    'rvm_message': data["message"]}
    #                         y = requests.put(url=url2, data=payload)
    #                         print(y)
    #                 except JSONDecodeError:
    #                     pass

    # collection.update_many({'email': {'$exists': False}}, {'$set': {"emaiil": ""}})

    # for emaiill in collection.find({"email_drop":  {"$ne": "Valid" }}):
    #     if "@" in emaiill["email"]:
    #     #     if emaiill["email"] != "":
    #         ademail = dbases['klentyemail']
    #         adklentyapikey = dbases["klenty_api_key"]
    #         adcadenceName = dbases["cadence_name"]
    #         ### EMAIL API
    #         try:
    #             addprospect = requests.post(
    #                 f"https://api.debounce.io/v1/?api=5f43170b7690e&email={emaiill['email']}")
    #             datadebounce = json.loads(addprospect.content)
    #         except JSONDecodeError:
    #             pass
    #         if datadebounce:
    #             try:
    #                 print(datadebounce)
    #                 print(datadebounce['debounce']['send_transactional'])
    #                 processemail = datadebounce['debounce']['send_transactional']
    #                 collection.find_one_and_update(
    #                     {"_id": ObjectId(f'{emaiill["_id"]}')},
    #                     {'$set': {
    #                         'free_email': datadebounce['debounce']['free_email'],
    #                         'valid_email': datadebounce['debounce']['result']}})
    #
    #                 if processemail == "1":
    #                     collection.find_one_and_update(
    #                         {"_id": ObjectId(f'{emaiill["_id"]}')},
    #                         {'$set': {'email_drop': "Valid"}})
    #
    #                     addprospect = requests.post(
    #                         f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
    #                         json={"Email": f"{emaiill['email']}",
    #                               "Company": f"{emaiill['company']}",
    #                               "City": f"{emaiill['city']}",
    #                               "Department": f"{emaiill['industry']}",
    #
    #                               "Phone": f"{emaiill['phone']}",
    #                               },
    #                         headers={'x-api-key': adklentyapikey})
    #                     try:
    #                         data = json.loads(addprospect.content)
    #                         print(data)
    #                     except JSONDecodeError:
    #                         pass
    #                     addtocadence = requests.post(
    #                         f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
    #                         json={"Email": f"{emaiill['email']}",
    #                               "cadenceName": adcadenceName},
    #                         headers={'x-api-key': adklentyapikey})
    #                     try:
    #                         data2 = json.loads(addtocadence.content)
    #                         print(data2)
    #                     except JSONDecodeError:
    #                         pass
    #
    #             except JSONDecodeError:
    #                 pass

    # conn1.close()
    # connyo.close()
