
# coding: utf-8

# In[29]:


class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calcPermeter(self):
        return 2*3.14*self.radius
    def calcArea(self):
        return 3.14*self.radius*self.radius


# In[31]:


a = Circle(50)
print("반지름: {} 원의 면적: {} 원의 둘레: {}".format(a.radius,a.calcPermeter(),a.calcArea()))

