
# coding: utf-8

# In[1]:


class Stack:
    item = []
    def __init__(self):
        self.top = -1
    def push(self,x):
        self.top+=1
        Stack.item.append(x)
    def pop(self):
        if self.top > -1:
            print(Stack.item[self.top])
            del Stack.item[self.top]
            self.top-=1
    def print(self):
        for i in Stack.item:
            print(i,end = " ")
    def size(self):
        return len(Stack.item)
    def isEmpty(self):
        if len(Stack.item):
            return False
        return True


# In[ ]:


stack = Stack()
while True:
    command = input().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    if command[0] == "pop":
        stack.pop()
    if command[0] == "size":
        print(stack.size())
    if command[0] == "empty":
        print(stack.isEmpty())
    if command[0] == "print":
        print(stack.print())

