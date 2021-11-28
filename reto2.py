def high_and_low(numbers):
    result = []
    numbers = list(map(int,numbers.split()))
    result.append(str(max(numbers)))
    result.append(str(min(numbers)))
    answer = " ".join(result)
    return print("'" + answer + "'")



if __name__ == '__main__':

    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"  