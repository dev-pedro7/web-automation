from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://anydesk.com/pt')
navegador.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div[2]/div/div[1]/a').click()






input("Pressione Enter para fechar o navegador...")
navegador.quit()