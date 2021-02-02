"""
Created on 01/31/21

Program to Assignment #8

@author: Michelle Medina
"""

#Write a function named cipher that takes a string. 
# The function returns that string in a ciphered form by using the ord of the first letter of the string to cipher each letter including the first letter. 
def cipher(s):
    c_string = ""
    for letter in s:
        c_string += chr(ord(s[0]) + ord(letter))
        return c_string


#Write another function to decipher (do the opposite of the previous function), given a string and returns the deciphered string.
def deciphered(s):
    d_string = ""
    for letter in s:
        d_string += ord(letter) - ord(int(s[0])/2)
        return d_string

def main():
    string = input("Insert a word: ")
    print(cipher(string))
    print(deciphered(string))

main()