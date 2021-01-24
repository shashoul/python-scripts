DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}


def convert(s):
    number = ''
    try:
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Succeed")
    except (KeyError, TypeError) as e:
        print(f"convert Faild!!, {e!r}")
        x = -1
    return x