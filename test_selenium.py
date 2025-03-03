from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.google.co.jp/')
driver.get('https://www.google.co.jp/')

# 検索フィールドの取得
query = driver.find_element(by=By.NAME, value='q')

# 検索文字列を入力
query.send_keys('バナナはおやつに入りますか')

# 3秒待つ
time.sleep(3)

# 検索ボタンをクリック
button = driver.find_element(by=By.NAME, value='btnK')
button.click()

# 3秒待つ
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

ll = [x for x in soup.text.split(' ') if len(x) > 0]
for count, value in enumerate(ll):
    print(count, value)
