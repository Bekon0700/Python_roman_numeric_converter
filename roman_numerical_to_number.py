class NumericalConverter:
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def converter(self, st):
        value = 0
        for i in range(len(st)):
            if i > 0 and NumericalConverter.rom_val[st[i]] > NumericalConverter.rom_val[st[i-1]]:
                value += abs(NumericalConverter.rom_val[st[i]] - NumericalConverter.rom_val[st[i - 1]]) -\
                         NumericalConverter.rom_val[st[i-1]]
                print(abs(NumericalConverter.rom_val[st[i]] - NumericalConverter.rom_val[st[i - 1]]) - NumericalConverter.rom_val[st[i-1]])
            else:
                value += NumericalConverter.rom_val[st[i]]
                print(NumericalConverter.rom_val[st[i]])
        print(value)


c = NumericalConverter()
num = input('Enter a Roman numerical: ')
c.converter(num)
