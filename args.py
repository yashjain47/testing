def multiply(a, b, *argv):
    mul = a * b
    for num in argv:
        mul *= num
    return mul


# a = multiply(1, 2, 3, 4, 5)
# print(a)

def tellArguments(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)


tellArguments(arg1="argument 1", arg2="argument 2", arg3="argument 3")

