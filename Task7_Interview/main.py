brackets_example = '((({[]})))'


class Stack:

    def __init__(self):
        self.stack_obj = []

    def is_empty(self):
        if len(self.stack_obj) == 0:
            return True
        else:
            return False

    def push(self, new_el):
        self.stack_obj.append(new_el)

    def pop(self):
        return self.stack_obj.pop(-1)

    def peek(self):
        return self.stack_obj[-1]

    def size(self):
        return len(self.stack_obj)

    def check(self, brackets_str):
        brackets = [('(', ')'), ('[', ']'), ('{', '}')]
        if len(brackets_str) % 2 != 0:
            print('Несбалансировано')
            return False
        elif len(brackets_str) == 0:
            print('Сбалансировано')
            return True

        for sign in list(brackets_str):
            for bracket_pair in brackets:
                if sign == bracket_pair[0]:
                    self.push(sign)
                elif sign == bracket_pair[1] and self.size() > 0 and self.pop() != bracket_pair[0]:
                    print('Несбалансировано')
                    return False
            brackets_str = brackets_str.replace(sign, '', 1)
            if self.is_empty() and len(brackets_str) != 0:
                self.check(brackets_str)
                return True
            elif self.is_empty() and len(brackets_str) == 0:
                print('Сбалансировано')
                return True


if __name__ == '__main__':
    brackets_obj = Stack()
    brackets_obj.check(brackets_example)
