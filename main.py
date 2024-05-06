
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule

# Configurando o navegador
driver = webdriver.Chrome()  # ou o navegador de sua preferência
driver.get('https://awstou.ifractal.com.br/fulltime/phonto.php')


# Função para bater ponto
def BaterPonto():
    # Espera até que os campos de login e senha estejam presentes na página
    login_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="registro_foto_login"]'))
    )
    senha_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-holder"]/form/div[1]/input[2]'))
    )

    # Preenche os campos de login e senha
    print(login_input)
    print(senha_input)
    login_input.send_keys('guilhermes')
    senha_input.send_keys('Padrao@2023')

    # Clica no botão de login
    login_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-holder"]/form/div[1]/button'))
    )
    login_button.click()
    print('apertou o botao')

    # Espera 30 segundos para garantir que o login seja realizado
    time.sleep(30)
    print("Ponto batido com sucesso.")

# Função para agendar a execução da função BaterPonto
def agendar_bater_ponto():
    schedule.every().day.at("08:00").do(BaterPonto)
    schedule.every().day.at("12:00").do(BaterPonto)
    schedule.every().day.at("14:00").do(BaterPonto)
    schedule.every().day.at("18:00").do(BaterPonto)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Espera 1 minuto antes de verificar novamente os agendamentos

# Chama a função para agendar a execução da função BaterPonto
agendar_bater_ponto()

