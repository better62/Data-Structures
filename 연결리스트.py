class sNode:
    def __init__(self,item):
        self.item=item #data field
        self.next=None #link field  
    def set_item(self,new_item):
        self.item=new_item
    def set_next(self,new_next):
        self.next=new_next
    def get_item(self):
        return self.item
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head=None  
    def is_empty(self):
        return self.head == None
        return 
    def add(self,item):  #adding the item in the front
        temp=sNode(item)  
        temp.set_next(self.head)
        self.head = temp
    def size(self): 
        current=self.head 
        count=0
        while current!=None:
            count+=1
            current = current.get_next()
        return count
    def search(self,item):  
        current=self.head
        found=False 
        while current!=None and found!=True:
            if (current.get_item()==item):
                found=True
            else:
                current=current.get_next()
        return found
    def delete(self,item):  
        current=self.head
        previous = None
        found=False
        while not found:
            if current.get_item() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    def append(self,item): 
        temp=sNode(item)
        current=self.head
        while current.get_next()!=None:
            current=current.get_next()
        current.set_next(temp)
    def printElement(self):
        current=self.head
        while current:
            if current.get_next()!=None:
                print(current.get_item(),'->',end=' ')
            else:
                print(current.get_item())
            current=current.get_next()

#main 함수-singly linked list 직접 확인해보기
s=LinkedList()
print(s.is_empty())
print(s.size())
s.add(1)
s.printElement() #1
s.add(2)
s.append(3)
s.printElement() #2->1->3
s.delete(3)
s.printElement() #2->1
print(s.search(4))  #False
