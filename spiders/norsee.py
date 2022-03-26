# # -*- coding: utf-8 -*-
# import datetime
# import itertools
# import json
# import re
# import ssl
# from json import JSONDecodeError
#
# import phonenumbers
# import pymongo
# import requests
# import scrapy
#
#
# class WebscraperrSpider(scrapy.Spider):
#
#     name = 'zillowleads'
#     start_urls = ['https://www.utahrealestate.com/roster/report/rpt/public/type/agent']
#
#     custom_settings = {
#         'ITEM_PIPELINES': {
#             # 'deploytoscloud.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,
#             # 'deploytoscloud.pipelines.PhonyDuplicatesPipeline': 200,
#             # 'deploytoscloud.pipelines.BRIANSCHULLERCityFilterPipeline': 300,
#
#         },
#         'DOWNLOADER_MIDDLEWARES': {
#             'scrapy_crawlera.CrawleraMiddleware': 610,
#             # 'scrapy_selenium.SeleniumMiddleware': 800
#             'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 700,
#
#         },
#         # 'SPIDER_MIDDLEWARES': {
#         #     'scrapy_deltafetch.DeltaFetch': 100,
#         # },
#
#         # 'DELTAFETCH_ENABLED': True,
#
#         'CRAWLERA_ENABLED': True,
#         'CRAWLERA_APIKEY': 'c79ed6d3bb814597b4b26b17dfa299d5',
#         'CRAWLERA_URL': 'http://gravvisoft.crawlera.com',
#         # "CONCURRENT_REQUESTS_PER_IP": 1,
#         "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
#         "CONCURRENT_REQUESTS": 32,
#         "RETRY_ENABLED": True,
#         "RETRY_TIMES": 5,
#         "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 429],
#
#     }
#
#     def parse(self, response, **kwargs):
#         AAAA=response.path("//a[contains(text(), Next)]").extract()
#         print(AAAA)
#         # dbyo = connyo[
#         #     "GRAVVIBOY"]
#         #
#         # email1 = []
#         #
#         # citylist = []
#         #
#         # industrylist = []
#         #
#         # collectionyo = dbyo["users_profile"]
#         # # cursor = collectionyo.update_many({'active_client': {'$exists': False}}, {'$set': {"active_client": False}})
#         #
#         # id_start = getattr(self, "id_start", "")
#         # id_end = getattr(self, "id_end", "")
#         # user_id = getattr(self, "user_id", "")
#         #
#         # # for dbases in itertools.islice(collectionyo.find(), int(id_start), int(id_end)):
#         # for dbases in collectionyo.find({"user_id": int(user_id)}):
#         #     if dbases["active_client"] == True:
#         #     #
#         #     #     databasename = dbases["databasename"]
#         #     #     print(databasename)
#
#                 # reg_city_statelist = []
#
#                 # stateslist = dbases["stateslist1"]
#                 # if stateslist1:
#                 #     stateslist1 = stateslist.replace("-", " ")
#                 #     statelist5 = stateslist1.split("|")
#                 #
#                 #     for s in statelist5:
#                 #         if s is not "":
#                 #             reg_city_statelist.append(f'{s}$')
#
#                 # industrylist1 = dbases["industrylist1_admin"]
#                 # industrylist2 = industrylist1.replace("+", " ")
#                 # industrylist4 = industrylist2.split("|")
#                 # if "" not in industrylist:
#                 #     print(industrylist4)
#                 # industrylist4 = industrylist4.replace("'", '"')
#
#                 # print(f'{industry: {'$in:  },city: {$in:  }})
#
#                 # industrylist3 = industrylist2.replace('and', '&')
#                 # industrylist4 = industrylist3.split("|")
#                 # industrylistwhat = list(industrylist4)
#                 # industrylistwhatwhat = filter(None, industrylistwhat)
#                 # citylist1 = dbases["citylist1"]
#                 # citylist2 = citylist1.replace(",", "-")
#                 # citylist5 = citylist2.split("|")
#                 #
#                 # melissa = "West-Chester,-OH|New-Lebanon,-OH|Lebanon,-OH|Goshen,-OH|Miamisburg,-OH|Kings-Mills,-OH|Cincinnati,-OH|Camp-Dennison,-OH|Morrow,-OH|Germantown,-OH|Fairfield,-OH|Middletown,-OH|Terrace-Park,-OH|Milford,-OH|Loveland,-OH|Maineville,-OH|Springboro,-OH|Bellevue,-KY|Mason,-OH|South-Lebanon,-OH|Anderson,-OH|Amelia,-OH|Hyde-Park,-OH|Mt.-Lookout,-OH|Kenwood,-OH|Mt.-Washington,-OH|California,-OH|New-Richmond,-OH|Batavia,-OH|Mt.-Carmel,-OH|Newtown,-OH|Mariemont,-OH|Fairfax,-OH|Symmes-Township,-OH|Montgomery,-OH|Blue-Ash,-OH|Deer-Park,-OH"
#                 # citylist1 = dbases["citylist1"]
#                 # citylist2 = citylist1.replace(",-", "--")
#                 # # citylist3 = citylist1.replace("-", "+")
#                 # citylist5 = citylist2.split("|")
#                 # url_liist = []
#
#                 # for i in industrylist4:
#                 #     if "'s" not in i:
#                 #         for c in citylist5:
#                 #             if c is not "":
#                 #                 urls = [f"https://www.google.com/search?q={i}+{c}"]
#                 #
#                 #                 for ur in urls:
#                 # #                     print(ur)
#                 # citiiew = ['cottonwood-heights',
#                 #            'draper',
#                 #            'midvale',
#                 #            'millcreeak',
#                 #            'murray',
#                 #            'riverton',
#                 #            'salt-lake-city‎',
#                 #            'sandy',
#                 #            'south-jordan',
#                 #            'south-salt-lake',
#                 #            'taylorsville',
#                 #            'west-jordan',
#                 #            'west-valley-city',
#                 #            'bluffdale',
#                 #
#                 #            'cottonwood-heights',
#                 #
#                 #            'draper',
#                 #
#                 #            'herriman',
#                 #            'holladay',
#                 #
#                 #            'midvale',
#                 #            'millcreek',
#                 #            'murray',
#                 #            'riverton',
#                 #            'salt-lake-city',
#                 #            'sandy',
#                 #            'south-jordan',
#                 #            'south-salt-lake',
#                 #            'taylorsville',
#                 #            'west-jordan', ]
#                 #
#                 # for c in citiiew:
#                 #     print(f"'https://www.zillow.com/c/real-estate-agent-reviews/{c}-ut/',")
#                         # urls = [
#                         #     # f'https://www.houzz.com/professionals/c/{c}',
#                         #         f'https://www.houzz.com/professionals/architect/c/{c}',
#                         #         f'https://www.houzz.com/professionals/design-build/c/{c}',
#                         #         f'https://www.houzz.com/professionals/general-contractor/c/{c}',
#                         #         f'https://www.houzz.com/professionals/home-builders/c/{c}',
#                         #         f'https://www.houzz.com/professionals/interior-designer/c/{c}',
#                         #         f'https://www.houzz.com/professionals/kitchen-and-bath/c/{c}',
#                         #         f'https://www.houzz.com/professionals/kitchen-and-bath-remodelers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/landscape-architect/c/{c}',
#                         #         f'https://www.houzz.com/professionals/landscape-contractors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/tile-stone-and-countertop/c/{c}',
#                         #         f'https://www.houzz.com/professionals/bedding-and-bath/c/{c}',
#                         #         f'https://www.houzz.com/professionals/furniture-and-accessories/c/{c}',
#                         #         f'https://www.houzz.com/professionals/carpenter/c/{c}',
#                         #         f'https://www.houzz.com/professionals/carpet-and-flooring/c/{c}',
#                         #         f'https://www.houzz.com/professionals/doors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/environmental-services-and-restoration/c/{c}',
#                         #         f'https://www.houzz.com/professionals/hardwood-flooring-dealers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/windows/c/{c}',
#                         #         f'https://www.houzz.com/professionals/furniture-refinishing-and-upholstery/c/{c}',
#                         #         f'https://www.houzz.com/professionals/glass-and-shower-door-dealers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/ironwork/c/{c}',
#                         #         f'https://www.houzz.com/professionals/kitchen-and-bath-fixtures/c/{c}',
#                         #         f'https://www.houzz.com/professionals/lighting/c/{c}',
#                         #         f'https://www.houzz.com/professionals/cabinets/c/{c}',
#                         #         f'https://www.houzz.com/professionals/closets-and-organization/c/{c}',
#                         #         f'https://www.houzz.com/professionals/paint-and-wall-coverings/c/{c}',
#                         #         f'https://www.houzz.com/professionals/handyman/c/{c}',
#                         #         f'https://www.houzz.com/professionals/home-staging/c/{c}',
#                         #         f'https://www.houzz.com/professionals/movers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/window-coverings/c/{c}',
#                         #         f'https://www.houzz.com/professionals/painters/c/{c}',
#                         #         f'https://www.houzz.com/professionals/photographer/c/{c}',
#                         #         f'https://www.houzz.com/professionals/agents-and-brokers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/roofing-and-gutter/c/{c}',
#                         #         f'https://www.houzz.com/professionals/artist-and-artisan/c/{c}',
#                         #         f'https://www.houzz.com/professionals/siding-and-exterior/c/{c}',
#                         #         f'https://www.houzz.com/professionals/fireplace/c/{c}',
#                         #         f'https://www.houzz.com/professionals/garage-door-repair/c/{c}',
#                         #         f'https://www.houzz.com/professionals/garage-doors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/building-supplies/c/{c}',
#                         #         f'https://www.houzz.com/professionals/stone-pavers-and-concrete/c/{c}',
#                         #         f'https://www.houzz.com/professionals/specialty-contractors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/staircases/c/{c}',
#                         #         f'https://www.houzz.com/professionals/wine-cellars/c/{c}',
#                         #         f'https://www.houzz.com/professionals/backyard-courts/c/{c}',
#                         #         f'https://www.houzz.com/professionals/hot-tub-and-spa-dealers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/driveways-and-paving/c/{c}',
#                         #         f'https://www.houzz.com/professionals/fencing-and-gates/c/{c}',
#                         #         f'https://www.houzz.com/professionals/garden-and-landscape-supplies/c/{c}',
#                         #         f'https://www.houzz.com/professionals/lawn-and-sprinklers/c/{c}',
#                         #         f'https://www.houzz.com/professionals/tree-service/c/{c}',
#                         #         f'https://www.houzz.com/professionals/outdoor-lighting-and-audio-visual-systems/c/{c}',
#                         #         f'https://www.houzz.com/professionals/outdoor-play/c/{c}',
#                         #         f'https://www.houzz.com/professionals/spa-and-pool-maintenance/c/{c}',
#                         #         f'https://www.houzz.com/professionals/pools-and-spas/c/{c}',
#                         #         f'https://www.houzz.com/professionals/decks-and-patios/c/{c}',
#                         #         f'https://www.houzz.com/professionals/appliances/c/{c}',
#                         #         f'https://www.houzz.com/professionals/electrical-contractors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/home-media/c/{c}',
#                         #         f'https://www.houzz.com/professionals/hvac-contractors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/plumbing-contractors/c/{c}',
#                         #         f'https://www.houzz.com/professionals/septic-tanks-and-systems/c/{c}',
#                         #         f'https://www.houzz.com/professionals/solar-energy-contractors/c/{c}',]
#
#                     # return  urls
#             z
#                 # print(url_liist)
#                             # yield scrapy.Request(url=urlsyo, callback=self.parse2)
#
#         # connyo.close()
#
#     # email_regex = re.findall(
#     #     "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
#     #     the_email)
#
#     # find_ph_num = re.findall(
#     #     "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",
#     #     b)
# # citiiew=['cottonwood-heights',
# # '',
# # 'draper',
# # 'midvale',
# # 'millcreek',
# # 'murray',
# # 'riverton',
# # 'salt-lake-city‎',
# # 'sandy',
# # 'south-jordan',
# # 'south-salt-lake',
# # 'taylorsville',
# # 'west-jordan',
# # 'west-valley-city',
# # 'bluffdale',
# #
# # 'cottonwood-heights',
# #
# # 'draper',
# #
# # 'herriman',
# # 'holladay',
# #
# # 'midvale',
# # 'millcreek',
# # 'murray',
# # 'riverton',
# # 'salt-lake-city',
# # 'sandy',
# # 'south-jordan',
# # 'south-salt-lake',
# # 'taylorsville',
# # 'west-jordan',]
#
#
# # https://www.zillow.com/c/real-estate-agent-reviews/orem-ut/
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
