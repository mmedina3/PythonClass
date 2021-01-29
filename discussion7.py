def main():
    s = int(input("Insert a number "))

    for i in range(s+1): 
        print(i, "x {} is".format(s), i*s)

main()

total = 0 
anum = 0 
while anum <= 100: 
     total = total + anum 
     anum = anum +1

     print (anum)

for i in range(0,10):
     print(i)



def foo(n1,n2):
    while n1 > n2:
        return -1
    else:
        for i in range(n1+1, n2):
            print(i**i)

def main():
     num1 = int(input("Insert first num"))
     num2 = int(input("Insert first num"))

     if (num1 or num2) == 0:
         print("Error Message")

     else:
        print(foo(num1, num2))
main()