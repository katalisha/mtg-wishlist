""" util function to covert snake case to camel case """


def snake_to_camel(string: str) -> str:
    res = "".join(word.capitalize() for word in string.split("_"))
    return res[0].lower() + res[1:]
