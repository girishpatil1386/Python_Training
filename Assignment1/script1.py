#!/usr/bin/python3
lst = []
tpl = ()

print("Enter comma separated number: ")
numbers = input().split(',')

lst.append(numbers)
tpl = tuple(numbers)

print("The List: " , lst)
print("The Tuple: ", tpl)
