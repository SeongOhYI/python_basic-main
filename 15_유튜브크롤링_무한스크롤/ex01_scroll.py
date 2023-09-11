from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# 스크롤을 바닥까지 내리기 위한 반복문 
while True:
    # 스크롤을 내리기 전 화면의 높이 
    before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    # 현재 상태에서 바닥으로 스크롤을 내림 
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    # 로딩 시간 고려해서 잠시 대기 
    time.sleep(2)
    # 스크롤 내린 뒤 화면의 높이 
    after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    time.sleep(2)
    # 스크롤 내리기 전, 후의 높이값 비교하여 높이값이 같다면(다 내려갔다면) 반복문 종료 
    if before_scroll_height == after_scroll_height:
        break

time.sleep(10)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# titles = driver.find_elements(By.ID, "video-title")

print("영상 갯수: ", len(titles))
for title in titles:
    print(title.text)