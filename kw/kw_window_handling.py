# -*- coding: utf-8 -*-
# kw_window_handling.py
"""
영웅문Global의 창열기/닫기/선택
"""

import pyautogui as pag
import time
from kw_naming import *


# 모든 화면 끄기
def close_all_window(닫기박스, region=(0, 120, 2560, 1500)):
    box_close = pag.locateOnScreen(닫기박스, confidence=CONFIDENCE, region=region)
    while box_close is not None:
        box_close = pag.locateOnScreen(닫기박스, confidence=CONFIDENCE, region=region)
        pag.click(box_close, duration=0.25)
    pag.sleep(WAIT_TIME)


# 화면 띠우기
def open_window(화면번호):
    pag.click(좌표_메인_화면번호입력란)
    pag.write(화면번호)
    pag.sleep(WAIT_TIME)


# 창 선택
def select_item(아이템이름, chktim=5, region=(0, 0, 2560, 1500)):
    end_time = time.time() + chktim
    while time.time() < end_time:
        sel_image = pag.locateOnScreen(아이템이름, confidence=CONFIDENCE, region=region)
        if sel_image is not None:
            pag.click(sel_image, duration=0.25)
            end_time = 0
        elif time.time() > end_time:
            raise Exception("해당 창이 열려있지 않습니다.")
        else:
            continue
    pag.sleep(WAIT_TIME)


# 아이콘 또는 버튼 위치 찾기
def search_location(아이템이름):
    center = pag.locateCenterOnScreen(아이템이름)
    return center


# 계좌 선택
def select_account(계좌번호):
    loc_account = pag.locateCenterOnScreen(img_탭_실시간잔고계좌번호, confidence=CONFIDENCE, region=(0, 120, 2560, 1500))
    pag.moveTo(loc_account, duration=0.1)
    pag.move(90, 0, duration=0.1)
    pag.click()

    # [맨 위 계좌]로 이동
    i = 10
    while i > 0:
        pag.hotkey("up")
        i -= 1

    # [원하는 계좌]로 이동하여 선택
    i = 계좌번호
    while i > 0:
        pag.hotkey("down")
        i -= 1
    pag.hotkey("enter")
    pag.sleep(WAIT_TIME)


if __name__ == '__main__':
    pass
