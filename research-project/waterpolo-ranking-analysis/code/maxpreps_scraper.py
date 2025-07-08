from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_driver_path = "C:/chromedriver138/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://www.maxpreps.com/water-polo/spring/rankings/1/"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
)

rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 6:
        data.append({
            "Rank": cols[0].text.strip(),
            "School": cols[1].text.strip(),
            "State": cols[2].text.strip(),
            "Record": cols[3].text.strip(),
            "Rating": cols[4].text.strip(),
            "Strength": cols[5].text.strip(),
        })

driver.quit()

df = pd.DataFrame(data)
df.to_csv("water_polo_rankings.csv", index=False)
print(df)
