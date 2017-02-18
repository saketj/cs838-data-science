import scrapy


class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    index = 106
    start_urls = [
        'https://www.nytimes.com/2016/06/01/dining/hungry-city-nabaya-restaurant-bronx.html?rref=collection%2Fcollection%2Frestaurant-guide',
        'http://www.nytimes.com/2009/06/17/dining/reviews/17rest.html?rref=collection%2Fcollection%2Frestaurant-guide',
	'http://www.nytimes.com/2012/08/01/dining/reviews/reynard-in-williamsburg-brooklyn-restaurant-review.html?rref=collection%2Fcollection%2Frestaurant-guide'
    ]

    def parse(self, response):
        filename = 'review-%s.txt' % ReviewsSpider.index
	ReviewsSpider.index = ReviewsSpider.index + 1
	restaurant_name = response.css('#story-meta > div.review-meta > div.meta-group > h4::text').extract_first().encode('utf-8').strip();
	restaurant_cuisine = response.css('#story-meta > div.review-meta > div.meta-group > ul > li.cuisine::text').extract_first().encode('utf-8').strip();
	restaurant_address = response.css('#story-meta > div.review-meta > div.meta-group > ul > li.postal-address > span::text').extract_first().encode('utf-8').strip();
	restaurant_phone = response.css('#story-meta > div.review-meta > div.meta-group > ul > li.telephone::text').extract_first().encode('utf-8').strip()
	review_body = response.css('p.story-body-text::text')
        with open(filename, 'wb') as f:
            f.write(restaurant_name + '\n' + restaurant_cuisine + '\n' + restaurant_address + '\n' + restaurant_phone + '\n')
	    for line in review_body:
		f.write(line.extract().encode('utf-8') + '\n')

		
