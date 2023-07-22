import requests
from src import get_api, extract_number as en


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'
print('로또 당첨번호를 알려드립니다!\n 궁금하신 회차를 적어주세요\n q를 입력하시면 프로그램이 종료됩니다.\n')

while True:
    number_of_times = input('궁금하신 회차: ')
    
    if number_of_times == "q":
        break
    lotto_nums = []
    
    # 여기에 api로 받아오는 것 완성해주세요!###########
    results = get_api.get_url_results(url, number_of_times)

    returnValue = results.get('returnValue', None)
    if returnValue == 'fail':  # check validation
        print("정보를 가져오는데 실패했습니다.\n회차 번호를 다시 확인해주세요.\n")
    else:
        lotto_date = results.get('drwNoDate', None)
        lotto_nums = en.extract_number(results)
    
    #################################################
        for idx, number in enumerate(lotto_nums, start=1):
            if idx == 7:
                print("보너스 번호 : ", number, "\n")
            else:
                print(f"번호 {idx} :", number)
    