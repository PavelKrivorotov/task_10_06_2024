from typing import Any


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
        if not isinstance(size, int):
            raise ValueError('')
        
        if size < 1:
            raise ValueError('')
        
        return size
    
    def add(self, value: Any) -> None:
        pass

    def pop(self) -> None:
        pass

    def show(self):
        item = self.head
        if isinstance(item, Item):
            print(id(item), item.value)

            while item.next != self.head and item.next != None:
                item = item.next
                print(id(item), item.value)


class Buffer_1(BaseBuffer):
    def __init__(self, size: int = 8) -> None:
        super().__init__(size)
        self.fill: int = 0

    def add(self, value: Any) -> None:
        if self.head is None:
            item = Item(value)
            item.next = item
            self.head = item
            self.tail = item
            self.fill += 1

        elif self.fill == self.size:
            self.tail = self.head
            self.tail.value = value
            self.head = self.head.next

        else:
            item = Item(value)
            self.tail.next = item
            self.tail = item
            self.tail.next = self.head
            self.fill += 1

    def pop(self) -> Any:
        item = self.head

        if self.fill == 0:
            raise StopIteration('No items in Buffer')
        
        elif self.fill == 1:
            self.head = None
            self.tail = None
            self.fill = 0
        
        elif self.fill == 2:
            self.tail.next = None
            self.head = self.tail
            self.fill = 1
        
        else:
            self.head = item.next
            self.tail.next = item.next
            self.fill -= 1

        return item.value


class Buffer_2(BaseBuffer):
    def __init__(self, size: int = 8) -> None:
        super().__init__(size)
        self.is_empty = True
        self._set_default()

    def _set_default(self) -> None:
        count = 0
        while count < self.size:
            item = Item()
            if count == 0:
                item.next = item
                self.head = item
                self.tail = item
            else:
                self.tail.next = item
                self.tail = item
                self.tail.next = self.head

            count += 1

        self.tail = self.head

    def add(self, value: Any) -> None:
        if self.tail == self.head and self.is_empty:
            self.head.value = value
            self.is_empty = False

        elif self.tail.next == self.head:
            self.tail = self.tail.next
            self.tail.value = value
            self.head = self.head.next

        else:
            self.tail = self.tail.next
            self.tail.value = value

    def pop(self) -> Any:        
        if self.is_empty:
            raise StopIteration('No items in Buffer')
        
        elif self.head == self.tail:
            value = self.head.value
            self.head.value = None
            self.is_empty = True
            return value
        
        else:
            value = self.head.value
            self.head.value = None
            self.head = self.head.next
            return value

