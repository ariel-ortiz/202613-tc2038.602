# O(1)
def is_even(n: int) -> bool:
    return (n & 1) == 0


# O(1)
def turn_uneven(n: int) -> int:
    return n | 1


# O(log N)
def count_one_bits(n: int) -> int:
    count: int = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count


# O(1)
def is_power_of_2(n: int) -> bool:
    return False if n <= 0 else (n - 1) & n == 0


# O(log N)
def floor_log2(n: int) -> int:
    if n <= 0:
        raise ValueError(f'floor_log2 is not defined for {n}')
    result: int = 0
    while n > 1:
        result += 1
        n >>= 1
    return result


# O(log min(abs(M), abs(N)))
def mul(m: int, n: int) -> int:
    negative: bool = (n < 0) ^ (m < 0)
    m = abs(m)
    n = abs(n)
    result: int = 0
    if n < m:
        n, m = m, n
    while m:
        result += n if (m & 1) else 0
        m >>= 1
        n <<= 1
    return -result if negative else result


if __name__ == '__main__':
    print(f'{is_even(4) = }')
    print(f'{is_even(13) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(665) = }')
    print(f'{turn_uneven(4) = }')
    print(f'{turn_uneven(13) = }')
    print(f'{turn_uneven(666) = }')
    print(f'{turn_uneven(665) = }')
    print(f'{count_one_bits(5) = }')
    print(f'{count_one_bits(8) = }')
    print(f'{count_one_bits(7) = }')
    print(f'{is_power_of_2(8) = }')
    print(f'{is_power_of_2(64) = }')
    print(f'{is_power_of_2(7) = }')
    print(f'{is_power_of_2(1) = }')
    print(f'{is_power_of_2(255) = }')
    print(f'{is_power_of_2(256) = }')
    print(f'{is_power_of_2(17) = }')
    print(f'{is_power_of_2(0) = }')
    print(f'{is_power_of_2(-8) = }')
    print(f'{floor_log2(8) = }')
    print(f'{floor_log2(128) = }')
    print(f'{floor_log2(10) = }')
    print(f'{floor_log2(25) = }')
    try:
        print(f'{floor_log2(0) = }')
    except ValueError:
        ...
    print(f'{mul(13, 17) = }')
    print(f'{mul(5, 20) = }')
    print(f'{mul(0, 7) = }')
    print(f'{mul(7, 0) = }')
    print(f'{mul(13, -17) = }')
    print(f'{mul(-13, 17) = }')
    print(f'{mul(-13, -17) = }')
