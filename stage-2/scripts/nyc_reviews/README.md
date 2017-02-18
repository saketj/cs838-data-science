# NYC Restaurant Review Scraper - Based on Scrapy

# How to load urls

  - Open the `nyc_reviews/spiders/reviews_spider.py` file.
  - Add the list of restaurant urls that we scraped earlier in the `start_urls` Python list.
  - Modify the `index` variable to start outputting from the index of your portion of dataset.

### How to run

```sh
$ scrapy crawl reviews
```