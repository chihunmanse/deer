class Penalty:
    def __init__(self):
        self.a = 0
  
class OutSidePenalty(Penalty):
    def hi(self):
        self.a = self.a + 10
        return self.a
 
class AreaPenalty(Penalty):
    def hi(self):
        if 1:
            self.a = 20
        return self.a


list = [OutSidePenalty(), AreaPenalty()]
b = 0
for i in list:
    print(i.hi())
    
    

print(b)