import scrapy


class OmtScrapy(scrapy.Spider):
    name = "omt"

    start_urls = [
        # "https://viva.pressbooks.pub/openmusictheory/chapter/syncopation-in-pop-rock-music/"
        "https://viva.pressbooks.pub/openmusictheory/part/fundamentals/"
    ]

    def parse(self, response):
        if response:
            yield {
                "page_title": response.css("title::text").get(),
                "assignments": response.xpath(
                    '//*[@id="content"]/section/div[.//a[@id="assignments"]]/following-sibling::ol'
                ).get(),
                "file_urls": [
                    url
                    for url in response.xpath(
                        '//*[@id="content"]/section/div[.//a[@id="assignments"]]/following-sibling::ol'
                    )
                    .css("a::attr(href)")
                    .getall()
                    if url.endswith(".pdf")
                ],
            }

        next_page = response.css(".js-nav-next").css("a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
