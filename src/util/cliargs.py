""" validate cli args and return them """

from argparse import Namespace, ArgumentParser


def process_args() -> Namespace:
    parser = ArgumentParser(
        prog="mtg wishlist",
        description="Searches stores for a wishlist of cards",
    )
    parser.add_argument(
        "filepath",
        help="the filepath for the dragon shield wishlist export file",
        type=str,
    )
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    return args
