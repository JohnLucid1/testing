

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def minus_num(self):
        return self.num1 - self.num2

    def plus_num(self):
        return self.num1 + self.num2

    def multiply_by_num(self):
        return self.num1 * self.num2

    def divide_by_num(self):
        if self.num2 == 0:
            return "cant devide by 0"
        return self.num1 / self.num2

    def to_number_power(self):
        return self.num1 ** self.num2

    def get_remainder(self):
        return self.num1 % self.num2
