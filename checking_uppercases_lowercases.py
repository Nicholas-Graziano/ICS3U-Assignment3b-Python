#!/usr/bin/env python3
# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number


def main():
    # this program checks if a letter is uppercase or lowercase

    # input
    letter = input("Enter a Letter :")
    # process
    if(letter.isupper()):
        print("uppercase")

    elif(letter.islower()):
        print("lowercase")
    else:
        print("Not a letter")


if __name__ == "__main__":
    main()
