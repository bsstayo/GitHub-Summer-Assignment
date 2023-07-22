import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'
print('로또 당첨번호를 알려드립니다!\n 궁금하신 회차를 적어주세요\n q를 입력하시면 프로그램이 종료됩니다.\n')

while True:
    number_of_times = input('궁금하신 회차: ')
    
    if number_of_times=="q":
        break
    lotto_nums = []
    
    # 여기에 api로 받아오는 것 완성해주세요!###########
    
    #################################################
    
    for idx, number in enumerate(lotto_nums):
        print(f"번호 {idx} :", number )
    