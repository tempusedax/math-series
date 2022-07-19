from series_module.series_package import fibonacci, lucas, sum_series


def test_fibonacci_one():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(14)
    expected = 377
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_two():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_three():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series():
    actual = sum_series(7)
    expected = 42
    assert actual == expected


def test_sum_series():
    actual = sum_series(10)
    expected = 178
    assert actual == expected

