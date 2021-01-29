#Function will convert Miles to Kilometers. 

#print the kilometer conversion
def print_k(k):
    print("The amount of kilometers that you ran is: ", k)

#convert the miles value to kilometers
def convert_m(m):
    kilometers= m * 1.609
    print_k(kilometers)

#grab the amount of miles ran
def main():
    miles:0
    miles= int(input("How many miles did you run?: "))
    convert_m(miles)

main()




#print the celsius conversion
def print_celsius(c):
    print("The conversion to celsius is: ", c)

#convert the fahrenheit value to celsius
def convert_f(f):
    celsius= (f - 32) * 5/9
    print_celsius(celsius)

#grab the current fahrenheit
def main():
    fahrenheit:0
    fahrenheit= int(input("What is the weather in fahrenheit today?: "))
    convert_f(fahrenheit)

main()