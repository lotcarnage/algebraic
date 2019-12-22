class Algebraic:
    class Integer:
        def __init__(self, v):
            if type(v) == self.__class__:
                self.v = v.v
            elif type(v) == int:
                self.v = v
            else:
                raise "Integer Type Error"
            self.p = Algebraic
        def __str__(self):
            return f"{self.v}"
        def Reciprocal(self):
            if self.v == 1:
                return self.__class__(1)
            elif self.v == 0:
                raise "Undefined Zero's reciprocal"
            else:
                return self.p.Rational(1, self.v)
        def __add__(self, operand):
            if type(operand) == self.__class__:
                return self.__class__(self.v + operand.v)
            elif type(operand) == int:
                return self.__class__(self.v + operand)
            else:
                return operand + self.v
        def __mul__(self, operand):
            if type(operand) == self.__class__:
                return self.__class__(self.v * operand.v)
            elif type(operand) == int:
                return self.__class__(self.v * operand)
            else:
                return operand * self.v
        def __sub__(self, operand):
            if type(operand) == int:
                return self + (self.__class__(-1) * operand)
            return self + (operand * self.__class__(-1))
        def __truediv__(self, denominator):
            if type(denominator) == int:
                denominator = self.__class__(denominator)
            return denominator.Reciprocal() * self
        def __radd__(self, operand):
            return self + operand
        def __rmul__(self, operand):
            return self * operand
        def __rsub__(self, operand):
            return self * (-1) + operand
        def __rtruediv__(self, numerator):
            if type(numerator) == int:
                numerator = self.__class__(numerator)
            return numerator / self

    class Rational:
        def __init__(self, numerator, denominator=1):
            if denominator == 0:
                raise "Zero div"
            self.numerator = numerator
            self.denominator = denominator
            self.p = Algebraic
        def __str__(self):
            if self.denominator == 1:
                return f"{self.numerator}"
            else:
                return f"({self.numerator}/{self.denominator})"
        def Reciprocal(self):
            return self.__class__(self.denominator, self.numerator)
        def __add__(self, operand):
            if type(operand) == self.__class__:
                numerator = self.numerator * operand.denominator + \
                            operand.numerator * self.denominator
                denominator = self.denominator * operand.denominator
                return self.__class__(numerator, denominator)
            return self + self.__class__(operand)
        def __mul__(self, operand):
            if type(operand) == self.__class__:
                numerator = self.numerator * operand.numerator
                denominator = self.denominator * operand.denominator
                return self.__class__(numerator, denominator)
            return self.__class__(operand) * self
        def __sub__(self, operand):
            return self + (operand * self.p.Integer(-1))
        def __truediv__(self, denominator):
            return denominator.Reciprocal() * self
    def __init__(self, v):
        self.v = self.__class__.Integer(v)
    def __str__(self):
        return f"{self.v}"
    def __add__(self, v):
        return self.__class__(self.v + v)
    def __mul__(self, v):
        return self.__class__(self.v * v)
    def __sub__(self, v):
        return self.__class__(self.v - v)
    def __truediv__(self, v):
        return self.__class__(self.v / v)

AI = Algebraic.Integer
AR = Algebraic.Rational

if __name__ == "__main__":
    a = AI(2)
    b = AR(3, 4)
    c = AI(4)
    print(f"a={a}")
    print(f"b={b}")
    print(f"a + b = {a+b}")
    print(f"a - b = {a-b}")
    print(f"a * b = {a*b}")
    print(f"a / b = {a/b}")
    print(f"a + 2 = {a+2}")
    print(f"a - 2 = {a-2}")
    print(f"a * 2 = {a*2}")
    print(f"a / 2 = {a/2}")
    print(f"b + a = {b+a}")
    print(f"b - a = {b-a}")
    print(f"b * a = {b*a}")
    print(f"b / a = {b/a}")
    print(f"2 + a = {2+a}")
    print(f"2 - a = {2-a}")
    print(f"2 * a = {2*a}")
    print(f"2 / a = {2/a}")
    exit()
