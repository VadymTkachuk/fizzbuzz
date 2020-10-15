#!/usr/bin/python
# -*- coding: utf-8 -*-
# FizzBuzz is a simple program that prints fizz when a number
# is divisible by three with the word "fizz"
# and any number divisible by five with the word "buzz" 
# and "fizzbuzz" when two conditions are met.

def main():

    print("FizzBuzz is a simple program that prints fizz when a number\n" +
          "is divisible by three with the word 'fizz'\n" +
          "and any number divisible by five with the word 'buzz'\n" +
          "and 'fizzbuzz' when two conditions are met.\n")

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 5 == 0:
            print("buzz")
        elif number % 3 == 0:
            print("fizz")
        else:
            print(number)

if __name__ == "__main__":
    main()
