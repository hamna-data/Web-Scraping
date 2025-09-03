from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Wait for search results to load
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
)

st = ""
for item in results:
    print(item.text)
    st += f"{item.text}\n"

with open("results.txt", "w", encoding="utf-8") as f:
    f.write(st)

assert "No results found." not in driver.page_source

input("Press Enter to close browser...")
driver.quit()
