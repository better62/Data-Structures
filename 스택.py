#Stack

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        if self.top==None:
            return True
        else:
            return False

    def push(self, value):
        new=Node(value)
        new.next = self.top
        self.top = new
            
    def pop(self):
        if self.is_empty():
            print('empty!')
        value = self.top.value
        self.top = self.top.next
        return value

    def display(self):
        temp=self.top
        while temp:
            print(temp.value, end=' -> ')
            temp=temp.next
        print()

    def who_is_top(self):
        if self.is_empty():
            print('empty')
        else:
            print(self.top.value)
            


def main():
    stack=Stack()

    stack.push('a')
    stack.display()
    
    stack.push('b')
    stack.display()
    stack.who_is_top()
    
    stack.push('c')
    stack.display()
    stack.who_is_top()

    stack.pop()
    stack.display()
    stack.who_is_top()
    
    stack.pop()

    stack.display()
            
main()
