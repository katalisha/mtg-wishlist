""" Magic card wishlist checker - lets find those cards and go shopping """

from util.cliargs import process_args, Namespace
from util.output import output_store_has_card, output_card, output_requests_blocked
from wishlist import load_cards
from store import Store
from binderpos_store import BinderStore


def main(args: Namespace):
    wanted_cards = load_cards(args.filepath)
    stores: list[Store] = [
        BinderStore("Tabernacle", "tabernacle-games.myshopify.com"),
        BinderStore("Plenty of Games", "plenty-of-games-au.myshopify.com"),
        # Store("Good Games", "good-games-townhall.myshopify.com"),
        # https://www.cherrycollectables.com.au
        # https://www.mtgmate.com.au
    ]

    for card in wanted_cards:
        print(output_card(card))
        for store in stores:
            has_card = store.check(card)
            print(output_store_has_card(store, has_card))

    for store in stores:
        limit = store.rate_limited_to()
        if limit is not None:
            print(output_requests_blocked(store.name, limit))


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(process_args())
