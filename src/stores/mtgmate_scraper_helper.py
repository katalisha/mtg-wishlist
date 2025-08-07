"""MTG Mate Scraper Helper"""

from cards.card import Card
from decimal import Decimal
from lxml import html
from stores.scraper_helper import ScraperHelper


class MtgMateScraperHelper(ScraperHelper):
    """Scraper helper for scraping mtgmate.com"""

    def url(self, card: Card) -> str:
        url_name = card.name.replace(" ", "_").replace("&", "%26")
        foil = ":foil" if card.printing == "Foil" else ""
        return f"https://www.mtgmate.com.au/cards/{url_name}/{card.set_code}/{card.number}{foil}"

    def find_stock_level(self, result: str) -> int:
        tree = html.fromstring(result)  # type: ignore
        stock = tree.xpath(
            '//tr[@class="magic-card"]/td[@class="available-quantity"]/text()'
        )
        if isinstance(stock, list):
            if len(stock) > 0:
                if isinstance(stock[0], str):
                    return int(stock[0])
        return 0

    def find_price(self, result: str) -> Decimal | None:
        tree = html.fromstring(result)  # type: ignore
        price = tree.xpath('//tr[@class="magic-card"]/td[@class="price"]/text()')

        if isinstance(price, list):
            if len(price) > 0:
                if isinstance(price[0], str):
                    return Decimal(price[0].replace("$", ""))
