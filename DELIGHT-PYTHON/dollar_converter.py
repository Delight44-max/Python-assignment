def exchange(dollar):
    if type(dollar) == str:
        raise ValueError("Dollar amount must be a number")

    naira = 1550 * dollar
    return naira