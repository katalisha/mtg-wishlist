""" Magic card wishlist checker - lets find those cards and go shopping """

from util.cliargs import process_args, Namespace
from wishlist import load_cards


def main(args: Namespace):
    wanted_cards = load_cards(args.filepath)
    print(wanted_cards)


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(process_args())
