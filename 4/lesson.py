# def a(b, /, c, *, d):
#     pass
from typing import Callable, Iterable


# def a(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# res = a(
#     1, 2,
#     c=3,
#     b=4
# )
# print(res)

# res = lambda a, c: a + c
#
#
# def b(i, j):
#     return i + j
#
#
# print(b(1, 2))
# print(res(1, 2))

# even = lambda i: i % 2
# list_1 = [i for i in range(1, 10) if even(i)]
# print(list_1)


# d = {'a': 1, 'b': 2, 'c': 3}
# x = 5
# res = lambda i: {k: v + x for k, v in i.items()}
# print(res(d))


# from pydantic import BaseModel
#
#
# class A(BaseModel):
#     name: str
#     age: int
#     score: int
#
#
# l = [A(name="olesya", age=10, score=17), A(name="igor", age=10, score=11), A(name="van", age=18, score=5486)]
#
# srt_l = sorted(l, key=lambda i: (i.age, i.score))
# print(srt_l)


# def c(i):
#     return i + 1
#
#
# def a(*l, b: Callable):
#     for i in l:
#         yield b(i)
#
#
# l = [1, 2, 3]
# res = a(*l, b=c)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
