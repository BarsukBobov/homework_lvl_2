from typing import Callable, Iterable


def fake_map(func: Callable, iterable: Iterable, *iterables: tuple[Iterable, ...] | Iterable):
    if iterables:
        sum_iterables = [iterable, *iterables]
        for i in range(max(len(iterable) for iterable in sum_iterables)):
            args = [iterable[i] if i < len(iterable) else None for iterable in sum_iterables]
            yield func(*args)
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
