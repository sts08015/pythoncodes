
# coding: utf-8

# In[7]:


class Queue:
    item = []
    def push(self,x):
        Queue.item.append(x)
    def pop(self):
        if len(Queue.item):
            print(Queue.item[0])
            del Queue.item[0]
    def print(self):
        for i in Queue.item:
            print(i,end = " ")
    def size(self):
        return len(Queue.item)
    def isEmpty(self):
        if len(Queue.item):
            return False
        return True


# In[ ]:


q = Queue()
while True:
    command = input().split()
    if command[0] == "push":
        q.push(int(command[1]))
    if command[0] == "pop":
        q.pop()
    if command[0] == "size":
        print(q.size())
    if command[0] == "empty":
        print(q.isEmpty())
    if command[0] == "print":
        print(q.print())

