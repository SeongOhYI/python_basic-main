from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        time.sleep(2)
        if before_scroll_height == after_scroll_height:
            break
    time.sleep(2)
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    print("영상 갯수: ", len(titles))
    return titles

# 브라우저 실행
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
# 검색어 입력
search_input = driver.find_element(By.CSS_SELECTOR, "input#search")
search_input.send_keys("뉴진스")
# 검색버튼 클릭
search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
search_button.click()
time.sleep(2)
# 필터버튼 클릭
filter_button = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
filter_button.click()
time.sleep(2)
# 조회수 클릭
hits = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
hits.click()
time.sleep(2)
# 무한 스크롤 함수 호출
titles = scroll()

for title in titles:
    print(title.text)