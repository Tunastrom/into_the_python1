import random


def generate_numbers(len_int):
    generate_numbers = set()
    numbers_len = 0
    while numbers_len < len_int:
        generate_numbers.add(random.randint(1, 45))
        numbers_len = len(generate_numbers)
    return list(generate_numbers)


def draw_winning_numbers(normal_len):
    return generate_numbers(normal_len + 1)


def count_matching_numbers(list_1, list_2):
    matcing_numbers = []
    for num_f in list_1:
        for num_s in list_2:
            if num_f == num_s:
                matcing_numbers.append(num_f)
    return len(matcing_numbers), matcing_numbers


def check(numbers, winning_numbers):
    rank = 0
    reword = 0
    counts, matching_numbers = count_matching_numbers(numbers, winning_numbers)
    # print(f'counts: {counts}\nmatching_numbers: {matching_numbers}')
    # print(f'bonnus_number: {winning_numbers[6]}')
    if winning_numbers[6] not in matching_numbers:
        if counts == 3:
            rank = 5
        elif counts == 4:
            rank = 4
        elif counts == 5:
            rank = 3
        elif counts == 6:
            rank = 1
    elif winning_numbers[6] in matching_numbers:
        if counts == 6:
            rank = 2
    return rank

