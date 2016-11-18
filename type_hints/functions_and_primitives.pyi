from typing import Union


class StubAnnotatedClass(object):
    def __init__(self, value: int) -> None:
        self.value = ... # type: int

    def function(self) -> str: ...
    def function1(self, argument: int) -> Union[str, int]: ...

