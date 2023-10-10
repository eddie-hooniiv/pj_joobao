import random
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException, \
#     JavascriptException, NoAlertPresentException, TimeoutException

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# import re
# import numpy
import time
# import os
# import sys
# import cv2 as cv
# from pytesseract import image_to_string
# import warnings
# from win10toast import ToastNotifier
# import logging

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # 브라우저 열기
# # driver.maximize_window()
wait = WebDriverWait(driver, 10)
#
# # 로그인 페이지 접속
# driver.get('https://www.yes24.com/Templates/FTLogin.aspx')
# # time.sleep(1)
# # 로그인
# driver.find_element(By.ID, 'SMemberID').send_keys('ciel8318')
# driver.find_element(By.ID, 'SMemberPassword').send_keys('vmffkdl12!@')
# driver.find_element(By.ID, 'btnLogin').click()
# # time.sleep(1)
#
# #티켓 페이지
# # driver.find_element(By.LINK_TEXT, '티켓').click()
# # time.sleep(1)
#
# #렛미플라이 페이지
# driver.get('http://ticket.yes24.com/Perf/46671?Gcode=009_207')
# time.sleep(1)

#예매하기 클릭
driver.find_element(By.LINK_TEXT, '예매하기').click()
#
# #예매하기 창으로 포커스 변경
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

#날짜 클릭
# 11월로 넘겨주는 코드임. 실행할 때 활성화해야됨.
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar"]/div/a[2]/img'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2023-10-11"]'))).click()

#회차 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ulTime"]/li[1]'))).click()

#다음 단계 클릭
driver.find_element(By.XPATH, '//*[@id="StepCtrlBtn01"]/a/img').click()

#좌석 선택 (H열 14번으로 세팅, 개발자 도구에서 확인 가능)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divFlash"]/iframe')))
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="divFlash"]/iframe'))
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t1300023"]'))).click()

#좌석 선택 완료 클릭
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/p[2]/a/img'))).click()

# 할인/쿠폰에서 다음단계 누르기
driver.switch_to.default_content()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="StepCtrlBtn03"]/a[2]'))).click()

# 수령방법 다음단계 누르기
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rdoDeliveryBase"]')))
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element_value((By.ID, 'ordererMailD'), 'hanmail.net')
)
# name = driver.find_element(By.ID, 'ordererUserName')
# phone_1 = driver.find_element(By.ID, 'ordererMobile1')
# phone_2 = driver.find_element(By.ID, 'ordererMobile2')
# phone_3 = driver.find_element(By.ID, 'ordererMobile3')
# mail_h = driver.find_element(By.ID, 'ordererMailH')
# mail_d = driver.find_element(By.ID, 'ordererMailD')

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="StepCtrlBtn04"]/a[2]'))).click()

