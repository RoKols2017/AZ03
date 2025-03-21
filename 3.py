from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import re

# ⚙️ Настройки
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 🔄 Запуск драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.divan.ru/category/divany")
time.sleep(5)  # время на прогрузку

# 💾 Получаем HTML
html = driver.page_source
driver.quit()

# 🧠 Парсим BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
cards = soup.find_all("div", {"data-testid": "product-card"})

# 📦 Извлечение данных
products = []

for card in cards:
    title_tag = card.find("span", {"itemprop": "name"})
    price_tag = card.find("span", {"data-testid": "price"})

    if title_tag and price_tag:
        title = title_tag.get_text(strip=True)
        price_text = price_tag.get_text(strip=True)
        price = int(re.sub(r"[^\d]", "", price_text))

        products.append({"Название": title, "Цена": price})

# 🗂️ Сохраняем CSV
df = pd.DataFrame(products)
df.to_csv("sofas.csv", index=False, encoding="utf-8-sig")
print("✅ Данные сохранены в sofas.csv")

# 📊 Средняя цена
average = df["Цена"].mean()
print(f"📈 Средняя цена дивана: {round(average):,} ₽")

# 📉 Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(df["Цена"], bins=10, color="orange", edgecolor="black")
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена (₽)")
plt.ylabel("Количество товаров")
plt.grid(True)
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()
