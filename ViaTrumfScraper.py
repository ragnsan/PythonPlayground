from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#åpne ViaTrumf
ViaTrumf = driver.get("https://viatrumf.no/kategori")
driver.implicitly_wait(10)

#klikk bort valg om notifikasjoner
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div").click()

#velge kategori å sortere etter
driver.find_element_by_id("merchant-sort").click()

#sorter etter de med høyeste bonus
driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/select/option[2]").click()

