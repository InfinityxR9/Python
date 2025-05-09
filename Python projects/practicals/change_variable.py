# To change the value of the existing variable, *All in a function* Not even a single line of code in the main file

def change_variable(a):
    global x
    x = a
    x *= 30

# To take the value of the variable from the user and multiply the variable by 30, but only in the function, not in the main file. And there is a catch, You have to change the value of the variable

x = int(input("Enter a number: "))
print("Before change:", x)
change_variable(x)
print("After change:", x)
