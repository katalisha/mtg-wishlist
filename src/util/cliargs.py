""" validate cli args and return them """

from argparse import Namespace, ArgumentParser


def process_args() -> Namespace:
    parser = ArgumentParser(
        prog="mtg wishlist",
        description="Searches stores for a wishlist of cards",
    )
    parser.add_argument(
        "-w",
        "--wishlist",
        help="the filepath for the dragon shield wishlist export file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-s",
        "--storelist",
        help="the filepath for list of stores to search",
        type=str,
        required=True,
    )
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    return args
