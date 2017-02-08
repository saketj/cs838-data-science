import scrapy
import re

class CityDataSpider(scrapy.Spider):
    name = "city_data"
    start_urls = [
        'http://www.city-data.com/zipmaps/New-York-New-York.html'
    ]

    def parse(self, response):
        for zipcode in response.css('div.data-block'):
            try:
                yield {
                    'zipcode': zipcode.css('::attr(id)').re(r'(\d+)')[0],
                    'population': re.sub(r',|\D', '', zipcode.css('::text')[7].extract()),
                    'population_density': re.sub(r',|\D', '', zipcode.css('::text')[28].extract()),
                    'cost_of_living': re.sub(r',|\s', '', zipcode.css('::text')[16].extract()),
                    'median_real_state_value': re.sub(r',|\D', '', zipcode.css('::text')[52].extract()),
                    'median_household_income': re.sub(r',|\D', '', zipcode.css('::text')[54].extract())
                }
            except:
                print 'Something went wrong for zipcode %s' % zipcode.css('::attr(id)').re(r'(\d+)')[0]
