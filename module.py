import sys


def threeFive(number):

    """Returns multiples of three and five as string

    Args:
        number(int): current loop value for the range between 1 and 100

    Returns:
        string: a string value representing the number value or a string if:
        `Three` the number is just mutiple, `Five` the number is just multiple
        of five and `ThreeFive` if the number is multiple of both three and
        five.
    """

    strNumber = ''

    if (number % 3 is 0):
        strNumber += "Three"

    if (number % 5 is 0):
        strNumber += "Five"

    return strNumber if strNumber else str(number)


def main():
    """Loop from 1 to 100"""
    for round in range(1, 100):
        """Print multiples as string"""
        print(threeFive(round))


def init():
    if __name__ == "__main__":
        sys.exit(main())

init()
