from itertools import permutations


def solution(numbers):
    answer, all_combies, answer_list, first_numbers = '', list(), list(), set()

    # numbers의 각 정수들 문자열 변환하고 내림차순 정렬해 numbers_str에 할당
    numbers_str = sorted(map(str, numbers), reverse=True)

    # 첫째자리 수 종류 구하여 first_numbers에 담기
    for number in numbers_str:
        first_numbers.add(number[0])

    # 첫째자리 수 종류 내림차순 정렬
    first_num_list = list(first_numbers)
    first_num_list.sort(reverse=True)
    print(first_num_list)

    # 0만 들어간 경우 처리
    if len(first_num_list) == 1 and first_num_list[0] == '0':
        answer = '0'
        return answer

    # 첫째자리수 내림차순으로 하나씩 반복
    for first_num in first_num_list:
        number_group = []
        # '0'을 answer에 모두 추가
        if first_num == '0':
            answer = 'here'
            for number in numbers_str:
                answer += number
            break
        # 각 첫째자리수 별로 숫자들 그룹화 및 그룹에 할당된 수들 numbers_str에서 제거
        for number in numbers_str[:]:
            if number[0] == first_num:
                number_group.append(number)
                numbers_str.pop(numbers_str.index(number))
        # 그룹 내에서 모든 경우의 수 구하고 가장 큰 수 탐색 한 뒤 answer_list에 추가
        max_g_num = 0
        for g_num in list(permutations(number_group, len(number_group))):
            g_num = int(''.join(list(map(str, list(g_num)))))
            if max_g_num != 0 and max_g_num < g_num:
                max_g_num = g_num
            elif max_g_num == 0:
                max_g_num = g_num
        answer_list.append(max_g_num)

    # 0이 추가 되어있을 때에 0 앞에 추가되도록 함.
    result = ''.join(list(map(str, answer_list)))
    if answer == '':
        answer = result
    elif answer.find('here') != -1:
        answer = answer.replace('here', result)

    return answer