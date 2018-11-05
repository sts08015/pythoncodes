
# coding: utf-8

# In[3]:


class TV:
    def __init__(self,channel,volume):
        self.channel = channel
        self.volume = volume
        self.power = False
    def turnOn(self):
        self.power = True
    def turnOff(self):
        self.power = False
    def setChannel(self):
        if self.power:
            self.channel+=1
    def setVolume(self):
        if self.power:
            self.volume+=1
    def __str__(self):
        a = "전원 : {} 볼륨 : {}, 채널 {}".format(self.power,self.volume,self.channel)
        return a


# In[6]:


x = TV(13,10)
x.turnOn()
print(x)
x.setVolume()
print(x)
x.setChannel()
print(x)

