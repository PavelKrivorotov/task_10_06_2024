### *Question 1*
### Hаписать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.

*Пример:*
```python
def is_even(value) -> bool:
    return value % 2 == 0
```

*Аналогичный по функциональности, но отличный по сути (even.py)*
```python
def is_even(value) -> bool:
    return value & 1 == 0
```

*Подробности:*

Увеличения или ухудшения производительности не выявлено *(возможно компилятор python-а компилирует один и тот же байт-код для этих двух функций)*.

В `примере` вычисляется остаток от деления *(если число чётное, то при делении на 2 остаток будет равен 0, иначе 1)*

В `аналогичной реализации` вычисляется битовая операция "И" *(если число чётное, то в двоичной записи младший бит этого числа будет равен 0,
иначе 1. Далее происходит сравнение младшего бита числа с еденицей - если в бите записан 0, тогда результат выражения 0 & 1 будет
равен 0 - число чётное, если записана 1, тогда 1 & 1 равняется 1 - число нечётное)*

### Question 2
### Написать несколько реализаций циклического буфера FIFO.

*buffer.py*
```python
class Item:
    def __init__(self, value: Any = None) -> None:
        self.value: Any = value
        self.next: 'Item' = None

class BaseBuffer:
    def __init__(self, size: int = 8) -> None:
        self.size = self._size(size)
        self.head: Item = None
        self.tail: Item = None

    def _size(self, size: int) -> int:
        ...
    
    def add(self, value: Any) -> None:
        pass

    def pop(self) -> None:
        pass

    def show(self):
        ...

class Buffer_1(BaseBuffer):
    def __init__(self, size: int = 8) -> None:
        super().__init__(size)
        self.fill: int = 0

    def add(self, value: Any) -> None:
        ...

    def pop(self) -> None:
        ...

class Buffer_2(BaseBuffer):
    def __init__(self, size: int = 8) -> None:
        super().__init__(size)
        self.is_empty = True
        self._set_default()

    def _set_default(self) -> None:
        ...

    def add(self, value: Any) -> None:
        ...

    def pop(self) -> Any:        
        ...
```

*Подробности:*

`Buffer_1` ...

`Buffer_2` ...

### Question 3
