marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("{number} 번 학생 축하합니다. 합격입니다. {marks}점" .format(number=number+1, marks=marks[number]))