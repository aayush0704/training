####from abc import ABC,abstractmethod
####
####class abs_cal(ABC):
####    @abstractmethod
####    def add():
####        pass
####    
####    @abstractmethod
####    def sub():
####        pass
####
####
####class cal(abs_cal):
####    @staticmethod
####    def add(a,b):
####        return a+b;
####    @staticmethod
####    def sub(a,b):
####        return a-b;
####    
####
####print(cal.add(7,9))
####
####
####
####    
##
##class hospital:
##
##    h_nm='apollo'
##    h_loc='patia'
##    def __init__(self,pnm):
##        self.__pnm=pnm
##
##    
##    def get(self):
##        print(self.__pnm)
##    
##        
##patient1=hospital('abcd')        
##   

##try:
##    x = int(input("Enter: "))
##except ValueError:
##    print("Invalid input")
##else:
##    print("You entered:", x)

##import re
##print(re.findall("[0-9]", "a1b2c3"))



##def find(li,tar):
##    n=len(li)
##    find=True
##    i=0
##    j=n-1
##    while find:
##        sum = li[i]+li[j]
##        if sum==tar:
##            return(li[i],li[j])
##
##        elif sum>tar:
##            j-=1
##        else :
##            i+=1
##
##li=[10,20,35,50,75,80,85]
##tar=int(input("enter targer: "))
##
##print(find(li,tar))
##    

##li=[5,2,-1,6,-2,7,3]
##n=len(li)
##i=0
##maxi=0
##
##for i in range(n-2):    
##    
##    if li[i]+li[i+1]+li[i+2]>maxi:
##        maxi=li[i]+li[i+1]+li[i+2]
##    
##    
##print(maxi)    


import re

print(re.findall("\w*\s?", "Order 123, item 45"))


