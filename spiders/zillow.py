 # # -*- coding: utf-8 -*-
 import ..scrapy.item as Zyte
 import phonenumbers
import pymongo
import requests
import scrapy



class WebscraperrSpider(scrapy.Spider):

    name = 'zillowleads'
    start_urls = ['https://www.yelp.com/search?find_desc=plumbiing&find_loc=Orem%2C+UT&ns=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'deploytoscloud.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,
            # 'deploytoscloud.pipelines.PhonyDuplicatesPipeline': 200,
            # 'deploytoscloud.pipelines.BRIANSCHULLERCityFilterPipeline': 300,

        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_crawlera.CrawleraMiddleware': 610,
            # 'scrapy_selenium.SeleniumMiddleware': 800
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 700,

        },
        # 'SPIDER_MIDDLEWARES': {
        #     'scrapy_deltafetch.DeltaFetch': 100,
        # },

        # 'DELTAFETCH_ENABLED': True,

        'CRAWLERA_ENABLED': True,
        'CRAWLERA_APIKEY': 'c79ed6d3bb814597b4b26b17dfa299d5',
        'CRAWLERA_URL': 'http://gravvisoft.crawlera.com',
        # "CONCURRENT_REQUESTS_PER_IP": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
        "CONCURRENT_REQUESTS": 32,
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 5,
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 429],

    }

#         print(response.text)
    def parse(self, response, **kwargs):
        global emailwhatwhat, datadebounce, phoneage, phoneage2, leads2, leads

        user_id = getattr(self, "user_id", "")
        comany= response.xpath('//h3/*//a/text()').extract()
        print(comany)

        comany_url= response.xpath('//h3/*//a/@href').extract()
        
        # alllurls = f'https://www.yelp.com{comany_url}')
        for l in comany_url:
            alllurls = f'https://www.yelp.com{l}'
            yield scrapy.Request(url=alllurls, callback=self.parsebiz, meta={"comany": comany, })
        
        
        
    def parsebiz(self, response):
        item=Zyte
        company = response.meta['company']
        print("companyz")
 
 
 #     nextlink_url_full = f'https://www.utahrealestate.com{name[0]}'
    #
    #     print(nextlink_url_full)
    #
    #     yield scrapy.Request(url=nextlink_url_full, callback=self.new_parse)
    #
    #
    # def new_parse(self, response):
    #
    #     hhk= response.xpath('//a[contains(text(), "Go to my Site")]/@href').extract()
    #
    #     name= response.css("h3::text").extract()
    #     print(name)
    #
    #
    #     for liikne in hhk:
    #         print(liikne)
    #



        # conn2 = pymongo.MongoClient("mongodb+srv://benslow:Grannyboy1@cluster0.kuvzf.mongodb.net", tls=True)
        #
        # dbyo = conn2["GRAVVIBOY"]
        # collectionyo = dbyo["users_profile"]
# id_start = getattr(self, "id_start", "")
        # id_end = getattr(self, "id_end", "")
        # user_id = getattr(self, "user_id", "")
        #
        # for dbases in itertools.islice(collectionyo.find(), int(id_start), int(id_end)):
        #     if dbases["active_client"] == True:
        #         print(dbases['citylist1'])
        #         s2city =dbases['citylist1'].replace(',-', " ")
        #         s3city = dbases['citylist1'].replace('- ', " ")

            #
            # else:
            #     pass
                # cust_cities = []
                # # S
                #

                # #         s2city = cityyo.replace(',-', " ")
                # #         s3city = s2city.replace('- ', " ")
                # cit = citylistwhatwhat.split("|")
                # for c in cit:
                #     if "" != c:
                #         citiesss = cust_cities.append(c.strip())
                #         print(citiesss)

            # for dbases in collectionyo.find({"user_id": int(user_id)}, batch_size=20):
            # for dbases in itertools.islice(collectionyo.find(batch_size=20), int(id_start), int(id_end)):
            #
            # zitems["databasename"] = dbases["databasename"]
            # zitems["klentyemail"] = dbases["klentyemail"]
            # zitems["klenty_api_key"] = dbases["klenty_api_key"]
            # zitems["cadence_name"] = dbases["cadence_name"]
            # zitems["databasename"] = dbases["databasename"]
            # zitems["ringlessvm_id"] = dbases["ringlessvm_id"]
            # zitems["databasename"] = dbases["databasename"]

            # industrylist1 = dbases['industrylist1']
            # industrylist1_admin = dbases['industrylist1_admin']
            #
            # zitems["industrylist1"] = industrylist1 + industrylist1_admin

            # if industrylist1 == None:
            #     print("databasename")
            # cust_industries = []
            # cust_cities = []
            # # S
            #
            # citylistwhatwhat = dbases['citylist1'].replace(",-", " ")
            #
            # #         s2city = cityyo.replace(',-', " ")
            # #         s3city = s2city.replace('- ', " ")
            # cit = citylistwhatwhat.split("|")
            # for c in cit:
            #     if "" != c:
            #         citiesss = cust_cities.append(c.strip().lower())
            #         print(citiesss)
            # print(cust_industries, cust_cities)
