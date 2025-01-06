from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL формы
url = "https://feedback.adidas.com/jfe/form/SV_0rcLuegxUa4m2PA?u=35015&tr=0&Q_Language=EN&isper=1"

# Инициализация веб-драйвера
service = Service("D:\\piton_files\\AutoFeedback\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

def click_element(identifier):
    """Клик по элементу."""
    element = wait.until(EC.element_to_be_clickable(identifier))
    element.click()

def fill_input(identifier, text):
    """Заполнение текстового поля."""
    input_area = wait.until(EC.element_to_be_clickable(identifier))
    input_area.click()
    input_area.send_keys(text)

# Укажите количество повторений
repeat_count = 10

# Список комментариев для разных итераций
comments = [
    "Good price and huge choice!",
    "Fast delivery and great quality!",
    "Excellent customer service!",
    "Will definitely recommend to friends.",
    "Loved the selection of products!"
]

try:
    for i in range(repeat_count):
        driver.get(url)

        print("Клик по первой кнопке 'NextButton'")
        click_element((By.ID, "NextButton"))

        print("Клик по элементу 'QID2-9-label'")
        click_element((By.ID, "QID2-9-label"))

        print("Клик по следующей кнопке 'NextButton'")
        click_element((By.ID, "NextButton"))

        print("Клик по элементу с padding")
        click_element((By.CSS_SELECTOR, "[style*='padding-bottom: 0px;']"))

        # Используем комментарий из списка на основе итерации
        comment_to_use = comments[i]  # Теперь используем i как индекс
        print(f"Клик по зоне ввода 'QR~QID4' с комментарием: '{comment_to_use}'")
        fill_input((By.ID, "QR~QID4"), comment_to_use)

        print("Клик по 'NextButton' после ввода комментария")
        click_element((By.ID, "NextButton"))

        # Добавляем клики в указанном порядке
        for qid in ["QID7-1-label", "QID22-2-label", "QID9-2-label"]:
            print(f"Клик по элементу '{qid}'")
            click_element((By.ID, qid))

        print("Клик по кнопке 'NextButton'")
        click_element((By.ID, "NextButton"))

        for qid in ["QID10-1-label", "QID10-5-label", "QID10-3-label", "QID10-4-label"]:
            print(f"Клик по элементу '{qid}'")
            click_element((By.ID, qid))

        print("Клик по следующему 'NextButton'")
        click_element((By.ID, "NextButton"))

        print("Клик по 'QID13-2-label'")
        click_element((By.ID, "QID13-2-label"))

        print("Клик по 'QID14-3-label'")
        click_element((By.ID, "QID14-3-label"))

        print("Клик по последнему 'NextButton'")
        click_element((By.ID, "NextButton"))
        print("Клик по последнему 'NextButton' (финальный клик)")
        click_element((By.ID, "NextButton"))

except Exception as ex:
    print(f"Произошла ошибка на этапе {i + 1}: {ex}")

finally:
    driver.quit()
