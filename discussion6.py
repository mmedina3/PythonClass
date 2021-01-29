
def main():
    eggs: 0

    eggs = int(input("How many eggs do you want? "))

    while eggs > 12:
        print("Can only select up to a dozen")
        return False
        
    else:
        price = eggs * .15
        print("Price for eggs is {}".format(price))

main()



eggs: 0

eggs = int(input("How many eggs do you want? "))

while eggs > 12:
    print("Can only select up to a dozen")
    break
        
else:
    price = eggs * .15
    print("Price for eggs is {}".format(price))

