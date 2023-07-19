class Stack:
    def __init__(self):
        self.__stack = []

    @property
    def stack(self):
        return self.__stack

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self.__stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self.__stack[-1]

    def size(self):
        return len(self.__stack)


def is_balanced(text: str) -> bool:
    stack = Stack()
    openers = '([{'
    opposites = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for digit in text:
        if digit in openers:
            stack.push(digit)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != opposites.get(digit):
                return False
    return True


print(is_balanced('{{[()]}}'))
print(is_balanced('(((([{}]))))'))
print(is_balanced('[([])((([[[]]])))]{()}'))

print(is_balanced('}{}'))
print(is_balanced('{{[(])]}}'))
print(is_balanced('[[{())}]'))
