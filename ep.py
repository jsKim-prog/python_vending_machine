import management
import datetime as t
import os


# 변경된 재고 정보를 텍스트 파일에 저장
def re_stock(goods) :
    f = open("stock/goods.txt", "w")

    for i in goods.keys():
        f.write("{}/{}/{}/{}/{}\n".format(i,goods[i]['분류'],goods[i]['품목'],goods[i]['가격'],goods[i]['재고']))
    f.close()

# 일 매출 정보를 텍스트 파일에 저장
def make_day_sale(month, day, day_sale) :
    f = open("mng/"+month+day+".txt", "w")
    for i in day_sale.keys() :
        f.write("{}/{}\n".format(i,day_sale[i]))
    f.close()

# 월 매출 정보를 불러와서 일 매출 정보를 더한 다음에 다시 텍스트 파일에 저장
# 추가 : 월 매출 파일이 없으면 생성
def make_month_sale(month, day_sale) :
    month_total_dic = {}    #월 매출 넣을 딕셔너리 준비
    f_dic = {}  #파일 작성할 딕셔너리
    # 해당월 매출 파일 있는지 확인
    if os.path.isfile("mng/"+month+"_total.txt"):
        month_total_dic = management.month_margin(month) # {1:{1:11110, 2:3100.. }}
        month_sale = month_total_dic[month]  # {1:11110, 2:3100.. }
        for i in month_sale.keys():  # i = 1, 2, 3...(상품번호),card, cash
            total = month_sale[i] + day_sale[i]  # day_sale : {"card":0,"cash":0, 1:0} -> 월별 매출에 오늘 매출 더하기
            f_dic[i] = total
    else:   # 파일 없으면 오늘 매출 = 월별 매출
        f_dic = day_sale

    f = open("mng/" + month + "_total.txt", "w")  # 기존 월별 매출 파일 열어서
    for i in f_dic.keys():
        f.write("{}/{}\n".format(i, f_dic[i]))  # 덮어쓰기
    f.close()


#main
def main(goods, day_sale) :
    now = t.datetime.now()
    month = now.month
    day = now.day

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    re_stock(goods) # 변경된 재고 정보를 텍스트 파일에 저장
    make_day_sale(month, day, day_sale) # 일 매출 정보를 텍스트 파일에 저장
    make_month_sale(month, day_sale) # 월 매출 정보를 불러와서 일 매출 정보를 더한 다음에 다시 텍스트 파일에 저장
