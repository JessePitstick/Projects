def main():
    happy_numbers = []
    unhappy_numbers = []
    i = 1
    while len(happy_numbers) < 8:
        if isHappy(i): happy_numbers.append(i)
        i += 1
    print happy_numbers

def isHappy(i, unhappy_numbers=None, happy_numbers=None):
    numbers_so_far = set() #this set helps prevent infinite loops
    while i != 1 and i not in numbers_so_far:
        numbers_so_far.add(i)
        i = sum_of_digits_squared(i)
    return i == 1

def sum_of_digits_squared(i):
    sum = 0
    for digit in str(i):
        sum += int(digit) * int(digit)
    return sum


if __name__ == '__main__':
    main()
