from typing import Callable, Iterable


def fake_map(func: Callable, iterable: Iterable, *iterables: tuple[Iterable, ...] | Iterable):
    if iterables:
        all_iterables = [iterable, *iterables]
        for i in range(min(len(iterable) for iterable in all_iterables)):
            yield func(*[iterable_obj[i] for iterable_obj in all_iterables])
    else:
        for i in iterable:
            yield func(i)


# с одним итератором
fake_map_res = fake_map(lambda i: i + 1, [1, 2, 3])
map_res = map(lambda i: i + 1, [1, 2, 3])
assert fake_map_res.__next__() == map_res.__next__()
assert fake_map_res.__next__() == map_res.__next__()

# с несколькими итераторами
fake_map_res2 = fake_map(lambda i, j: i + j, [1, 2, 3], [2, 3, 4])
map_res2 = map(lambda i, j: i + j, [1, 2, 3], [2, 3, 4])
assert fake_map_res2.__next__() == map_res2.__next__()
assert fake_map_res2.__next__() == map_res2.__next__()

# с ошибкой StopIteration из-за разных длин итерируемых объектов
fake_map_res3 = fake_map(lambda i, j: i + j, [1, 2, 3], [2])
map_res3 = map(lambda i, j: i + j, [1, 2, 3], [2])
error_map = None
error_fake_map = None
try:
    fake_map_res3.__next__()
except Exception as e:
    error_map = type(e)
try:
    map_res3.__next__()
except Exception as e:
    error_fake_map = type(e)
assert error_map == error_fake_map
