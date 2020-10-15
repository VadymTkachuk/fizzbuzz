#!/usr/bin/python
# -*- coding: utf-8 -*-
# FizzBuzz is a simple program that prints "fizz" when a number
# is divisible by three and "buzz" if a number is divisible by five 
# and "fizzbuzz" when two conditions are met.

def main():

    print("\nFizzBuzz is a simple program that prints \"fizz\"" + 
          "when a number is divisible by three and \"buzz\"" + 
          "if a number is divisible by five and \"fizzbuzz\"" +
          "when two conditions are met.\n")

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
