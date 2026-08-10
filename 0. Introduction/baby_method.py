def baby_method(s: float, guess: float, delta: float) -> float:
    if s < 0:
        raise ValueError(f'Cannot compute square root of: {s}')
    prev: float = guess
    while True:
        guess = (prev + s / prev) / 2
        if abs(guess - prev) <= delta:
            return guess
        prev = guess


# print(f'__name__ == {__name__}')


if __name__ == '__main__':
    x: float = 30
    result: float = baby_method(x, 5, 0.0001)
    print(f'sqrt {x} = {result} ({result * result})')
