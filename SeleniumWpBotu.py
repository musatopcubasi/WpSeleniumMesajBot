from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


isim ="23'D"
mesaj="SAYGILI BİR BİREY OLDUĞUN İÇİN TEŞEKKÜR EDERİM İLBEYCİM"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

print('Karekodu telefondan okuttuktan sonra WhatsApp ekranının gelmesini bekleyin.')
input("Ekran geldiyse enter'a basın:")
kisibul =driver.find_element_by_xpath('//span[@title="{}"]'.format(isim))
kisibul.click()
sayi=0
while True:
    mesajalani = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    mesajalani.send_keys(mesaj + Keys.ENTER)
    if sayi==500:
        break
    sayi+=1


print('Mesajınız gönderildi.')
input('Çıkmak için entera basınız.')