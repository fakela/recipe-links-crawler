import scrapy


class YummlySpider(scrapy.Spider):
    name = 'yummly'
    allowed_domains = ['yummly.com']
    start_urls = ['https://www.yummly.com/recipes?q=meatballs&taste-pref-appended=true']

    def parse(self, response):
        #gets the recipe link,author and ingredient
        for product in response.css("div.RecipeContainer"):
            yield {
                "link": product.css("a.card-title::attr(href)").extract(),
                "author": product.css("span a.source-link::text").extract(),
                "ingredients": [''.join(li.css('span::text').extract()).replace(
          u'\xa0', u' ').strip() for li in product.css('div.recipe-ingredients li')]          
            }


        # next_url_path = response.css(
        #     "a[rel='next']::attr('href')").extract_first()
        # if next_url_path:
        #     yield scrapy.Request(
        #         response.urljoin(next_url_path),
        #         callback=self.parse
        #     )