import random

class standinfo():

    def __init__(self, standNames, singletotal, standstotal):
        
        self.standNames = standNames
        self.singletotal = singletotal
        self.standstotal = standstotal
        
        for i in range(3):
            self.standstotal = self.sellHotDogs(self.standNames[i], random.randint(100,1000), self.singletotal, self.standstotal)
            
        self.displayAll(self.standstotal)
        
        return
        
    def sellHotDogs(self, name, ID, onestand, allstands):
        
        onestand = 0
        for i in range(random.randint(1,25)):
            onestand+=1
            allstands+=1
        self.displayInfo(name, ID, onestand)
        return allstands
        
    def displayInfo(self, name, ID, onestand):
        
        print(f"Name: {name}")
        print(f"ID: {ID}")
        print(f"Sold: {onestand}\n")
        
    def displayAll(self, allstands):
    
        print(f"Total sold: {allstands}")


def main():
    
    stands = ['Stand1', 'Stand2', 'Stand3']
    totalsold = 0
    alltotalsold = 0
    
    standinfo(stands, totalsold, alltotalsold)

main()
