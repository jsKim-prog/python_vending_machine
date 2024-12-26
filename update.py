# pay.main() -> return guest_log
# pay.main()이 반환한 고객의 매출 정보를 이용하여 일 매출과 재고 정보를 갱신
# day_sale : [{"card":0,"cash":0, 상품번호:0}]
def main(goods, guest_log, day_sale) :
    guest_dic = guest_log["판매"] # {'판매':{s_num:buy_count}}
    guest_dic_keys = list(guest_dic.keys()) # = [1, 8 ..] 선택한 상품번호

    for i in list(day_sale.keys()):     ## 일 매출
        if i not in guest_dic_keys :    # 사용자가 선택한 상품이 아니면 skip
            continue
        day_sale[i] = guest_dic[i] * goods[i]["가격"]         # guest_dic[i] :buy_count
        goods[i]["재고"] = goods[i]["재고"] - guest_dic[i]    # 재고수량 감소

    # 금액 부분 업데이트
    if guest_log["결제"] == 'cash':
        day_sale["cash"] = day_sale["cash"] + guest_log["판매금액"]
    elif guest_log["결제"] == 'card':
        day_sale["card"] = day_sale["card"] + guest_log["판매금액"]
