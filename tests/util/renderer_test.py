"""
Test renderer methods
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from _pytest.capture import CaptureFixture
from renderer import Renderer
from cards.card import Card
from stores.store import StockedCard, Store


@dataclass()
class MockStore(Store):
    """Mock store for testing purposes"""

    # pylint: disable=unused-argument
    def perform_search_for_card(self, card: Card) -> StockedCard | None:
        return None

    def rate_limited_to(self) -> datetime | None:
        return None


def test_card_str():
    renderer = Renderer(verbose=False)
    card = Card("Ao, the Dawn Sky", "NEO", "Kamigawa: Neon Dynasty", "406", "Normal")
    result = renderer.card_str(card)
    expected = "\u001b[0;35m\u001b[1mAo, the Dawn Sky\u001b[0m \u001b[2m(Kamigawa: Neon Dynasty, 406)\u001b[0m\u001b[0m"
    assert result == expected


def test_card_str_highlight():
    renderer = Renderer(verbose=False)
    card = Card("Ao, the Dawn Sky", "NEO", "Kamigawa: Neon Dynasty", "406", "Normal")
    result = renderer.card_str(card, highlight=True)
    expected = "\u001b[1;33m\u001b[1mAo, the Dawn Sky\u001b[0m \u001b[2m(Kamigawa: Neon Dynasty, 406)\u001b[0m\u001b[0m"
    assert result == expected


def test_card_search_result_found(capsys: CaptureFixture[str]):
    renderer = Renderer(verbose=True)
    store = MockStore("test")  # pylint: disable=too-many-function-args
    renderer.card_search_result(store, True)
    captured = capsys.readouterr()
    assert captured.out == "\u001b[0;32m\u2713 test\u001b[0m\n"


def test_card_search_result_not_found(capsys: CaptureFixture[str]):
    renderer = Renderer(verbose=True)
    store = MockStore("test")  # pylint: disable=too-many-function-args
    renderer.card_search_result(store, False)
    captured = capsys.readouterr()
    assert captured.out == "⨷ \x1b[9mtest\u001b[0m\n"


def test_shopping_list(capsys: CaptureFixture[str]):
    renderer = Renderer(verbose=False)
    store = MockStore("Test Store")  # pylint: disable=too-many-function-args
    card1 = Card("Ao, the Dawn Sky", "NEO", "Kamigawa: Neon Dynasty", "406", "Normal")
    card2 = Card("Another Card", "SET", "Set Name", "123", "Normal")
    store.cards.append(StockedCard(card1, Decimal("5.00")))
    store.cards.append(StockedCard(card2, Decimal(3.50)))

    renderer.shopping_list([store], [card1])

    captured = capsys.readouterr()
    expected_output = (
        "\n\u001b[1mTest Store\x1b[0m: $8.50\n"
        "✓ \u001b[1;33m\u001b[1mAo, the Dawn Sky\x1b[0m \x1b[2m(Kamigawa: Neon Dynasty, 406)\x1b[0m\x1b[0m @ $5.00\n"
        "✓ \u001b[0;35m\u001b[1mAnother Card\x1b[0m \x1b[2m(Set Name, 123)\x1b[0m\x1b[0m @ $3.50\n"
    )
    assert captured.out == expected_output
