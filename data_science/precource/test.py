class SoccerPlayer(object):
    def __init__(self, name : str, position : str, back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return f'Hello, My name is {self.name},. I play in {self.position} in center'

    def __add__(self, other):
        return self.name + other.name

    def change_back_number(self, new_number):
        print('선수의 등번호를 변경합니다 : From %d to %d' %(self.back_number, new_number))
        self.back_number = new_number

Ji = SoccerPlayer('Ji', 'ST', 1)
Sangryeol = SoccerPlayer('Sangryeol ', 'ST', 1)

print(sangryeol.back_number)
sangryeol .change_back_number(11)
print(sangryeol.back_number)
print(sangryeol)