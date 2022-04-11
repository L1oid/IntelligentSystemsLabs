class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __call__(self, x):
        s = 0
        for i in range(len(self.coef)):
            s += self.coef[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        k = Polynomial(st)
        if len(self.coef) < len(other.coef):
            m = len(self.coef)
        else:
            m = len(other.coef)
        for i in range(m):
            st.append(self.coef[i] + other.coef[i])
        if len(self.coef) > m:
            st += self.coef[m::]
        else:
            st += other.coef[m::]
        k.coef = st
        return k


poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()