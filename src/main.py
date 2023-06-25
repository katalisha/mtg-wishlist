""" Magic card wishlist checker - lets find those cards 🤑 """

from cliargs import process_args, Namespace
from renderer import Renderer
from cards.wishlist import load_cards
from stores.store_list import load_stores
from stores.store import CardSearchFailure

# TODO https://www.cherrycollectables.com.au
# TODO try mypy


def main(args: Namespace):
    wishlist = load_cards(args.wishlist)
    stores = load_stores(args.storelist)
    render = Renderer(args.verbose)
    total_cards = len(wishlist)
    errors: bool = False

    for i, card in enumerate(wishlist):
        render.next_card(card, i, total_cards)

        for store in stores:
            try:
                has_card = store.search_for_card(card)
                render.card_search_result(store, has_card)
            except CardSearchFailure as exc:
                errors = True
                render.card_search_error(store.name, str(exc.__cause__.__class__))

    render.done(stores)

    for store in stores:
        limit = store.rate_limited_to()
        if limit is not None:
            render.requests_blocked(store.name, limit)

    if errors:
        print("there were some errors use --verbose to see details")


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(process_args())
