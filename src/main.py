""" Magic card wishlist checker - lets find those cards 🤑 """

from cliargs import process_args, Namespace
from renderer import Renderer
from cards.wishlist import load_cards
from stores.store_list import load_stores

# TODO https://www.cherrycollectables.com.au
# TODO https://www.mtgmate.com.au


def main(args: Namespace):
    wishlist = load_cards(args.wishlist)
    stores = load_stores(args.storelist)
    render = Renderer(args.verbose)
    total_cards = len(wishlist)

    for i, card in enumerate(wishlist):
        render.next_card(card, i, total_cards)

        for store in stores:
            has_card = store.check(card)
            render.store_has_card(store, has_card)

    render.done(stores)

    for store in stores:
        limit = store.rate_limited_to()
        if limit is not None:
            render.requests_blocked(store.name, limit)


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(process_args())
