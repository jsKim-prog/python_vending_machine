import datetime as t
from common import LINES


# 월 매출을 파일에서 읽어와서 딕셔너리 형태로 저장한 다음 반환
def month_margin(month):
    f = open("mng/" + month + "_total.txt", "r")
    tmp_mng_dic = {}  # ** 이름변경(tmp_dic은 main 파일 자동 끌어옴)
    tmp_month = {}

    while True:
        line = f.readline()
        if line == '':
            break
        line = line.rstrip("\n")
        tmp_list = line.split("/")
        tmp_month[tmp_list[0]] = int(tmp_list[1])  # {1:11110, 2:3100.. }
    tmp_mng_dic[month] = tmp_month  # {1:{1:11110, 2:3100.. }}
    return tmp_mng_dic


# 받아온 day_sale 딕셔너리를 이용하여 일매출을 화면에 출력
# 월매출 딕셔너리를 반환 받아서 화면에 출력
def main(goods, day_sale):
    today = t.datetime.now()
    month = str(today.month).zfill(2)   # 두자리 숫자로 0채워서 표시
    day = str(today.day).zfill(2)

    while True:
        try:
            print(LINES)
            s_num = int(input("1. 일 매출 / 2. 월 매출 / 5. 종료 : "))
            print(LINES, end="\n")
        except TypeError:
            print("숫자를 입력하세요.")
            continue
        if s_num == 1:  # 일매출 선택시
            print("  일  매  출")
            print(LINES)
            print("Today : {}/{}/{}".format(today.year, month, day))
            print(LINES)
            for i in day_sale.keys():
                if i == 'card' or i == 'cash':
                    continue
                else:
                    print("{}. {} : {}".format(i, goods[i]['품목'], day_sale[i]))
            print(LINES, end="\n")
            print("{} : {}\n{} : {}\n".format('card', day_sale['card'], 'cash', day_sale['cash']))
            print(LINES, end="\n")
            print()
        elif s_num == 2:
            dic = month_margin(month) #return tmp_mng_dic
            tmp_mng_dic = dic[month]
            print("월  매  출")
            print(LINES)
            for i in tmp_mng_dic.keys():
                if i == 'card' or i == 'cash':
                    continue
                else:
                    print("{}. {} : {}".format(i, goods[i]['품목'], tmp_mng_dic[i]))

            print(LINES, end="\n")
            print("{} : {}\n{} : {}\n".format('card', tmp_mng_dic['card'], 'cash', tmp_mng_dic['cash']))
            print(LINES, end="\n")
            print()
        elif s_num == 5:
            break
        else:
            print(LINES)
            print("다시 입력하세요.")
            print(LINES, end="\n")
            print()
