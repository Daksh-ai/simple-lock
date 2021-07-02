class lock:
    def login(self):
        print("you have account press [Y/N]:")
        self.a=input()
        if self.a=="Y":
            self.username=input("Enter the username")
            self.password=input("Enter the password")
            return "Lock active"
        if self.a=="N":
            return q.signin()
        
        
    def signin(self):
        li=[input("Enter the username:"),input("Enter the password:")]
        f=open("code1.txt","w")
        s1="\n".join(li)
        f.write(s1)
        return "Your Account Active Now!"
        f.close()
        
        
        
        
            
            


if __name__ == '__main__':
    n=int(input("1:login\n2:signup"))
    q=lock()
    if n==1:
        print(q.login())
    elif n==2:
        print(q.signin())
        
    
    

