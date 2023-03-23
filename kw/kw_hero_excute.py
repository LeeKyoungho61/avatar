# -*- coding: utf-8 -*-
# kw_hero_excute.py
"""
키움 영웅문 Global 프로그램 실행,
공동인증서 로그인
"""

from kw_window_handling import *
import subprocess


def hero_excute():
    # 영웅문Global 실행
    kw_hero: str = r'c:\KiwoomGlobal\bin\nfstarter.exe'
    subprocess.Popen(kw_hero)
    # 공동인증서 로그인
    select_item(img_버튼_공동인증서로그인)  # [공동인증서 로그인] 버튼 클릭
    select_item(img_탭_인증서이경호)  # [이경호 인증서] 선택
    pag.write(img_인증서비번_이경호, interval=0.1)  # [비밀번호] 입력
    pag.hotkey('enter')
    # [영웅문Global 프로그램] 화면에 표시될때까지 대기한다(300초)
    select_item(img_탭_영웅문로고, chktim=300, region=(0, 0, 150, 40))
    pag.sleep(5)  # 초기화면 나올때까지 5초 대기
    # 영웅문Global 초기화면의 [접속정보]화면을 닫는다(20초)
    select_item(img_박스_접속상태화면닫기, chktim=20, region=(0, 120, 500, 500))


if __name__ == '__main__':
    hero_excute()
