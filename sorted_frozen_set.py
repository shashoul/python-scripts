from collections.abc import Sequence, Set
from itertools import chain
from bisect import bisect_left


class SortedFrozenSet(Sequence, Set):
    
    def __init__(self, items=None):
        self._items = tuple(sorted( 
            set(items) if (items is not None)
            else set()
        ))


    def __contains__(self, item):
        # index = bisect_left(self._items, item)
        # return (index != len(self._items)) and self._items[index] == item
        try:
            self.index(item)
            return True
        except ValueError:
            return False


    def __len__(self):
        return len(self._items)


    def __iter__(self):
        return iter(self._items)
        # for item in self._items:
            # yield item


    def __getitem__(self, index):
        #return self._items[index]
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )


    def __repr__(self):
        return "{type}({arg})".format(
            type=type(self).__name__,
            arg=(
                "[{}]".format(
                    ", ".join(map(repr,self._items))
                )
                if self._items
                else ""
            )
        )


    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items


    def __hash__(self):
        return hash((type(self), self._items))


    def __add__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return SortedFrozenSet(
            chain(self._items, rhs._items)
        )


    def count(self, item):
        return int(item in self)


    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError(f"{item!r} not found")