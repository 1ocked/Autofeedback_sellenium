# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = "https://feedback.adidas.com/jfe/form/SV_0rcLuegxUa4m2PA?u=35015&tr=0&Q_Language=EN&isper=1"
#
# service = Service("D:\\piton_files\\AutoFeedback\\chromedriver\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# try:
#     driver.get(url)
#     wait = WebDriverWait(driver, 10)
#
#     def click_element(by, value):
#         element = wait.until(EC.element_to_be_clickable((by, value)))
#         element.click()
#
#     print("Клик по первой кнопке 'NextButton'")
#     click_element(By.ID, "NextButton")
#
#     print("Клик по элементу 'QID2-9-label'")
#     click_element(By.ID, "QID2-9-label")
#
#     print("Клик по следующей кнопке 'NextButton'")
#     click_element(By.ID, "NextButton")
#
#     print("Клик по элементу с padding")
#     click_element(By.CSS_SELECTOR, "[style*='padding-bottom: 0px;']")
#
#     print("Клик по зоне ввода 'QR~QID4'")
#     input_area = wait.until(EC.element_to_be_clickable((By.ID, "QR~QID4")))
#     input_area.click()
#     input_area.send_keys("Good price and huge choice")
#
#     print("Клик по 'NextButton' после ввода комментария")
#     click_element(By.ID, "NextButton")
#
#     for qid in ["QID7-1-label", "QID22-2-label", "QID9-2-label"]:
#         print(f"Клик по элементу '{qid}'")
#         click_element(By.ID, qid)
#
#     print("Клик по кнопке 'NextButton'")
#     click_element(By.ID, "NextButton")
#
#     for qid in ["QID10-1-label", "QID10-5-label", "QID10-3-label", "QID10-4-label"]:
#         print(f"Клик по элементу '{qid}'")
#         click_element(By.ID, qid)
#
#     print("Клик по следующему 'NextButton'")
#     click_element(By.ID, "NextButton")
#
#     print("Клик по 'QID13-2-label'")
#     click_element(By.ID, "QID13-2-label")
#
#     print("Клик по 'QID14-3-label'")
#     click_element(By.ID, "QID14-3-label")
#
#     print("Клик по последнему 'NextButton'")
#     click_element(By.ID, "NextButton")
#     click_element(By.ID, "NextButton")  # Последний клик
#
# except Exception as ex:
#     print("Произошла ошибка:", ex)
# finally:
#     driver.quit




# Ваш скрипт на Selenium выглядит хорошо и структурирован для автоматизации подачи отзывов на сайте Adidas. Вот несколько предложений и улучшений, которые вы можете рассмотреть:
#
# Обработка ошибок: Вместо того чтобы ловить общие исключения, вы можете быть более конкретными в том, какие типы исключений хотите обрабатывать. Это поможет предоставить более целенаправленную информацию о проблемах.
#
# Использование time.sleep(): Хотя time.sleep() иногда необходим, предпочтительнее полагаться на WebDriverWait. Это сделает скрипт более эффективным и менее подверженным проблемам с таймингом.
#
# Динамические ожидания: Вы можете более эффективно использовать динамические ожидания для работы с элементами, которые могут загружаться с разным временем ожидания.
#
# Модульность: Если скрипт вырастет в сложности, рассмотрите возможность разбивки его на функции для улучшения читаемости и обслуживания.


