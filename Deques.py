class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)


character_deque = Deque()

def palindrome_checker(string):
    for ch in string:
        character_deque.add_rear(ch)

    still_equal = True

    while character_deque.size() > 1 and still_equal:
        first = character_deque.remove_front()
        last = character_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(palindrome_checker('radar'))
print(palindrome_checker(''))

