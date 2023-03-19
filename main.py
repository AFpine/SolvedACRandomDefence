from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import os

# Need Chromedriver

result = ''     # selected problems
search_str = '' # search query

users = input("Input Users\n").split()      # BOJ 이름들을 띄어쓰기로 구분해서 입력
levels = input("Input Levels\n").split()    # 원하는 문제의 레벨들을 띄어쓰기로 구분해서 입력
minv, maxv = map(int, input("Input Min and Max\n").split())     # 푼 사람 수의 최소 / 최대 값을 띄어쓰기로 구분해서 입력
delay = 1       # 만약 문제가 뽑히기 전에 chrome 창이 꺼진다면 이 값을 키우기

for user in users :
    search_str += f'!@{user} '
search_str += f's#{minv}..{maxv} '

search_str += '!#math '

options = webdriver.ChromeOptions()
options.add_argument("headless")        # 이 옵션을 끄면 chrome창이 켜지는게 눈에 보임 
                                        # 켜놓으면 cookie error가 뜨지만 상관은 없음
                                        
# chrome_driver_dir = 'C:/Users/mrt20/Desktop/AFpine/_etc/'     # hard coding
chrome_driver_dir = os.getcwd()     
chrome_driver_dir += '/chromedriver'
chrome_driver_dir.replace('\\', '/')

driver = webdriver.Chrome(chrome_driver_dir, options=options)
driver.get('https://solved.ac/search?query=')
time.sleep(delay)

search_box = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[1]/input')

random.shuffle(levels)
for level in levels :
    t_search_str = search_str + f'*{level}'
    
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(t_search_str)
    search_box.send_keys(Keys.ENTER)
    time.sleep(delay)

    suffle_button = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[1]/div/a[6]')
    suffle_button.click()
    time.sleep(delay)

    res = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/span/a/span')
    result += str(res.get_attribute('innerHTML')) + " "
    # time.sleep(delay)
driver.quit()

print("\n\n\nlist :", result)
