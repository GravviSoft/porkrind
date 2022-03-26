# -*- coding: utf-8 -*-
import datetime
import time
from json import JSONDecodeError
import phonenumbers
import json
import re

import requests
import scrapy
from scrapy import Selector
from ..items import FbaboutItem2

# scrapy crawl ZYTE_GRAVVI_DB -a citylist1="Grayslake,-IL|Barrington,-IL|Cary,-IL|Lake-Villa,-IL|Mchenry,-IL|Park-Ridge,-IL|Elk-Grove-Village,-IL|Highland-Park,-IL|Buffalo-Grove,-IL|Highwood,-IL|Great-Lakes,-IL|Winnetka,-IL|Lincolnshire,-IL|Schaumburg,-IL|Waukegan,-IL|Wauconda,-IL|Round-Lake,-IL|Rolling-Meadows,-IL|Lake-Bluff,-IL|Draper,-UT|Mount-Prospect,-IL|Des-Plaines,-IL|Island-Lake,-IL|Arlington-Heights,-IL|Prospect-Heights,-IL|Glenview,-IL|Glencoe,-IL|Libertyville,-IL|Deerfield,-IL|Hoffman-Estates,-IL|Gurnee,-IL|Fox-River-Grove,-IL|Northbrook,-IL|Sandy,-UT|Ingleside,-IL|North-Chicago,-IL|Mundelein,-IL|Vernon-Hills,-IL|Wheeling,-IL|Palatine,-IL|" -a database="EricLandoll126" -a industrylist1="Appliance-Repair-Service|Architectural-Designer|Cabinets|Carpenter|Carpet-Cleaner|Chimney-Sweeper|Roofing|Cleaning-Service|Concrete-Contractor|Construction-Company|Contractor|Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Demolition-&-Excavation-Company|Doors|Electrician|Elevator-Service|Fence-&-Gate-Contractor|Fireplaces|Flooring|Furniture|Garage-Door-Service|Gardener|Roofing-Contractor|Gutter-Cleaning-Service|Handyman|Heating-Ventilating-&-Air-Conditioning-Service|Home-Audio-Visual|Home-Remodeling|Home-Security-Company|House-Painting|Interior-Design-Studio|Janitorial-Service|Landscaping|Lighting|Lumber-Yard|Masonry-Contractor|Moving-Service|Painters|Paving-&-Asphalt-Service|Pest-Control-Service|Roofing|Plumbing-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Swimming-Pool-&-Hot-Tub-Service|Tiling-Service|Tree-Cutting-Service|Vinyl-Siding-Company|Water-Treatment-Service|Well-Water-Drilling-Service|Window-Services" -a industrylist1_admin="Appliance-Repair-Service|Appliance-Sales|Appliance-Installation|Appliance-Repair|Cooktop,-Range-&-Stove-Installation|Oven-Installation|Range-Hood-Installation|Appliance-Removal|Oven-Repair|Cooktop,-Range-&-Stove-Repair|Dishwasher-Installation|Architectural-Designer|Cabinets|Custom-Kitchen-Cabinets|Custom-Cabinets|Custom-Bathroom-Vanities|Custom-Cabinet-Doors|Custom-Built-ins|Cabinet-Installation|Cabinet-Sales|Custom-Entertainment-Centers|Custom-Bookcases|Custom-Pantries|Carpenter|Handyman|Carpentry|Custom-Built-ins|Custom-Shelving|Custom-Bookcases|Custom-Cabinets|Finish-Carpentry|Custom-Furniture|Custom-Entertainment-Centers|Custom-Pantries|Custom-Fireplace-Mantels|Carpet-Cleaner|Chimney-Sweeper|Cleaning-Service|Commercial-Cleaning|House-Cleaning|Concrete-Contractor|Concrete-Sales|Patio-Construction|Hardscaping|Stone-Masonry|Retaining-Wall-Construction|Paver-Installation|Masonry|Concrete-Construction|Stone-Installation|Concrete-Driveway-Installation|Driveway-Sealing|Concrete-Driveway-Installation|Concrete-Construction|Hardscaping|Driveway-Repair|Driveway-Resurfacing|Asphalt-Paving|Land-Leveling-&-Grading|Paver-Installation|Masonry|Construction-Company|Contractor|General-Contracting|Home-Remodeling|Kitchen-Remodeling|Bathroom-Remodeling|Home-Additions|Home-Extensions|Custom-Homes|New-Home-Construction|Basement-Remodeling|Deck-Building|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Countertops|Custom-Countertops|Tile-Sales|Countertop-Sales|Countertop-Installation|Backsplash-Installation|Tile-Installation|Natural-Stone-Countertops|Quartz-Countertops|Granite-Countertops|Marble-Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Pergola-Construction|Deck-Building|Patio-Construction|Porch-Design-&-Construction|Gazebo-Design-&-Construction|Sunroom-Design-&-Construction|Deck-Design|Trellis-Construction|Patio-Design|Pool-Deck-Design-&-Construction|Demolition-&-Excavation-Company|Doors|Door-Dealer|Custom-Exterior-Doors|Door-Sales|Exterior-Door-Installation|Custom-Interior-Doors|Custom-Folding-Doors|Interior-Door-Installation|Sliding-Door-Installation|Bifold-Doors|Custom-Retractable-Screens|Door-Repair|Electrician|Electricians|Electrical-Installation|Electrical-Repair|Electrical-Inspection|Circuit-Breaker-Installation-&-Repair|Lighting-Design|Electrical-Outlet-&-Light-Switch-Installation|Exhaust-Fan-Installation|House-Wiring|Deck-Lighting-Installation|Home-Energy-Audit|Elevator-Service|Fence-&-Gate-Contractor|Fence-Contractors|Driveway-Gate-Installation|Fence-Installation|Gate-Installation|Fence-Repair|Chain-Link-Fence-Installation|Gate-Repair|Fence-Sales|Wrought-Iron-Fence-Installation|Aluminum-Fence-Installation|Wood-Fence-Installation|Fireplaces|Fireplace-Installation|Fireplace-Sales|Custom-Fireplaces|Gas-Fireplace-Installation|Custom-Fireplace-Mantels|Custom-Fire-Pits|Wood-Stove-Installation|Electric-Fireplace-Installation|Outdoor-Fireplace-Construction|Fireplace-Repair|Flooring|Carpet-Installation|Carpet-Sales|Custom-Rugs|Custom-Flooring|Carpet-Repair|Carpet-Stretching|Rug-Cleaning|Carpet-Cleaning|Flooring-Installation|Laminate-Flooring-Installation|Custom-Flooring|Wood-Floor-Installation|Vinyl-Flooring-Installation|Wood-Flooring-Sales|Flooring-Sales|Tile-Installation|Laminate-Flooring-Sales|Vinyl-Flooring-Sales|Stair-Installation|Railing-Installation|Baluster-Installation|Staircase-Design|Railing-Repair|Stair-Repair|Glass-Railings|Furniture|Antique-Restoration|Furniture-Refinishing|Upholstery-Repair|Custom-Upholstery|Custom-Furniture|Furniture-Repair|Wall-Upholstery|Custom-Drapery|Leather-Repair|Upholstery-Cleaning|Furniture-Repair-&-Upholstery-Service|Custom-Furniture|Pool-Table-Repair|Furniture-Repair|Furniture-Refinishing|Upholstery-Repair|Antique-Restoration|Custom-Tables|Sandblasting|Furniture-Sales|Custom-Furniture|Outdoor-Furniture-Sales|Furniture-Delivery|Custom-Rugs|Custom-Tables|Lighting-Sales|Custom-Pool-Tables|Antique-Furniture-Sales|Custom-Framing|Garage-Door-Service|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Sales|Custom-Garage-Doors|Gardener|Glass-Service|Shower-Door-Installation|Shower-Door-Sales|Mirror-Installation|Glass-Installation|Shower-Door-Repair|Stained-Glass-Repair-&-Design|Window-Installation|Glass-Cutting|Glass-Repair|Window-Repair|Gutter-Cleaning-Service|Handyman|Closet-Design|Custom-Walk-in-Closets|Closet-Organization|Space-Planning|Custom-Cabinets|Professional-Organizing|Garage-Storage|Decluttering|Custom-Storage|Sports-Equipment-Storage|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Heating-Ventilating-&-Air-Conditioning-Service|Air-Conditioning-&-Heating|Heating-&-Cooling-Sales-&-Repair|HVAC|Air-Conditioning-Installation|Heat-Pump-Installation|HVAC-Installation|Air-Conditioning-Repair|Furnace-Installation|Oil-to-Gas-Conversion|HVAC-Inspection|Heating-System-Installation|Ventilation-Installation-&-Repair|Thermostat-Repair|Home-Audio-Visual|Home-Automation|Home-Theater-Installation|Outdoor-Audio-Installation|Surround-Sound-Installation|Home-Theater-Design|Security-Camera-Installation|TV-Installation|Smart-Homes|Home-Security-Companies-&-Installation|Home-Audio-Systems|Home-Remodeling|Kitchen-&-Bath-Contractor|Custom-Homes|Home-Remodeling|New-Home-Construction|Home-Additions|Kitchen-Remodeling|Home-Extensions|Bathroom-Remodeling|Architectural-Design|Kitchen-Design|Bathroom-Design|Kitchen-Remodeling|Bathroom-Remodeling|Home-Remodeling|Home-Additions|Cabinet-Installation|Custom-Cabinets|Custom-Kitchen-Cabinets|Home-Extensions|Custom-Bathroom-Vanities|Custom-Countertops|Home-Improvement|Home-Security-Company|House-Painting|Custom-Artwork|Texture-Painting|Decorative-Painting|Mural-Painting|Wall-Stenciling|Faux-Painting|Stained-Glass-Repair-&-Design|Custom-Framing|Art-Installation|Custom-Furniture|Interior-Design-Studio|Home-Staging|Furniture-Selection|Space-Planning|Color-Consulting|Decluttering|Downsizing|Art-Selection|Furniture-Rental|Holiday-Decorating|Feng-Shui-Design|Interior-Design|Kitchen-Design|Bathroom-Design|Bedroom-Design|Living-Room-Design|Space-Planning|Color-Consulting|Furniture-Selection|Kids-Bedroom-Design|Dining-Room-Design|Janitorial-Service|Landscaping|Landscape-Company|Landscape-Architects-&-Landscape-Designers|Landscape-Contractors|Gardeners-&-Lawn-Care|Landscape-Construction|Hardscaping|Landscape-Maintenance|Garden-Design|Patio-Construction|Custom-Fire-Pits|Custom-Water-Features|Paver-Installation|Outdoor-Fireplace-Construction|Pool-Landscaping|Planting|Lawn-Care|Irrigation-System-Installation|Weed-Control|Tree-Pruning|Brush-Clearing|Drought-Tolerant-Landscaping|Lawn-Aeration|Yard-Waste-Removal|Drip-Irrigation-Installation|Lighting|Lighting-Sales|Lighting-Design|Outdoor-Lighting-Design|Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Deck-Lighting-Installation|Recessed-Lighting-Installation|Ceiling-Fan-Installation|Pool-Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Lighting-Installation|Deck-Lighting-Installation|Outdoor-Lighting-Design|Lighting-Design|Lighting-Sales|Home-Automation|Pool-Lighting-Installation|Outdoor-Audio-Installation|Lumber-Yard|Masonry-Contractor|Moving-Service|Piano-Moving|Local-Moving|Long-Distance-Moving|Painters|Painting|Door-Painting|Drywall-Repair|Interior-Painting|Drywall-Texturing|Baseboard-Installation|Interior-Door-Installation|Door-Repair|Ceiling-Painting|Paint-Removal|Backsplash-Installation|Paint-Sales|Wallcovering-Sales|Paving-&-Asphalt-Service|Pest-Control-Service|Plumbing-Service|Plumbers|Plumber|Faucet-Installation|Emergency-Plumbing|Faucet-Repair|Water-Heater-Repair|Plumbing-Repair|Drain-Cleaning|Garbage-Disposal-Repair|Garbage-Disposal-Installation|Water-Heater-Installation|Tankless-Water-Heater-Installation|Water-Heater-Installation-&-Repair-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Roof-Replacement|Gutter-Installation|Roof-Installation|Asphalt-Shingle-Roofing|Roof-Repair|Metal-Roofing|Roof-Inspection|Composition-Roofing|Gutter-Repair|Soffit-Installation|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Solar-Energy-Systems|Solar-Panel-Installation|Home-Energy-Audit|Solar-Panel-Repair|Solar-Panel-Cleaning|Passive-Solar-Heating-&-Cooling|Solar-Pool-Heating|Solar-Water-Heating|Solar-Tube-Installation|Skylight-Installation|Skylight-Repair|Swimming-Pool-&-Hot-Tub-Service|Swimming-Pool-Cleaner|Hot-Tub-Installation|Hot-Tub-Sales|Custom-Hot-Tubs|Sauna-Installation|Sauna-Sales|Sauna-Repair|Pool-Liner-Replacement|Pool-and-Spa-Repair|Pool-Cleaning-&-Maintenance|Sauna-Repair|Solar-Pool-Heating|Aboveground-Pools|Aboveground-Pool-Liner-Replacement|Pool-Covers|Natural-Swimming-Pools|Swimming-Pool-Design|Swimming-Pool-Construction|Pool-Deck-Design-&-Construction|Pool-Lighting-Installation|Pool-Remodeling|Custom-Hot-Tubs|Natural-Swimming-Pools|Hot-Tub-Installation|Pond-Construction|Sauna-Installation|Tiling-Service|Tree-Cutting-Service|Tree-Pruning|Tree-Removal|Stump-Removal|Tree-Planting|Wood-Chipping|Stump-Grinding|Hedge-Trimming|Mulching|Land-Clearing|Vinyl-Siding-Company|Water-Treatment-Service|Mold-Removal-&-Remediation|Water-Removal|Historic-Building-Conservation|Water-Testing|Indoor-Air-Quality-Testing|Basement-Waterproofing|Attic-Restoration|Fire-Damage-Restoration|Land-Surveying|Popcorn-Ceiling-Removal|Well-Water-Drilling-Service|Window-Services|Window-Replacement|Window-Installation|Custom-Windows|Window-Sales|Window-Repair|Egress-Windows|Bifold-Windows|Trim-Work|Skylight-Installation|Window-Screen-Installation|Window-Installation-Service|Home-Window-Service|Custom-Blinds-&-Shades|Motorized-Blinds|Blinds-&-Shades-Sales|Custom-Drapery|Blind-Installation|Plantation-Shutters|Interior-Shutters|Custom-Retractable-Screens|Exterior-Shades|Exterior-Shutters" -a klentyCadence="Cadence1" -a klentyapikey="60AD20DF50832D00294CD58D" -a klentymail="eric.landoll@n2pub.com" -a stateslist1="None" -a user_id="126" -a vmdapi="3528899"

listcount = []


class FBBOOK(scrapy.Spider):
    name = 'FBBOOK'
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'Docdash.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,
            # 'Docdash.pipelines.PhonyDuplicatesPipeline': 200,
            # 'Docdash.pipelines.BRIANSCHULLERCityFilterPipeline': 300,

        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_crawlera.CrawleraMiddleware': 610,
            # 'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
            ## User agent
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            # need pip install scrapy_fake_useragent  (in conda)
            # 'scrapy_fake_useragent.middlewares.RandomUserAgentMiddleware': 400,
            ## Proxy (privoxy + tor)
            # cf https://trevsewell.co.uk/scraping/anonymous-scraping-scrapy-tor-polipo/
            # activate http proxy (turn on proxy)
            # 'scrapy_fb.middlewares.UserAgentRotatorMiddlware': 110,
            # call the middleware to customize the http proxy  (set proxy to 'http://127.0.0.1:8118')
            # 'scrapy_fb.middlewares.ProxyMiddleware': 100,


        },
    #     "EXTENSIONS" : {
    #     # 'scrapy.extensionsa.enpxxtensions.TorRenewIdentity': 1,
    #     'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
    # },

    "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 429],
        # "CRAWLERA_URL": "gravvisoft.crawlera.com:8010",
        # "CRAWLERA_APIKEY": "c79ed6d3bb814597b4b26b17dfa299d5",
        # "CRAWLERA_ENABLED": True,
        # "CRAWLERA_DOWNLOAD_TIMEOUT": 200,
        # 'CONCURRENT_REQUESTS': 32,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 32,
        # "SCRAPEOPS_API_KEY" : 'b24fa8fe-eab1-4870-806a-e5ff27579a61',

    },
    #     #
    #     'CONCURRENT_REQUESTS': 1,
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    #     # 'TOR_RENEW_IDENTITY_ENABLED': True,
    #     # 'TOR_ITEMS_TO_SCRAPE_PER_IDENTITY': 5
    #     # "MYEXT_ENABLED": True,
    #     "ROTATING_PROXY_LIST_PATH": 'proxy-list.txt',
    #     "ROTATING_PROXY_PAGE_RETRY_TIMES": 5



    # def __init__(self, name=None, **kwargs):
    #     super().__init__(name=None, **kwargs)
    #     self.request = None

    def start_requests(self):

        global city, industry, cityyo, cityies, proxiyo2

        indlist = []

        industrylist1 = getattr(self, "industrylist1", "")
        industrylist1_admin = getattr(self, "industrylist1_admin", "")
        industrylistwhatwhat = f'{industrylist1}{industrylist1_admin}'
        # print(industrylistwhatwhat)
        ind = industrylistwhatwhat.split("|")
        for indus in ind:
            if "" != indus:
                indlist.append(indus)
        # print(cit)

        indjoin = "|".join(indlist)
        industry = indjoin.split("|")

        stateies = getattr(self, "stateslist1", "")
        cityyo = getattr(self, "citylist1", "")
        citylist = []

        if stateies:
            cityyo = f"{cityyo}{stateies}"

        cit = cityyo.split("|")
        for c in cit:
            if "" != c:
                citylist.append(c)

        cityjoin = "|".join(citylist)
        city = cityjoin.split("|")


        ziillowlist = []

        global link1
        self.start_urls = ["https://scrapethissite.com/pages/simple/"]
        for ind in industry:
            for key in city:
                for n in range(0, 5, 1):

                    link2 = f'zillow.com/professionals/real-estate-agent-reviews/salt-lake-city-ut/'
                    link3 = f'https://www.google.com/search?q={key}+{ind}+{n}+&start=0&num=100'
                    link4 = f'https://www.google.com/search?q={ind}+{key}+{n}+&start=0&num=100'

                    self.start_urls.append(link2)
                    self.start_urls.append(link3)
                    self.start_urls.append(link4)
                    self.start_urls.append("https://scrapethissite.com/pages/simple/")
        #
        # proxy = FreeProxy(elite=True, https=True, timeout=5).get()
        # print(proxy)
        # yield scrapy.Request(url="http://scrapethissite.com/pages/simple/", callback=self.parse)

        # # initialize some
        # # holding variables
        # oldIP = "0.0.0.0"
        # newIP = "0.0.0.0"
        #
        # # how many IP addresses
        # # through which to iterate?
        # nbrOfIpAddresses = 3
        #
        # # seconds between
        # # IP address checks
        # secondsBetweenChecks = 2
        # session = requests.session()
        #
        # # TO Request URL with SOCKS over TOR
        # session.proxies = {}
        # session.proxies['http'] = 'socks5h://localhost:9050'
        # session.proxies['https'] = 'socks5h://localhost:9050'
        # try:
        #     r = session.get('http://httpbin.org/ip')
        # except Exception as e:
        #     print(str(e))
        # else:
        #     proxiyo = r.text
        #     proxiyo2 = json.loads(proxiyo)
        #     print(proxiyo2)
        #     if proxiyo2:
        #         with Controller.from_port(port=9051) as controller:
        #             controller.authenticate(password="16:7A0120469C58F8B860F85FAB0FE00F3774E6FF1F7C313F7C1DFDC70667#D")
        #             print("Success!")
        #             controller.signal(Signal.NEWNYM)
        #             print("New Tor connection processed")
        #             for link in self.start_urls:
        #                 yield scrapy.Request(url=link, callback=self.parse, meta={'proxy': proxiyo2['origin']})
        #             controller.close()
        #         print(proxiyo2)
        #     else:
        #         print(proxiyo2['origin'])
        #         pass
        # time.sleep(5)
        for link in self.start_urls:
        #     yield scrapy.Request(url=link, callback=self.parse)
        #     # middleware will process the request
        #     yield scrapy.Request(url=url, callback=self.parse)

        # check if Tor has changed IP
            yield scrapy.Request(url=link, callback=self.parse)

    #
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     print('\n\nSpider: Start')
    #     print('Is proxy in response.meta?: ', response.meta)
    #     print ("user_agent is: ", response.request.headers['User-Agent'])
    #     print('\n\n Spider: End')
    #     # self.log('Saved file  ---  %s' % filename)
    #
    #
    # def is_tor_and_privoxy_used(self, response):
    #     print('\n\nSpider: Start')
    #     print("My IP is : " + str(response.body))
    #     print("Is proxy in response.meta?: ", response.meta)  # not header dispo
    #     print('\n\nSpider: End')
        # self.log('Saved file %s' % filename)


    def parse(self, response, **kwargs):
        # print("My IP is : " + str(response.body))
        # print ("user_agent is: ", response.request.headers['User-Agent'])
        #
        # print(response.headers.get('Set-Cookie'))
        # proxy = response.meta
        # print(proxy)
        gitit = response.xpath("//span[text()='View all']").extract()
        # print(gitit)

        if gitit:
            requesturl1 = f'{response.request.url}{gitit[0]}'

            yield scrapy.Request(
                url=requesturl1,
                callback=self.parse_result, )

        gitit2 = response.xpath("//span[text()='More businesses']/ancestor-or-self::a[1]/@href").extract()
        print(gitit2)
        if gitit2:
            requesturl2 = f'{response.request.url}{gitit2[0]}'
            print(requesturl2)
            if requesturl2:
                yield scrapy.Request(
                    url=requesturl2,
                    callback=self.parse_result)

    def parse_result(self, response):
        item = FbaboutItem2()

        time.sleep(5)

        def FindIndustry(string):
            iindustrylist = []
            industrylist1 = getattr(self, "industrylist1", "")
            industrylist1_admin = getattr(self, "industrylist1_admin", "")
            industrylistwhatwhat = f'{industrylist1}{industrylist1_admin}'
            ind = industrylistwhatwhat.split("|")
            for i in ind:
                if "" != i:
                    iindustrylist.append(i)

            indjoin = "|".join(iindustrylist)
            injoin = indjoin.replace("-", " ")

            indies3 = injoin.replace("|", r"\b|\b")

            regexind = fr'\b{indies3}\b'
            industryyoo = re.findall(regexind, string)
            return [x for x in industryyoo]

        def FindCity(string):
            citylist = []
            stateies = getattr(self, "stateslist1", "")
            cityies = getattr(self, "citylist1", "")

            if stateies:
                cityies = f"{cityies}{stateies}"

            cit = cityies.split("|")
            for c in cit:
                if "" != c:
                    citylist.append(c)

            citjoin = "|".join(citylist)
            cijoin = citjoin.replace("-", " ")
            # print(citjoin)

            cityies3 = cijoin.replace("|", r"\b|\b")

            regex_city = fr'\b{cityies3}\b'
            ciityyoo = re.findall(regex_city, string)
            return [x for x in ciityyoo]

        citytesty = response.xpath("//div[contains(@id,'tsu')]").extract()
        for ct in citytesty:
            # print(ct)
            ctsel = Selector(text=ct)
            ctsel_links = ctsel.xpath("//div[text()='Directions']/ancestor::a/@data-url").extract()
            print(ctsel_links)

            # COMPANY
            if ctsel_links:

                site = ctsel.xpath("//div[text()='Website']/ancestor::a/@href").extract()
                print(site)

                textit = ctsel.xpath("//div[@class='rllt__details']//text()").extract()
                print(textit)
                divheading = ctsel.xpath("//div[@class='rllt__details']/preceding::div[1]/text()[1]").extract()
                print(f'THIS IS THE DIVHEAD:   {divheading}')
                # place("+", " ")
                # print(selecter_citylinks3)
                # CITY
                selecter_citylinks2 = ctsel_links[0]
                selecter_citylinks3 = selecter_citylinks2
                foundcity2 = FindCity(f'{selecter_citylinks3}{" ".join(textit)}')
                print(f'FOUNDCIIIIIIIITTTTYYYY:     {foundcity2}')
                if foundcity2:
                    item['city'] = foundcity2[0]
                    found_industry1 = FindIndustry(" ".join(textit).title())
                    print(found_industry1)
                    if found_industry1:
                        item['industry'] = found_industry1[0]
                        item['city'] = foundcity2[0]

                        # COMPANY
                        if ctsel_links:
                            lineline2 = ctsel_links[0]
                            lineline4 = lineline2.split(",")[0]
                            line5yo = lineline4.replace("/maps/dir//", "")
                            line6 = line5yo.replace("+", " ")
                            print(line6)
                            item['company'] = line6

                        for match in phonenumbers.PhoneNumberMatcher(" ".join(textit), "US"):
                            phoneage = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
                            phone_found = phoneage
                            if phoneage:
                                item['phone'] = phoneage
                                print(phone_found)
                            else:
                                pass

                            if site:
                                item['url'] = site[0]  # data_id = data['id']
                                yield scrapy.Request(url=item['url'], callback=self.email_parse_result, meta={
                                    'city': item["city"],
                                    'company': item["company"],
                                    'industry': item["industry"],
                                    'phone': item['phone'],
                                    'url': item['url'],
                                    # "data_id": data_id,
                                })

                            else:
                                item["url"] = None
                                item['email'] = None
                                # item["valid_email"] = None
                                # item['free_email'] = None
                                # item["email_drop"] = None
                                yield item
                                print(f'FOUND BOTH THE INDUSTRY AND CITY: {item["city"]} {item["industry"]}')
                                urlccciittyy = 'https://www.gravvisoft.com/api/lead/'

                                itemcity = {
                                    "user_id": getattr(self, 'user_id', ''),
                                    "date": str(datetime.date.today()),
                                    'city': item["city"],
                                    'company': item["company"],
                                    'industry': item["industry"],
                                    'phone': item['phone'],
                                    # "email": item['email'],

                                    # 'valid_email': item['valid_email'],
                                    # "free_email": item['free_email'],
                                    # "email_drop": item["email_drop"],
                                }
                                x = requests.post(urlccciittyy, data=itemcity)
                                x_yo = x.content
                                id_numxyoo = r
                                if "DT_RowId" in x_yo.ccntent:
                                    print(x_yo)

                                yield item

            nextlink = response.xpath("//span[text()='Next']").extract()
            if nextlink:
                nextlink_url = response.xpath("//span[text()='Next']/ancestor-or-self::a[1]/@href").extract()
                nextlink_url_full = f'{response.request.url}{nextlink_url[0]}'
                print(nextlink_url_full)
                yield scrapy.Request(
                    url=nextlink_url_full,
                    callback=self.parse_result,
                )

    def email_parse_result(self, response):
        global datadebounce
        item = FbaboutItem2()
        city = response.meta['city']
        industry = response.meta['industry']
        phone = response.meta['phone']
        company = response.meta['company']
        url = response.meta['url']

        # data_id = response.meta['data_id']
        # print(f'THIS IS THE META DATA: {data_id}')
        bodytext = response.xpath('//body//text()').extract()
        bodyjoin = " ".join(bodytext)
        # print(bodyjoin)
        emailfind = re.findall(
            "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
            bodyjoin)
        print(emailfind)
        if emailfind:
            item['email'] = emailfind[0]

            ademail = getattr(self, 'klentymail', '')
            adklentyapikey = getattr(self, 'klentyapikey', '')
            adcadenceName = getattr(self, 'klentyCadence', '')
            ### EMAIL API
            try:
                addprospect = requests.post(
                    f"https://api.debounce.io/v1/?api=5f43170b7690e&email={item['email']}")
                datadebounce = json.loads(addprospect.content)
            except JSONDecodeError:
                pass
            if not datadebounce:
                item['free_email'] = None
                item['valid_email'] = None
                item['email_drop'] = None

            if datadebounce:
                print(datadebounce['debounce']['send_transactional'])
                processemail = datadebounce['debounce']['send_transactional']

                item['free_email'] = datadebounce['debounce']['send_transactional']
                item['valid_email'] = datadebounce['debounce']['reason']

                if processemail != "1":
                    item['email_drop'] = None

                elif processemail == "1":
                    item["email_drop"] = "Valid"

                    addprospect = requests.post(
                        f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
                        json={"Email": f"{item['email']}",
                              "Company": f"{company}",
                              "City": f"{city}",
                              "Department": f"{industry}",
                              "Phone": f"{phone}",
                              },
                        headers={'x-api-key': adklentyapikey})
                    try:
                        data = json.loads(addprospect.content)
                        print(data)
                    except JSONDecodeError:
                        pass
                    addtocadence = requests.post(
                        f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
                        json={"Email": f"{item['email']}",
                              "cadenceName": adcadenceName},
                        headers={'x-api-key': adklentyapikey})
                    try:
                        data2 = json.loads(addtocadence.content)
                        print(data2)
                    except JSONDecodeError:
                        pass

            # yield item
            print(f'FOUND BOTH THE INDUSTRY AND CITY: {city} {industry}')
            urlccciittyy = 'https://www.gravvisoft.com/api/lead/'

            itemcity2 = {
                "user_id": getattr(self, 'user_id', ''),
                "date": str(datetime.date.today()),
                'city': city,
                'company': company,
                'industry': industry,
                'url': url,
                'email': item['email'],
                'phone': phone,
                'valid_email': item['valid_email'],
                "free_email": item['free_email'],
                "email_drop": item["email_drop"],
            }
            print(itemcity2)
            x2 = requests.post(urlccciittyy, data=itemcity2)
            print(x2.content)
            yield item
