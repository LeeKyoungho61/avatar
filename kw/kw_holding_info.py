# -*- coding: utf-8 -*-
# kw_holding_info.py
"""
아바타계좌의 정보를 읽는다
"""


class Avatar:
    def __init__(self, name, shares, price, purchase_price, profit, profit_rate):
        self.name = name
        self.shares = shares
        self.price = price
        self.purchase_price = purchase_price
        self.profit = profit
        self.profit_rate = profit_rate


def holding_info(계좌번호, 티커):
    my_avatar_dict = {'코드': 'SOXL',
                      '보유량': 2206,
                      '현재가': 11.1100,
                      '매입가': 17.9728,
                      '평가수익률': '-38.29%',
                      '평가손익': -15184.2859
                      }
    return my_avatar_dict


if __name__ == '__main__':
    my_avatar = holding_info('avatar1', 'SOXL')
    print(my_avatar)
    print(my_avatar['코드'])

    clas_avatar = Avatar('avatar1', 'SOXL')
