class Complex:
    def __init__(self, a, b):
        self.__real = a
        self.__imag = b

    def print(self):
        print(self.__real, "+", self.__imag, "i")

    def __add__(self, other):
        result = Complex(self.__real+other.__real, self.__imag+other.__imag)
        return result

def main():
    c1 = Complex(5, 10)
    c2 = Complex(2,3)
    c3 = c1 + c2
    c1.print()
    c2.print()
    c3.print()
    c4 = c1.__add__(c2)
    c4.print()



main()