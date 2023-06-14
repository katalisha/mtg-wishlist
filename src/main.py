""" Magic card wishlist checker - lets find those cards and go shopping """

from util.cliargs import process_args, Namespace
from util.output import Outputter
from wishlist import load_cards
from store import Store
from binderpos_store import BinderStore


def main(args: Namespace):
    wanted_cards = load_cards(args.filepath)
    stores: list[Store] = [
        BinderStore("Tabernacle", "tabernacle-games.myshopify.com"),
        BinderStore("Plenty of Games", "plenty-of-games-au.myshopify.com"),
        BinderStore("Good Games", "good-games-townhall.myshopify.com"),
        # https://www.cherrycollectables.com.au
        # https://www.mtgmate.com.au
    ]

    output = Outputter(args.verbose)

    for i, card in enumerate(wanted_cards):
        progress = i / len(wanted_cards)
        output.progress_bar(progress)

        output.card(card)
        for store in stores:
            has_card = store.check(card)
            output.store_has_card(store, has_card)

    output.progress_bar(1)

    for store in stores:
        limit = store.rate_limited_to()
        if limit is not None:
            output.requests_blocked(store.name, limit)

    output.shopping_list(stores)


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(process_args())
