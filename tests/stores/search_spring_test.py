""" test search_string store """
from stores.search_spring import Inventory, Product, SearchSpringStore
import pathlib
from decimal import Decimal
from cards.card import Card


def test_valid_json():
    filepath = pathlib.Path(__file__).parent / "searchspring_found.json"

    with open(filepath, "r", encoding="utf-8") as file:
        data = file.read()
        result = Inventory.parse_raw(data)

        p1 = Product(
            collection_handle=[
                "all",
                "foil",
                "gaming-singles",
                "in-stock",
                "kamigawa-neon-dynasty",
                "latest-singles",
                "magic-the-gathering-singles",
                "single",
                "singles",
                "stock-not-including-pre-orders",
                "under-5",
                "under-99",
            ],
            name="FOIL SHOWCASE Hidetsugu, Devouring Chaos 378 -  Kamigawa Neon Dynasty",
            price=Decimal("1.99"),
        )
        p2 = Product(
            collection_handle=[
                "all",
                "gaming-singles",
                "in-stock",
                "kamigawa-neon-dynasty",
                "latest-singles",
                "magic-the-gathering-singles",
                "single",
                "singles",
                "stock-not-including-pre-orders",
                "under-5",
                "under-99",
            ],
            name="SHOWCASE Hidetsugu, Devouring Chaos 378 -  Kamigawa Neon Dynasty",
            price=Decimal("0.99"),
        )

        expected = Inventory(products=[p1, p2])
        print(expected)

        assert result == expected


def test_build_request():
    store = SearchSpringStore("Cherry Collectables", "https://kq0hnn.a.searchspring.io")
    card = Card(
        name="Hidetsugu Consumes All",
        set_code="NEO",
        set_name="Kamigawa: Neon Dynasty",
        number="361",
        printing="Normal",
    )
    result = store.build_request_params(card)
    assert result == {
        "siteId": "kq0hnn",
        "bgfilter.collection_handle": "magic-the-gathering-singles",
        "resultsFormat": "native",
        "q": "361 Kamigawa: Neon Dynasty",
    }
