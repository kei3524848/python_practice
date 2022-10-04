import doctest


def average(values):
    """数値のリストから算術平均を計算
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()  # test fail時にはその旨のトレースが表示される
