def main():
    n=input("Enter your number ")
    if "b" in n:
        n=int(n, base = 0)
        print(" Dec =", n)
        print(" Oct =", oct(n))
        print(" Hex =", hex(n))
    elif "o" in n:
        n=int(n, base = 0)
        print(" Dec =", n)
        print(" Bin =", bin(n))
        print(" Hex =", hex(n))
    elif "x" in n:
        n=int(n, base = 0)
        print(" Dec =", n)
        print(" Bin =", bin(n))
        print(" Oct =", oct(n))
    else:
        n=int(n)
        print(" Bin =", bin(n))
        print(" Oct =", oct(n))
        print(" Hex =", hex(n))
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    c=input("Enter third number: ")
    a=int(a)
    b=int(b)
    c=int(c)
    print("Min =",min(a,b,c))
    print("Max =",max(a,b,c))
main()