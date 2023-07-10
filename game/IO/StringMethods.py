def text_length_limiter(string: str, index_digits: int) -> str:
    length = 20
    if (len(string) + index_digits) >= (length - index_digits):
        string = string[:(length - index_digits) - 4]
        string += "... "
    else:
        while (len(string)) < (length - index_digits):
            string += " "

    return string


def star_rating_spacer(star_rating_text: str, amount) -> str:
    while amount < 5:
        star_rating_text += " "
        amount += 1

    return star_rating_text
