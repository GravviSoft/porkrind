# # import scrapy
# #
# #
# # class PaginatezillowSpider(scrapy.Spider):
# #     name = 'paginatezillow'
# #     start_urls = ['https://www.zillow.com/c/real-estate-agent-reviews/cottonwood-heights-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/draper-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/midvale-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/millcreeak-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/murray-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/riverton-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/salt-lake-city‎-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/sandy-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/south-jordan-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/south-salt-lake-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/taylorsville-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/west-jordan-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/west-valley-city-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/bluffdale-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/cottonwood-heights-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/draper-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/herriman-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/holladay-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/midvale-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/millcreek-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/murray-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/riverton-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/salt-lake-city-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/sandy-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/south-jordan-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/south-salt-lake-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/taylorsville-ut/',
# # 'https://www.zillow.com/c/real-estate-agent-reviews/west-jordan-ut/',
# # ]
#
#     # def parse(self, response):
#
# #
# #  -*- coding: utf-8 -*-
# # import scrapy
# # import urlparse
# # from scrapy.linkextractors import LinkExtractor
# # from scrapy.spiders import CrawlSpider, Rule
# # from extract_emails import ExtractEmails
#
#
# class ZillowSpider(CrawlSpider):
#     name = 'zillow2'
#     def __init__(self, filename=None, *a, **kw):
#         super().__init__(*a, **kw)
#         if filename:
#             with open(f'{filename}') as f:
#                 self.start_urls = [url.strip() for url in f.readlines()]
#
#
#
#     def parse_item(self, response):
#         global industry
#         #businessname
#         businessname = response.css('span.ctcd-user-name::text').get()
#         #city
#         city = response.css('span.locality::text').get()
#         #Brokerage name or company
#         company = response.css('dd.profile-information-address::text').get()
#         #Industry
#         ind = (str(self.start_urls[0]))
#         ind = ind.split("/")[4]
#         ind = ind.split("-reviews")[0]
#         ind = ind.replace("-", " ")
#         industry = ind.title()
#         print(industry)
#         #all links on to on page that would contain an email.
#         linkwebsites = response.css('.zsg-lg-3-5 a::attr(href)').getall()
#         for url in linkwebsites:
#             em = ExtractEmails(url, depth=2, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.5)
#             emails = em.emails
#             for e in emails:
#                 yield {
#                     'Name': businessname,
#                     'Email': e,
#                     'Business': "your business.",
#                     'City': city,
#                     'Industry': industry,
#                     'Site': 'Zillow.com'
#                 }
#
#         #Go into teammembers profile pages
#         teammemberlinks = response.css('a.ptm-member-image-container::attr(href)').getall()
#         for teamlink in teammemberlinks:
#             teamlink = response.urljoin(teamlink)
#             print(teamlink)
#             if teamlink:
#                 yield scrapy.Request(url=teamlink, callback=self.teammemberpages)
#
#     def teammemberpages(self, response):
#
#         name = response.css('span.ctcd-user-name::text').get()
#         name = name.split(' ')[0]
#
#         city = response.css('span.locality::text').get()
#         company = response.css('dd.profile-information-address::text').get()
#         # Industry
#         print(industry)
#         # follow all links on the profile page that may contain an email.
#         linkwebsites = response.css('.zsg-lg-3-5 a::attr(href)').getall()
#         for url in linkwebsites:
#             em = ExtractEmails(url, depth=2, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.5)
#             emails = em.emails
#             for e in emails:
#                 yield {
#                     'Name': name,
#                     'Email': e,
#                     'Business': company,
#                     'City': city,
#                     'Industry': industry,
#                     'Site': 'Zillow.com'
#                 }
#
#
#
