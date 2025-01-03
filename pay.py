import datetime as t #날짜관리 위한 라이브러리 호출
from common import LINES

#고객 성별 선택
def choice_gender(guest_log) :
    print(LINES)
    gender = input("\n성별 입력\n1. 남자/2. 여자 : ")
    print(LINES, end="\n")
    if gender == '1' :
        guest_log["gender"] = 'man'
    elif gender == '2' :
        guest_log["gender"] = 'woman'
    else:
        return True
    return False

#고객 연령대 선택
def choice_age(guest_log) :
    print(LINES)
    print("\n나이 입력\n0. 10대 이전\n1. 10대\n2. 20대\n3. 30대\n4. 40대\n5. 50대\n6. 60대\n7. 60대 이상")
    print(LINES, end="\n")
    age = input("선택 : ")
    print() # 한줄 띄우기
    if age == '0':
        guest_log['age'] = 0
    elif age == '1':
        guest_log['age'] = 10
    elif age == '2':
        guest_log['age'] = 20
    elif age == '3':
        guest_log['age'] = 30
    elif age == '4':
        guest_log['age'] = 40
    elif age == '5':
        guest_log['age'] = 50
    elif age == '6':
        guest_log['age'] = 60
    elif age == '7':
        guest_log['age'] = 70
    else:
        return True
    return False

# 상품 선택
# 물건 목록을 띄우고 그 중에서 어떤 물건을 구매할지 선택
# 물건의 수량 정보까지 취합하여 저장
# 구매 물건으로 로또를 선택했을 경우 lotto.main() 호출
#goods : from main.py -> {1: {tmp_dic}, 2:{tmp_dic}...}
def select_goods(tmp, goods) :
    tmp_list = list(goods.keys()) # = [1,2,...] 상품번호 리스트
    buy_count = 0 # 선택수량 넣을 변수 -> while, if문 사용으로 미리 선언
    s_num = 0  # 사용자가 입력한 번호 담을 변수
    print(LINES)
    for i in tmp_list:
        print("\n{}.\t{}\t/\t금액\t:\t{}".format(i,goods[i]['품목'], goods[i]['가격'])) # 1.      진라면  /       금액    :       800
    print(LINES, end="\n")

    while True: #사용자가 입력한 번호가 상품리스트에 있는 번호일 때까지 반복
        s_num = input("\n구매상품 번호 : ")
        if s_num in goods :
            break

    while True:
        try:
            buy_count = int(input("\n구매 상품 수량 : "))
            break
        except TypeError:
            continue
    #10개 입력시 로또 실행

    while True:
        print(LINES)
        print("제품 : {} / 수량 : {}".format(goods[s_num]['품목'], buy_count))
        print(LINES, end="\n")
        num = input("1. 확인 / 2.취소 : ")
        print(LINES, end="\n")
        if num == '1' :
            tmp[s_num] = buy_count # {'판매':{s_num:buy_count}}
            return False    # 제품선택 while 종료
        elif num == '2' :
            return True     # line 50으로

# 구매하고자 하는 물건의 종류와 수량을 선택하는 흐름 제어
def flow_choice(guest_log, goods) :
    boolean = True
    # service = 0
    tmp_goods = guest_log['판매'] # {'판매':{}}

    while boolean :
        boolean = select_goods(tmp_goods, goods)

    guest_log['판매'] = tmp_goods

    while True:
        print(LINES)
        end_flag = input("1. 다음 / 2. 다른 물품 선택 : ")
        print(LINES, end="\n")

        if end_flag == '1':
            return False
        elif end_flag == '2' :
            return True

# 결제 흐름
# 영수증 출력을 위하여 구매한 물건의 수량과 합계금액 정보를 저장
def cal_cost(tmp_dic, goods) :
    total = 0
    tmp_list = list(tmp_dic.keys()) #[1,2,...]
    sale_dic = {}
    sel_count = 0
    for i in tmp_list :
        tmp = {}
        sel_count += 1
        sel_t = goods[i]['가격'] * tmp_dic[i] #선택 물품 총금액
        total += sel_t
        tmp["품목"] = goods[i]["품목"]
        tmp["수량"] = tmp_dic[i]
        tmp["총금액"] = sel_t
        sale_dic[sel_count] = tmp
    return  sale_dic, total

# 결제 방법 선택
def select_payment():
    print(LINES)
    payment = input("1. 카드 / 2. 현금 : ")
    print(LINES, end="\n")
    tmp = 0

    if payment == '1' :
        tmp=1
    elif payment == '2':
        tmp = 2
    else:
        return True, tmp
    return False, tmp

# 결제 방법 중 카드 결제 관련 흐름 제어(영수증 출력)
def select_card(sale_dic, total, guest_log) :
    print()
    print()
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]["품목"],sale_dic[i]["수량"],sale_dic[i]["총금액"]))
    print()
    print(LINES, end="\n")

    print("\ntotal : {}".format(total))

    print(LINES, end="\n")

    tmp = input("1. 확인 / 2. 취소 : ")

    print(LINES, end="\n")

    if tmp == '1':
        print("결제 완료")
        print("=" * 15)
        guest_log["결제"] = "card"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = None
        return False
    elif tmp == '2':
        print("결제 취소")
        print("=" * 15)
        return True
    else:
        print("다시 입력하세요.")
        return True

# 결제 방법 중 현금 결제 관련 흐름 제어
def select_cash(sale_dic, total, guest_log) :
    print()
    print()
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['품목'], sale_dic[i]['수량'], sale_dic[i]['총금액']))

    print()
    print(LINES, end="\n")
    print("Total : {}".format(total))
    print(LINES, end="\n")
    tmp = 0 #변수 유효범위!
    while True:
        try:    # 숫자입력 유도
            tmp = int(input("\n받은 현금 : "))
            break
        except TypeError:
            print("숫자를 입력하세요.")
            continue
    # 받은 돈 계산
    if tmp - total < 0:
        print(LINES, end="\n")
        print("받은 현금이 부족합니다.")
        print(LINES, end="\n")
        return True
    else:
        print(LINES, end="\n")
        print("\n결제 완료")
        print(LINES, end="\n")
        print("잔돈 : {}원".format(tmp - total))
        print(LINES, end="\n")
        guest_log["결제"] = "cash"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = tmp - total
        return False

# 물건 구매 후에 결재 관련된 모든 흐름 제어
def flow_payment(guest_log, goods) :
    boolean = True
    select_num = 0
    tmp_goods = guest_log['판매'] #{'판매':{}}
    sale_dic, total = cal_cost(tmp_goods, goods) # return sale_dic, total

    while boolean:
        boolean, select_num = select_payment() # 결제방법 선택(1. 카드 / 2. 현금) -> return False, tmp
    boolean = True
    if select_num == 1 :
        while boolean :
            boolean = select_card(sale_dic, total, guest_log)
    elif select_num == 2 :
        while boolean :
            boolean = select_cash(sale_dic, total, guest_log)
    return False


# 메인메뉴
def main(goods) :
    now = t.datetime.now()
    guest_log = {'판매':{}}
    print(LINES)
    print("Today : {}/{}/{} {}:{}".format(now.year, now.month, now.day, now.hour, now.minute))
    print(LINES, end="\n")
    # 고객 성별 선택
    while choice_gender(guest_log):
       print("\n다시 입력하세요.")
    # 고객 연령대 선택
    while choice_age(guest_log):
        print("\n다시 입력하세요.")
    # 상품 선택
    while flow_choice(guest_log, goods):
        continue
    # 결제 흐름
    while flow_payment(guest_log, goods):
        continue

    # 날짜, 시간정보 정리
    now_time = "{}-{}-{}/{}:{}".format(now.year, now.month, now.day, now.hour, now.minute)
    guest_log["일시"] = now_time
    print(LINES, end="\n")
    print()
    return guest_log

# ** guest_log -> 사용자정보 파일로 저장 추가 (예정)
# **  현금계산시 적은 돈 입금시 누적 계산 적용(예정)