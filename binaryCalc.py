
class binary_calc():

    def __init__(self, a, b, op):
    
        self.op = op
        self.a = a
        self.b = b
        
        if(self.op == 'add'):
            sum = self.add()
            
        elif(self.op == 'sub'):
            sum = self.add()
            
        elif(self.op == 'mul'):
            sum = self.add()
            
        elif(self.op == 'div'):
            sum = self.add()
        
        
    def add(self):
    
        for(i in range(0,len(self.a))):
            if(self.a[i] == 0):
                self.a[i] == 'false'
            elif(self.a[i] == 1):
                self.a[i] == 'true'
        







def main():
    binary_calc()