def triangle(a_p, b_p, c_p):
    if a_p + b_p > c_p and a_p + c_p > b_p and b_p + c_p > a_p:
        return "Это треугольник"
    else:
        return "Это не треугольник"
a = float(input())
b = float(input())
c = float(input())
print(triangle(a, b, c))
