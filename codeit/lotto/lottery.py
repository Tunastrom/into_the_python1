from random import randint


def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    generate_numbers = set()
    numbers_len = 0
    while numbers_len < n:
        generate_numbers.add(randint(1, 45))
        numbers_len = len(generate_numbers)
    return list(generate_numbers)


def draw_winning_numbers():
    # 코드를 작성하세요.
    generate_nums = generate_numbers(7)
    winning_numbers = sorted(generate_nums[0:6])
    bonus_num = generate_nums[6]
    winning_numbers.append(bonus_num)
    return winning_numbers


def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    matcing_numbers = []
    for num_f in numbers:
        for num_s in winning_numbers:
            if num_f == num_s:
                matcing_numbers.append(num_f)
    return len(matcing_numbers)


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    normal_count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if normal_count < 3:
        return 0
    elif normal_count == 3:
        return 5000
    elif normal_count == 4:
        return 500000
    elif normal_count == 5 and bonus_count == 1:
        return 50000000
    elif normal_count == 5:
        return 1000000
    elif normal_count == 6:
        return 100000000
