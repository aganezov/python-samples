# -*- coding: utf-8 -*-
from __future__ import absolute_import
from typing import List, Union
from typing import Optional

from datetime import date


# functions || int / str


def function(argument1: int, argument2: str) -> str:
    return argument2


a = function(5, "5")





























# Objects with inline type specification

class C(object):
    foo = None  # type: Optional[List[str]]

    def __init__(self, bar):
        self.bar = bar  # type: Optional[str]

    @staticmethod
    def f2():
        """ return type is automatically inferred """
        return "foo"

    @staticmethod
    def f3():
        x = C.f2()
        return x.upper()






















class StubAnnotatedClass(object):

    def __init__(self, value):
        self.value = value

    def function(self):
        if self.value < 100:
            return "sting1"
        else:
            return "sting2"

    def function1(self, argument):
        if argument > 5 and self.value < 100:
            return "string"
        else:
            return 10


























def collected_function(argument1: Union[int, str], argument2: Union[int, str]) -> Union[int, str]:
    if argument1 > argument2:
        return argument1
    return argument2














if __name__ == "__main__":
    print(collected_function(1, 2))
    print(collected_function(2, 3))
    print(collected_function(3, 4))
    print(collected_function("string1", "string2"))




