#! /usr/bin/python3

# file: autori.py
# name: Michelle Bi
# ut eid: mjb6496
# date: 1 feb 2024
import sys

def main():
    str = input()
    new = str[0]
    for i in range(len(str)):
        if str[i] == ' ' or str[i] == '-':
            new += str[i+1]
    print(new) 
    
    

if __name__ == "__main__":
    main()
