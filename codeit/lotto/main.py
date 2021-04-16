from lotto_workers import generate_numbers, draw_winning_numbers, check
import time

def main():
    switch = True
    rank_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
    reword_list = [100000000, 50000000, 1000000, 50000, 5000]
    winning_numbers = draw_winning_numbers(6)
    print(f'winning_numbers: {winning_numbers}')
    while switch:
        numbers = generate_numbers(6)
        # print(f'numbers: {numbers}')
        rank = check(numbers, winning_numbers)
        # if rank == 0:
        #     print('꽝입니다!.. 다시 도전하세요')
        # else:
        #     print(f'축하합니다! {rank}등에 당첨되었습니다! 상금은 {format(reword_list[rank-1],",")}원입니다!')
        rank_dict[rank] += 1
        print(rank_dict)
        if rank_dict[1] > 0:
            trial_count = 0
            for i in range(6):
                trial_count += rank_dict[i]
            rank_0_percent = (rank_dict[0] / trial_count) * 100
            rank_1_percent = (rank_dict[1] / trial_count) * 100
            rank_2_percent = (rank_dict[2] / trial_count) * 100
            rank_3_percent = round((rank_dict[3] / trial_count) * 100, 10)
            rank_4_percent = round((rank_dict[4] / trial_count) * 100, 2)
            rank_5_percent = round((rank_dict[5] / trial_count) * 100, 2)
            print(f'총 실행횟수: {format(trial_count,",")}\n'                                
                  f'1등 당첨확률: {rank_1_percent}%\n'                            
                  f'2등 당첨확률: {rank_2_percent}%\n'                            
                  f'3등 당첨확률: {rank_3_percent}%\n'                            
                  f'4등 당첨확률: {rank_4_percent}%\n'                            
                  f'5등 당첨확률: {rank_5_percent}%\n'                            
                  f'꽝 확률: {rank_0_percent}%\n')
            switch = False

            
if __name__ == '__main__':
    main()























