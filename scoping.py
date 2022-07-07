var = 3
def out():
    
    def inn():
        var=1
        print(var)
        
    
    global var
    var=16
    inn()
    print(var)
def honest(a):
    if a==0: 
        return True
    else:
        a=odd(a-1)
        return a
def odd(a):
    if a==0:
        return False
    else:
        a=honest(a-1)
        return a
def main():
    print(var)
    out()
    print (var)
    a=input("Enter number (noy very big): ")
    a=honest(int(a))
    if a==True:
        print("Number is honest")
    else:
        print("Number is odd")
main()
