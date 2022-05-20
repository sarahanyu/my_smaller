"""
File: my_smaller.py
Name:
-------------------------
This program implements a my_smaller function
which takes 2 arguments and outputs the
smaller one
"""


def main():
    n1 = int(input('First number: '))
    n2 = int(input('Second number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)


def my_smaller(n1, n2):
    if n1 < n2:
        return n1
    return n2




if __name__ == '__main__':
    main()
