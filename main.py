# 클래스 연결
import ep # 일매출 관리(파일관리)
import gmanagement #재고관리
import management #월매출 관리(파일관리)
import pay  #고객정보받기, 상품리스트 보여주기, 구매과정(결제)
import update #일매출, 재고정보 갱신
from common import LINES

#재고 및 물품 정보를 텍스트 파일에서 읽기
# goods , day_sale 딕셔너리 생성
f = open("stock/goods.txt", 'r')
goods = {}  # 물품 정보 및 재고 저장
day_sale = {"card":0,"cash":0}  # 일 매출 정보 저장

# goods.txt : key 정의
while True:
    tmp_dic = {}
    line = f.readline()
    line = line.rstrip("\n") # 파일에서 읽어와서 우측 엔터 지우고 다시 저장
    if line == "": # 빈줄이면 멈추기
        break
    st_list = line.split("/")
    tmp_dic["분류"] = st_list[1]
    tmp_dic["품목"] = st_list[2]
    tmp_dic["가격"] = int(st_list[3])
    tmp_dic["재고"] = int(st_list[4])

    goods[st_list[0]] = tmp_dic #goods
    day_sale[st_list[0]] = 0    #{"card":0,"cash":0, 1:0}

# menu 불러오기
while True:
    print(LINES)
    print("1. 판매시작 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print(LINES, end="\n")
    select_num = input('선택 : ')

    # 판매 및 재고, 일매출 정리
    if select_num == '1':
        tmp = pay.main(goods)   #return guest_log
        #pay결과 받아 update
        update.main(goods, tmp, day_sale)
    elif select_num == '2': # 재고 및 발주 관리
        gmanagement.main(goods)
    elif select_num == '3': # 일매출 및 월매출 확인
        management.main(goods, day_sale)
    elif select_num == '9' : # 프로그램 종료 전에 메모리에 있는 정보를 텍스트 파일로 저장
        ep.main(goods, day_sale)
        break
    else:
        print("다시 선택 하세요\n")