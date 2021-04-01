# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:52:47 2021

@author: junob
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time as t
import random as r
import pyautogui
import pyperclip

main_url = 'https://www.gopax.co.kr/'
url ='https://www.gopax.co.kr/exchange/btc-krw'
url_bull = 'https://www.gopax.co.kr/exchange/btcbull-krw'
url_bear = 'https://www.gopax.co.kr/exchange/btcbear-krw'
#driver = webdriver.Firefox(executable_path=r'/home/pi/programing/python_folder/gopax_kakaotalk_macro/geckodriver')
driver = webdriver.Edge('../msedgedriver.exe')
#driver = webdriver.PhantomJS('../phantomjs-2.1.1-windows/bin/phantomjs.exe')

price_factor = 1000000

def notice_click():
    try:
        driver.find_elements_by_class_name('button-hide24hours-text')[0].click()
    except:
        pass
    
driver.get(main_url)
while True:
    try:
        notice_click()
        driver.find_elements_by_class_name('EmergencyPopup__button')[0].click()
        break
    except:
        t.sleep(1)
        

    
def text_to_number(text):
    number=''
    for i in text:
        try:
            if i =='.':
                number = number+'.'
            else:
                number = number+str(int(i))
        except:
            pass
    #print(price)
    try:
        number = eval(number) 
    except:
        number = 0

    return number

def send_to_kakaotalk(text):
    pyautogui.write(text)
    pyautogui.press('enter')
    
def send_to_kr_kakaotalk(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    
def coin_price(name):
    price = 0
    while True:
        # bs = BeautifulSoup(driver.page_source, 'html.parser')
        # price_text = bs.find('title').get_text()
        # print(price_text)
        try:
            if name == 'bit':
                #button = driver.find_elements_by_class_name('SelectableMarketFilters__filter')
                price_text = driver.find_elements_by_css_selector('#BTC\/KRW > td.SortableMarketTable__lastPriceCell.SortableTable__align--right > div')[0].text + ' KRW/BTC'
            elif name == 'bull':
                driver.find_elements_by_class_name('SelectableMarketFilters__filter')[2].click()
                price_text = driver.find_elements_by_css_selector('#BTCBULL\/KRW > td.SortableMarketTable__lastPriceCell.SortableTable__align--right > div')[0].text + ' KRW/BTCBULL'
                driver.find_elements_by_class_name('SelectableMarketFilters__filter')[1].click()
            elif name == 'bear':
                driver.find_elements_by_class_name('SelectableMarketFilters__filter')[2].click()
                price_text = driver.find_elements_by_css_selector('#BTCBEAR\/KRW > td.SortableMarketTable__lastPriceCell.SortableTable__align--right > div')[0].text + ' KRW/BTCBEAR'
                driver.find_elements_by_class_name('SelectableMarketFilters__filter')[1].click()
            price = text_to_number(price_text)
            print(price_text, price)
            break
        except:
            t.sleep(1)
    return price_text, price

def bitconet():
    location = pyautogui.locateOnScreen(r'bitconet.PNG')
    if location != None:    
        #print('yes')
        send_to_kakaotalk('https://youtu.be/faa5uf8ZJBA')
        send_to_kr_kakaotalk('빝코넥~~~~~~~~!')  

def bitcoin():
    location = pyautogui.locateOnScreen(r'bitcoin.PNG')
    if location != None:    
        #print('yes')
        price_text, price = coin_price('bit')
        send_to_kakaotalk(url+'\n'+price_text)
        
def bitcoin_bull():
    location = pyautogui.locateOnScreen(r'bitcoinbull.PNG')
    if location != None:    
        #print('yes')
        #driver.get(url_bull)
        price = 0
        price_text, price = coin_price('bull')
        send_to_kakaotalk(url_bull+'\n'+price_text)
        #driver.get(url)
     
def bitcoin_bear():
    location = pyautogui.locateOnScreen(r'bitcoinbear.PNG')
    if location != None:  
        #print('yes')
        #driver.get(url_bear)
        price = 0
        price_text, price = coin_price('bear')
        send_to_kakaotalk(url_bear+'\n'+price_text)
        #driver.get(url)

def still_jusik():
    location = pyautogui.locateOnScreen(r'stilljusik.PNG')
    if location != None:  
        send_to_kakaotalk('https://youtu.be/F99hkg1wCNg')
    
def dduckrock():
    location = pyautogui.locateOnScreen(r'dduckrock.PNG')
    if location != None:  
        send_to_kakaotalk('https://youtu.be/Zig99GrHnpw')
        
def dducksang():
    location = pyautogui.locateOnScreen(r'dducksang.PNG')
    if location != None:
        send_to_kr_kakaotalk('정보를 찾을 수 없습니다.')   
        
def hangang():
    location = pyautogui.locateOnScreen(r'hangang.PNG')
    if location != None:
        driver.get('https://hangang.life/')
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        temp = bs.find('head').find('meta',{'name':'description'})
        temp = str(temp)
        temp = temp.split(' ')[5]
        send_to_kr_kakaotalk('현재 한강 수온은 '+temp+'°C 입니다')
        driver.get(url)
        while True:
            try:
                driver.find_elements_by_class_name('EmergencyPopup__button')[0].click()
                break
            except:
                t.sleep(1)

def lotto():
    location = pyautogui.locateOnScreen(r'lotto.PNG')
    if location != None:
        lotto_list = range(1,46)
        lotto_number = r.sample(lotto_list,6)
        send_to_kr_kakaotalk('빝코넷의 추천 번호: '+str(lotto_number))  

def magic_sora():
    location = pyautogui.locateOnScreen(r'magicsora.PNG')
    if location != None:
        answer_list = ['그래','안돼']
        send_to_kr_kakaotalk(r.choice(answer_list))   
    
def percent(a,b):
    per = (a/b-1)*100
    per_text = '%0.2f'%(per)+'%'
    return per_text

btc_b = coin_price('bit')[1]
#driver.get(url_bull)
btc_bull_b = coin_price('bull')[1]
#driver.get(url_bear)
btc_bear_b = coin_price('bear')[1]
#driver.get(url)

now = datetime.now()
day_b = now.day
price_factor_b = 0
while True:
    t.sleep(1)
    notice_click()
    bitconet()
    bitcoin()
    bitcoin_bull()
    bitcoin_bear()
    still_jusik()
    dduckrock()
    dducksang()
    hangang()
    lotto()
    magic_sora()
    
    price_text, price = coin_price('bit')
    price_factor_a = price//price_factor
    
    if price_factor_a > price_factor_b:
        send_to_kakaotalk('UP! ' + price_text)
    elif price_factor_a < price_factor_b:
        send_to_kakaotalk('DOWN! ' + price_text)
    price_factor_b = price_factor_a

    now = datetime.now()
    day_a = now.day
    if day_a != day_b:
        btc_a = coin_price('bit')[1]
        # driver.get(url_bull)
        btc_bull_a = coin_price('bull')[1]
        # driver.get(url_bear)
        btc_bear_a = coin_price('bear')[1]
        # driver.get(url)
        send_to_kakaotalk('BTC: '+'{:,}'.format(btc_a)+' KRW, '+percent(btc_a,btc_b))
        send_to_kakaotalk('BTC BULL: '+'{:,}'.format(btc_bull_a)+' KRW, '+percent(btc_bull_a,btc_bull_b))
        send_to_kakaotalk('BTC BEAR: '+'{:,}'.format(btc_bear_a)+' KRW, '+percent(btc_bear_a,btc_bear_b))
        btc_b = btc_a
        btc_bull_b = btc_bull_a
        btc_bear_b = btc_bear_a
    day_b = day_a
