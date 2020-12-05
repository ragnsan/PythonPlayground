
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

link = driver.get("https://youtube.com")
driver.implicitly_wait(10)


#velg å ikke logge på YouTube
ikkeLoggPå = driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button").click()


#find search bar
searchBar = driver.find_element_by_name("search_query")

#click searchbar
searchBar.click()

#type in text
searchBar.send_keys("Rick Astley Never Gonna Give You Up")

#seach by clicking enter
searchBar.send_keys(Keys.RETURN)

#find first video
video = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")[0]

#click on video
video.click()


# #click search button
# searchButton = driver.find_element_by_id("search-icon-legacy")