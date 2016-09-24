from random import choice

class Element():
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return '[ %s ]' % self.value


class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            if self.first == self.last:
                return '[ %s ]' % self.first.value
            current = self.first
            out_string = '[' + ' %s <->' % str(current.value)
            while current.next != self.last:
                current = current.next
                out_string += ' %s <->' % str(current.value)
            out_string += ' %s ]' % self.last.value
            return out_string
        else:
            return 'The list is empty'

    def __getitem__(self, i):
        if i < 0:
            i = self.length + i
        if i > self.length or i < 0:
            return 'list index out of range'
        else:
            current = self.first
            for j in range(self.length):
                if i == j:
                    return current
                current = current.next

    def __iter__(self):
        current = self.first
        while current.next != None:
            yield current
            current = current.next
        raise StopIteration

    def __len__(self):
        return self.length         

    def random(self, minimal=3, maximal=10):
        for i in range(choice(range(minimal, maximal))):
            self.add(choice(range(10)))
        print('Generated random linked list:\n', self)

    def add(self, value, index=None):
        self.length += 1
        if self.first != None and index == None:
            self.last.next = self.last = Element(value, self.last)
        elif self.first == None and index == None:
            self.first = self.last = Element(value, self.last)
        elif index >= self.length - 1 or index < 0:
            self.length -= 1
            print('Index must be in range 0 to %s' % str(self.length - 1))
        else:
            current = self.first
            for i in range(index + 1):
                if i == index:
                    if current == self.first:
                        self.first = self.first.prev = Element(value, None, self.first)
                    elif current == self.last:
                        self.last.next = self.last = Element(value, self.last)
                    else:
                        current.prev.next = current.prev = Element(value, current.prev, current)
                    break
                current = current.next

    def delete(self, index):
        if index >= self.length or index < 0:
            print('Index must be in range 0 to %s' % str(self.length - 1))
        else:
            current = self.first
            for i in range(index + 1):
                if i == index:
                    if current == self.first:
                        self.first = self.first.next
                        self.first.prev = None
                    elif current == self.last:
                        self.last = self.last.prev
                        self.last.next = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    break
                current = current.next

    def clear(self):
        self.__init__()

if __name__ == '__main__':
    ll = LinkedList()
    ll.random()
    for i in ll:
        print(i.value)