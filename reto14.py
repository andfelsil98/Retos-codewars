# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(n):

    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while (a <= n):
            n = n - a
            roman = roman + dic[a]
    return roman


if __name__ == '__main__':
    resultado = solution(9)
    print(resultado)