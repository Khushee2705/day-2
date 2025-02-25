L=[]
def signup():
    email=input("Enter your email:")
    password=input("Enter your password:")
    a={"Email:":email,"Password:":password}
    L.append(a)
    print("Signup successful.")
    print(L)
    return

def check():
        em=input("Enter your email:")
        p=input("Enter your password:")
        for i in range (len(L)):
            if(L[i]['Email:'] != em):
                print("Email is not registered, please signup first.")
                return
            else:
                if(L[i]['Password:']!=p):
                    print("Incorrect password.")
                    return
                else:
                    print("Log in successful")
                    return
           
def main():
    while True:
       c=str(input("Do you want to SignUp? (Yes/No):"))
       if(c.lower()=="yes"):
          signup()
       d=str(input("Do you want to SignIn?(Yes/No):"))
       if(d.lower()=="yes"):
          check()

if __name__=="__main__":
    main()