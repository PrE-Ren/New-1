while(1):
    print("Give me number")
    a = int(input())
    print("Give me one more!")
    b = int(input())
    if a==0 and b==0:
        break
    print("a+b:")
    print(a+b)
    print("a-b:")
    print(a-b)
    print("a*b:")
    print(a*b)
    if b==0:
        print("Can't divide in 0!")
    else:
        print("a/b:")
        print(a/b)
        print("a%b:")
        print(a%b)
    print("a**b")
    print(a**b)
	

