# d = ""

def dog(d):
    if d == "Y" or "y":
        dogsays = str("woof")
        return dogsays;
    else:
        nodog = str("too bad")
        return nodog;
def main():
 q=input("Do you have a dog Y/N? ")
 print(dog(q))

main()

