class Mathematician:
    def __init__(self, numbers, year):
        self.numbers = numbers
        self.year = year

    def square_nums(self):
        square_numbers = []
        result = 0
        for i in self.numbers:
            result = i**2
            square_numbers.append(result)
        return square_numbers

    def remove_positives(self):
        positive_numbers = []
        for i in self.numbers:
            if i > 0:
                positive_numbers.append(i)
        return positive_numbers

    def filter_leaps(self):
        leap_years = []
        for i in self.year:
            if i % 4:
                leap_years.append(i)
        return leap_years


m = Mathematician(numbers = [7, 11, 5, 4, -1], year = [2000, 2001, 2002, 2003, 2004])

print(m.square_nums())
print(m.remove_positives())
print(m.filter_leaps())

