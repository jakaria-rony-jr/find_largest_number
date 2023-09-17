def find_largest_number(a, b, c):
    if a==b==c:
        print('Three Number is Equal')
    elif a >= b and b >= c:
        return a
    elif b >= c and b >= c:
        return b
    else:
        return c
num1 = float(input("a: "))
num2 = float(input("b: "))
num3 = float(input("c: "))

largest_num = find_largest_number(num1, num2, num3)
print("big number", largest_num)





