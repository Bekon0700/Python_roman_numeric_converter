class NumericalConverter:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    def converter(self, number):
        roman_nam = ''
        i = 0
        while number > 0:
            for _ in range(number // NumericalConverter.val[i]):
                roman_nam += NumericalConverter.syb[i]
                number -= NumericalConverter.val[i]
            i += 1
        print(roman_nam)


c = NumericalConverter()
num = int(input('Enter a number: '))
c.converter(num)
