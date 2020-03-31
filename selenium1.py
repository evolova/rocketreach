from selenium import webdriver
from time import sleep
import csv

DRIVER = '/Users/volova/Downloads/chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get('https://rocketreach.co/educational-employees-credit-union-email-format_b5c91e71f42e36e2')
sleep(10)
element = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/ul/li/div/div[2]/ul/li[1]/a')

links = []
for ii in range(len(element)):
    #print(element[ii].get_attribute('href'))
    link = element[ii].get_attribute('href')
    links.append(link)

csv_lists=[]
for link in links:
    list = []

    list.append(link)
    driver.get(link)
    sleep(10)

    name = driver.find_element_by_xpath('//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[1]/div/h1/a/span[1]')
    name = name.text
    name, a = name.split("'")
    list.append(name)

    position = driver.find_element_by_xpath('//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[1]/div/h3')
    position = position.text
    position, a = position.split('@')
    list.append(position)

    fb = driver.find_element_by_xpath('//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[2]/div/div/ply-links-directive/ul/li[4]/a')
    fb= fb.get_attribute('href')
    list.append(fb)

    ln = driver.find_element_by_xpath('//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[2]/div/div/ply-links-directive/ul/li[2]/a')
    ln = ln.get_attribute('href')
    list.append(ln)

    print(list)
    # csv_lists.append(list)

    with open(r'selenium1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(list)

driver.quit()
# position = '//*[@id="blur-container"]/div[3]/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/ul/li/div/div[2]/ul/li[2]'
#
# name = '//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[1]/div/h1/a/span[1]'
#
# fb = '//*[@id="blur-container"]/div[3]/div/div[2]/div/div[1]/div[2]/div/div/ply-links-directive/ul/li[4]/a'
