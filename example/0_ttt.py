# import numpy as np
# import pyautogui as pag
# import cv2
# import pytesseract
# from PIL import Image
# from imutils.perspective import four_point_transform
# import matplotlib.pyplot as plt
# import imutils
# import re
# import requests

# 보유량 화면 확인
# 실시간잔고_보유량 = pag.locateOnScreen("kw_my_holdings.png")
# print(실시간잔고_보유량)

# 스크린 샷 찍기
# pag.sleep(10)
# img = pag.screenshot(region=(1080, 677, 90, 50))
# img.save("screenshot.png")  # 파일로 저장

# https://mokeya.tistory.com/146
# 보유량 추출 - 처리 없음
# filename = 'screenshot_2.png'
# image = np.array(Image.open(filename))
# text = pytesseract.image_to_string(image, lang='kor+eng')
# print(".")
# print("..")
#
# print(text)

# 전처리 - 노이즈 제거 (normalization, thresholding, image blur)
# norm_img = np.zeros((image.shape[0], image.shape[1]))
# img = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)
# img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
# img = cv2.GaussianBlur(img, (1, 1), 0)
# text = pytesseract.image_to_string(img, lang='kor')
# print("...")
# print("....")
#
# print(text)
# =================================================

# https://yunwoong.tistory.com/58
# 보유량 추출 - 처리 없음
# import pytesseract
# import cv2
# import matplotlib.pyplot as plt
#
# path = 'screenshot_2.png'
# image = cv2.imread(path)
# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image
# text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
# print("By 김윤웅")
# print(text)


# OCR - 전처리
from imutils.perspective import four_point_transform
import matplotlib.pyplot as plt
import pytesseract
import imutils
import cv2
import re
import requests
import numpy as np


# def plt_imshow(title='image', img=None, figsize=(8, 5)):
#     plt.figure(figsize=figsize)
#
#     if type(img) == list:
#         if type(title) == list:
#             titles = title
#         else:
#             titles = []
#
#             for i in range(len(img)):
#                 titles.append(title)
#
#         for i in range(len(img)):
#             if len(img[i].shape) <= 2:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
#             else:
#                 rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
#
#             plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
#             plt.title(titles[i])
#             plt.xticks([]), plt.yticks([])
#
#         plt.show()
#     else:
#         if len(img.shape) < 3:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         else:
#             rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#         plt.imshow(rgbImg)
#         plt.title(title)
#         plt.xticks([]), plt.yticks([])
#         plt.show()


# def run_tesseract_ocr(image, width, ksize=(5, 5), min_threshold=75, max_threshold=200, lang='eng'):
#     image_list_title = []
#     image_list = []
#
#     image = imutils.resize(image, width=width)
#     ratio = org_image.shape[1] / float(image.shape[1])
#
#     # 이미지를 grayscale로 변환하고 blur를 적용
#     # 모서리를 찾기위한 이미지 연산
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, ksize, 0)
#     edged = cv2.Canny(blurred, min_threshold, max_threshold)
#
#     image_list_title = ['gray', 'blurred', 'edged']
#     image_list = [gray, blurred, edged]
#
#     # contours를 찾아 크기순으로 정렬
#     cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
#
#     receiptCnt = None
#
#     # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
#     for c in cnts:
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#         # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영수증 영역으로 판단하고 break
#         if len(approx) == 4:
#             receiptCnt = approx
#             break
#
#     # 만약 추출한 윤곽이 없을 경우 오류
#     if receiptCnt is None:
#         raise Exception(("Could not find receipt outline."))
#
#     output = image.copy()
#     cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)
#
#     image_list_title.append("Receipt Outline")
#     image_list.append(output)
#
#     # 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
#     receipt = four_point_transform(org_image, receiptCnt.reshape(4, 2) * ratio)
#
#     plt_imshow(image_list_title, image_list)
#     plt_imshow("Receipt Transform", receipt)
#
#     options = "--psm 4"
#
#     text = pytesseract.image_to_string(cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB), lang=lang, config=options)
#
#     # OCR결과 출력
#     print("[INFO] OCR결과:")
#     print("==================")
#     print(text)


# image_nparray = np.asarray('screenshot.png')
# org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
# org_image = 'screenshot.png'
# run_tesseract_ocr(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100, lang='kor+eng')


import os
import pywinauto
import subprocess
import time

os.system('chcp 65001')

# 그리드 매매 단톡방에서 퍼옴
########################################################################
# 함수 선언부 (그리드 매매법 단톡방에서 펌)
########################################################################
# 프로세스 강제종료
# def close_process_cmd(process):
#     if process in os.popen('tasklist /fi "IMAGENAME eq %s"' % process).read():
#         subprocess.call(['taskkill', '/F', '/T', '/IM', process])
#
#
# def app_start_wait(path):
#     result = pywinauto.timings.wait_until_passes(g_timeout, g_retry_interval,
#                                                  lambda: pywinauto.Application("win32").start(path))
#     print(result)
#     return result
#
#
# def app_conn_wait(**kwargs):
#     result = pywinauto.timings.wait_until_passes(g_timeout, g_retry_interval,
#                                                  lambda: pywinauto.Application("win32").connect(**kwargs))
#     top_win = pywinauto.timings.wait_until_passes(g_timeout, g_retry_interval,
#                                                   lambda: result.top_window())  # top_window가 활성화 될때까지 대기
#     top_win.wait('ready', g_timeout, g_retry_interval)  # 윈도우가 보이고 활성화시까지 대기
#     top_win.set_focus()
#     print(top_win)
#     return top_win
#
#
# def win_child_wait(win, **kwargs):
#     print(win.children())
#     result = pywinauto.timings.wait_until_passes(g_timeout, g_retry_interval, lambda: win.children(**kwargs))
#     print(result)
#     if isinstance(result, list):    # 배열인경우
#         kwargs['idx'] = kwargs.get('idx', 0)  # array_idx 키가 없을경우 0
#         child = result[kwargs['idx']]  # 결과값의 array_idx 항목
#     else:
#         child = result
#     pywinauto.timings.wait_until_passes(g_timeout, g_retry_interval,
#                                         lambda: child.is_enabled())  # child가 활성화 될때까지 대기
#     child.set_focus()
#     return child
#
#
# ########################################################################
# # 변수 선언부
# ########################################################################
# g_timeout = 20
# g_retry_interval = 0.5
# g_win_info = {}  # 윈도우 정보 저장
# g_ctl_info = {}  # 컨트롤 정보 저장
# g_win_info["cert"] = {'title_re': '.*인증서 선택.*'}
# g_ctl_info["cert_edit_pass"] = {'class_name': 'Edit'}
# g_ctl_info["cert_btn_confirm"] = {'title': '인증서 선택(확인)', 'class_name': 'Button'}
# g_cert_pass = ''  # 본인 비번 입력하세요!(간편인증 or 공인인증)
# desktop = pywinauto.Desktop(backend='uia')
#
# ########################################################################
# # 프로그램 실행 및 로그인창 찾기
# ########################################################################
# close_process_cmd('nfstarter.exe')
# close_process_cmd('nfrunlite.exe')
# app_login = app_start_wait(r'C:\KiwoomGlobal\bin\nfstarter.exe')  # 프로그램 실행
# win_cert = app_conn_wait(**g_win_info["cert"])  # 인증서 창 찾기
# win_cert_edit_password = win_child_wait(win_cert, **g_ctl_info["cert_edit_pass"])  # 첫번째 Edit 컨트롤창
# win_cert_btn_password = win_child_wait(win_cert, **g_ctl_info["cert_btn_confirm"])  # 인증서 비밀번호 입력 확인버튼
#
# ########################################################################
# # 패스워드 입력->로그인버튼 클릭
# ########################################################################
# win_cert_edit_password.type_keys(g_cert_pass)  # 패스워드 입력
# win_cert.wait('ready')
# win_cert_btn_password.click_input()
#
# ########################################################################
# # 영웅문 Global 창 찾기 -> 모든창 닫기 클릭
# ########################################################################
# g_win_info["main"] = {'path': r'C:\KiwoomGlobal\bin\nfrunlite.exe'}
# g_ctl_info["main_menu"] = {'class_name': 'ReBarWindow32'}
#
# win_main = app_conn_wait(**g_win_info["main"])  # 메인 창 찾기 nfrunlite.exe
# main_menu = win_child_wait(win_main, **g_ctl_info["main_menu"])  # 메인메뉴 찾기
# main_menu.right_click_input()  # 오른쪽 버튼 클릭
# desktop.컨텍스트.wait('visible', g_timeout, g_retry_interval)  # 컨텍스트메뉴 보일때까지 대기
# desktop.컨텍스트.child_window(title='모든 창 닫기', control_type='MenuItem').click_input()
#
# ########################################################################
# # 메뉴코드 입력: 2150(실시간잔고)->닫기->2152(실시간 미체결)
# ########################################################################
# g_ctl_info["main_menu_toolbar"] = {'title': '메뉴툴바'}
# g_ctl_info["main_menu_toolbar_edit"] = {'class_name': 'Edit'}
# main_menu_toolbar = win_child_wait(win_main, **g_ctl_info["main_menu_toolbar"])  # 메뉴툴바 찾기
# main_menu_toolbar_edit = win_child_wait(main_menu_toolbar, **g_ctl_info["main_menu_toolbar_edit"])  # 메뉴툴바 찾기
# main_menu_toolbar_edit.click_input()
# main_menu_toolbar_edit.type_keys('2150{ENTER}')
# main_menu_toolbar_edit.type_keys('{ESC}')
# main_menu_toolbar_edit.click_input()
# main_menu_toolbar_edit.type_keys('2152{ENTER}')


