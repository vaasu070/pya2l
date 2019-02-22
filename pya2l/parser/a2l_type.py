"""
@project: pya2l
@file: a2l_type.py
@author: Guillaume Sottas
@date: 11.02.2019
"""


class Ident(str):
    def dump(self, n=0):
        yield n, str(self)


class String(str):
    def dump(self, n=0):
        yield n, '"{}"'.format(str(self))


class Float(float):
    def dump(self, n=0):
        yield n, str(self)


class Int(int):
    def dump(self, n=0):
        yield n, str(self)


class Long(int):
    def dump(self, n=0):
        yield n, str(self)


class DataType(str):
    def dump(self, n=0):
        yield n, str(self)


class DataSize(str):
    def dump(self, n=0):
        yield n, str(self)


class AddrType(str):
    def dump(self, n=0):
        yield n, str(self)


class ByteOrder(str):
    def dump(self, n=0):
        yield n, str(self)


class IndexOrder(str):
    def dump(self, n=0):
        yield n, str(self)


class List(list):
    def dump(self, n=0):
        for e in self:
            for n in e.dump(n=n):
                yield n


class Offset(List):
    def __init__(self, offset):
        super(Offset, self).__init__([Long(o) for o in offset])

    def dump(self, n=0):
        yield n, ' '.join(next(x)[1] for x in [e.dump() for e in self])


class IdentList(List):
    def __init__(self, ident):
        super(IdentList, self).__init__([Ident(i) for i in ident])

    def dump(self, n=0):
        if len(self):
            for e in self:
                for n in e.dump(n=n):
                    yield n
        else:
            yield n, ''
