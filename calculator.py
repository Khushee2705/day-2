def add(x,y):
     return x+y
def subtract(x,y):
     return x-y
def multiply(x,y):
     return x*y
def divide(x,y):
     return x/y
def main():
  while True:
     print("select operator:")
     print("1.ADD")
     print("2.SUBTRACT")
     print("3.MULTIPLY")
     print("4.DIVIDE")
     c=int(input("Enter your choice:"))
     a=int(input("Enter number 1:"))
     b=int(input("Enter number 2:"))
     if c==1:
          print(a,"+",b,"=",add(a,b))
     elif c==2:
          print(a,"-",b,"=",subtract(a,b))
     elif c==3:
          print(a,"*",b,"=",multiply(a,b))
     elif c==4:
          print(a,"/",b,"=",divide(a,b))      
     else:
          print("Wrong choice")             
     next=str(input("Do you want to do calculator? (yes/no):"))
     if(next.lower()=="yes"):
          continue
     else:
          break
main()    