""" validate cli args and return them """

from argparse import Namespace, ArgumentParser


def process_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "filepath",
        help="the filepath for the dragon shield wishlist export file",
        type=str,
    )

    args = parser.parse_args()
    return args
