def fizzBuzz(n):
    # Write your code here
  for num in range (1,n +1):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"  
    if num % 5 !=0 and num %3 != 0:
        string = string + str(num)
    print(string)
    
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)