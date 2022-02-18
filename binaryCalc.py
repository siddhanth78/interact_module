import sys

class binary_calc():

    def __init__(self, a, b, op):
        self.op = op
        self.a = a
        self.b = b
        
        if(self.a == None or self.b == None):
            print("Arrays cannot be null.")
            quit(0)
        
        if(len(self.a) != len(self.b)):
            print("Array lengths must be equal.")
            quit(0)
            
        bin1, bin2 = self.flip()
        
        if(self.op == 'add'):
            ans = self.add(bin1, bin2)
            
        elif(self.op == 'sub'):
            ans = self.sub(bin1, bin2)
            
        '''elif(self.op == 'mul'):
            ans = self.add(bin1, bin2)
            
        elif(self.op == 'div'):
            ans = self.add(bin1, bin2)'''
            
        self.display(ans)
        
    def flip(self):
        aflip = self.a.copy()
        bflip = self.b.copy()
        
        aflip.reverse()
        bflip.reverse()
        
        return aflip, bflip
        
    def complement(self, bin1):
    
        bin_comp = bin1.copy()
        
        one = [0] * len(bin1)
        one[-1] = 1
        
        for i in range(0, len(bin_comp)):
            if(bin1[i] == 0):
                bin_comp[i] = 1
            elif(bin1[i] == 1):
                bin_comp[i] = 0
                
        final = self.add(bin_comp, one)
        
        return final
            
        
    def display(self, ans):    
        print(f'{self.a} {self.op} {self.b} = {ans}')
    
    def add(self, bin_1, bin_2):
        bin1 = bin_1.copy()
        bin2 = bin_2.copy()
        carry = 0
        sum_ = [''] * len(bin1)
        
        for i in range(0, len(bin1)):
            if(carry == 0 and bin1[i] == 0 and bin2[i] == 0):
                sum_[i] = 0
                carry = 0
            elif(carry == 0 and bin1[i] == 0 and bin2[i] == 1):
                sum_[i] = 1
                carry = 0
            elif(carry == 0 and bin1[i] == 1 and bin2[i] == 0):
                sum_[i] = 1
                carry = 0
            elif(carry == 0 and bin1[i] == 1 and bin2[i] == 1):
                sum_[i] = 0
                carry = 1
            elif(carry == 1 and bin1[i] == 0 and bin2[i] == 0):
                sum_[i] = 1
                carry = 0
            elif(carry == 1 and bin1[i] == 0 and bin2[i] == 1):
                sum_[i] = 0
                carry = 1
            elif(carry == 1 and bin1[i] == 1 and bin2[i] == 0):
                sum_[i] = 0
                carry = 1
            elif(carry == 1 and bin1[i] == 1 and bin2[i] == 1):
                sum_[i] = 1
                carry = 1
                    
        return sum_
        
    def sub(self, bin_1, bin_2):
        bin1 = bin_1.copy()
        bin2 = bin_2.copy()
    
        bin_comp = self.complement(bin2)
        diff = self.add(bin1, bin_comp)
        
        return diff


def main():
    binary_calc([1,1,1], [0,0,1], 'sub')
    

main()