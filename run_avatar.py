# -*- coding: utf-8 -*-
# run_avatar.py
"""
실행 파일
"""


import pyautogui as pag
# import cv2
from kw import *
# from kw_window_handling import *
# from kw_hero_excute import *
# from kw_holding_info import *
# from kw_load_my_avatar import *

# 프로그램에서 사용하는 값 설정
pag.PAUSE = 0.1

아바타1 = 4  # 아바타SOXL(6000-6798)


###############################################################################
# 영웅문Global을 실행하고 로그인한다
hero_excute()
# 열려진 모든 창을 닫는다
close_all_window(img_박스_서브윈도우닫기)
# [실시간잔고-2510]창을 연다
open_window(화면번호_실시간잔고)
# [미니주문-2102]창을 연다
open_window(화면번호_미니주문)
# 화면 맨아래의 [실시간잔고]탭을 클릭한다
select_item(img_탭_실시간잔고)
# 계좌번호의 [원하는 계좌]를 선택한다
select_account(아바타1)
# [조회]버튼을 누른다
select_item(img_버튼_실시간잔고조회)
print('준비 완료')
###############################################################################

# 아바타계좌의 [종목] [수량] [현재가]를 OCR로 읽는다 ###########################
holdinfo = holding_info(아바타1, 'SOXL')
# [내 아바타시트 정보]를 로드한다
load_avatar_sheet()
# [종목] 확인
# [현재가]에 대한 [누적수량] 확인
# [매수][매도][대기] 결정
# [매수][매도]의 경우, [미니 주문]

# def mini_order(매수매도, 티커, 종류, 수량, 가격):
# def mini_order(매수매도, 티커, 수량=0, 가격=0):
#     # 1. 매수/매도/정정 선택
#     if 매수매도 == "매수":
#         pag.click(미니주문_매수탭)
#     elif 매수매도 == "매도":
#         pag.click(미니주문_매도탭)
#     elif 매수매도 == "정정":
#         pag.click(미니주문_정정탭)
#     else:
#         raise Exception("매수/매도/정정중에서 한가지를 입력 하세요")
#
#     # 2. 종목 입력
#     pag.sleep(.25)
#     pag.click(미니주문_종목)
#     pag.write(티커, interval=0.1)
#     pag.press("enter")
#
#     # 3. 종류 선택
#
#     # 4. 수량 입력
#     pag.sleep(.25)
#     pag.click(미니주문_수량)
#     pag.write(str(수량))
#     pag.press("enter")
#
#     # 5. 가격 입력 --> 현재가와 비교하여 15% 이내이어야 한다. 아니면 에러 처리
#     pag.sleep(.25)
#     pag.click(미니주문_가격)
#     pag.write(str(가격))
#     pag.press("enter")


# 미니주문
# mini_order("매수", "TQQQ", "지정가", 1, 1.2)
# mini_order("매수", "SOXL", 1, 1.99)

# 매수 종류 : 1=지정가 2=시장가 3=ATFER지정 4=LOC 5=매수VWAP 6=매수TWAP
# 매도 종류 : 1=지정가 2=시장가 3=ATFER지정 4=LOC 5=매도MOC 6=매도VWAP 7=매도TWAP 8=매도STOP 9=매도STOP LIMIT
# 정정 번호 : 정정 또는 취소하려는 매수번호/매도번호
