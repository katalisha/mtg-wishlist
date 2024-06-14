"""
Test wishlist methods
"""

from cards.wishlist import convert_row_to_card
from cards.card import Card


def test_successful_card_creation():
    expected_card = Card(
        "Ao, the Dawn Sky", "NEO", "Kamigawa: Neon Dynasty", "406", "Normal"
    )
    row = {
        "Quantity": "1",
        "Card Name": "Ao, the Dawn Sky",
        "Set Code": "NEO",
        "Set Name": "Kamigawa: Neon Dynasty",
        "Card Number": "406",
        "Condition": "NearMint",
        "Printing": "Normal",
        "Language": "English",
        "LOW": "3.20",
        "MID": "5.20",
        "MARKET": "5.02",
    }
    card = convert_row_to_card(row)
    assert card.__dict__ == expected_card.__dict__


def test_unknown_printing_returns_empty_string():
    row = {
        "Quantity": "1",
        "Card Name": "Ao, the Dawn Sky",
        "Set Code": "NEO",
        "Set Name": "Kamigawa: Neon Dynasty",
        "Card Number": "406",
        "Condition": "NearMint",
        "Printing": "Something weird",
        "Language": "English",
        "LOW": "3.20",
        "MID": "5.20",
        "MARKET": "5.02",
    }
    card = convert_row_to_card(row)
    assert card.printing == ""


def test_missing_field_returns_none():
    row = {
        "Card Name": "Ao, the Dawn Sky",
        "Set Code": "NEO",
        "Set Name": "Kamigawa: Neon Dynasty",
        "Card Number": "406",
        "Condition": "NearMint",
        "Printing": "Normal",
        "Language": "English",
        "LOW": "3.20",
        "MID": "5.20",
        "MARKET": "5.02",
    }
    card = convert_row_to_card(row)
    assert card is None


def test_bad_heading_returns_none():
    row = {
        "Quantity": "1",
        "nombre de tarjeta": "Ao, the Dawn Sky",
        "Set Code": "NEO",
        "Set Name": "Kamigawa: Neon Dynasty",
        "Card Number": "406",
        "Condition": "NearMint",
        "Printing": "Normal",
        "Language": "English",
        "LOW": "3.20",
        "MID": "5.20",
        "MARKET": "5.02",
    }
    card = convert_row_to_card(row)
    assert card is None
