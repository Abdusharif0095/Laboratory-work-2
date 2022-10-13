import functools


def polindrome(num: int) -> bool:
    return (str(abs(num)) == "".join(reversed(str(abs(num)))))


def lists(nums):
    lst = [[], [], []]
    mods = [2, 3, 5]

    for num in nums:
        for i in range(3):
            if num % mods[i] == 0:
                lst[i].append(num)

    return lst[0], lst[1], lst[2]


def reverse_num(num: int) -> int:
    return (-(num < 0) + (num > 1)) * int(("".join(reversed(str(abs(num))))))


def NewtonMethod(a, n):
    xk = 1
    xk1 = (1 / n) * ((n - 1) * xk + a / xk ** (n - 1))
    while abs(xk1 - xk) > 0.00001:
        xk = xk1
        xk1 = (1 / n) * ((n - 1) * xk + a / xk ** (n - 1))

    return xk1


def is_prime(num: int) -> bool:
    for i in range(int(num ** (1 / 2) + 1)):
        if num % i == 0:
            return False

    return True


cache_map = {}


def cache_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cache_map
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        key = ", ".join(args_repr + kwargs_repr)
        if key in cache_map:
            return cache_map[key]
        else:
            value = func(*args, **kwargs)
            cache_map[key] = value
            return value

    return wrapper


cnt = 5
cache_map_cnt = {}
cache_map_val = {}


def cache_function_cnt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cnt
        global cache_map_cnt
        global cache_map_val
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        key = ", ".join(args_repr + kwargs_repr)
        if key in cache_map_cnt and cache_map_cnt[key] != 0:
            cache_map_cnt[key] -= 1
            return cache_map_val[key]
        else:
            value = func(*args, **kwargs)
            cache_map_val[key] = value
            cache_map_cnt[key] = cnt - 1
            return value

    return wrapper


@cache_function
def factorial(n: int) -> int:
    return n * factorial(n - 1) if n >= 1 else 1


@cache_function_cnt
def factorial2(n: int) -> int:
    return n * factorial2(n - 1) if n >= 1 else 1


# print(factorial(6))
# print(round(NewtonMethod(7**7, 7), 5))
# print(polindrom(-22))
# print(lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
# print(reversed_num(-123))
