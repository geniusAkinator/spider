from tutorial.items import TutorialItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
class DmozSpider(RedisCrawlSpider):
	"""docstring for ClassName"""
	name = "domz"
	allowed_domains = ['www.comicat.org']
	# start_urls = ['http://www.comicat.org/1.html']
	redis_key = "redisQueue"

	# list_page = LinkExtractor(allow=r'http://www.comicat.org/\d+.html')

	list_page = LinkExtractor(allow=r'\d+.html')

	rules = (
		Rule(list_page , callback='parse_item' , follow=True),
	)

	def parse_item(self,response):
		item = TutorialItem()
		lis = response.xpath('//tbody[@id="data_list"]//tr')
		for tr in lis:
			item['title'] = tr.xpath('//td[3]/a/text()').get()
			item['magnet'] = 'magnet:?xt=urn:btih:'+tr.xpath('//td[3]/a/@href').get().split('-')[1].split('.')[0]
			yield item 

# filename = response.url.split("/")[-2]
# with open(filename,'wb') as f: