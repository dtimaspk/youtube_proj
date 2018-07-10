from selenium import webdriver
import html_builder as builder


chrome_driver = '/web_drivers/chromedriver'

def get_info_canal(url, num):
	browser = webdriver.Chrome(executable_path = chrome_driver)
	browser.get(url)

	nome_canal = browser.find_element_by_id('channel-title').text
	img_canal = browser.find_element_by_id('avatar').find_element_by_id('img').get_attribute('src')
	
	div_canal = builder.criar_div_canal(img_canal, num)
	
	browser.close()

	return div_canal

def get_info_video(url, num):
	browser = webdriver.Chrome(executable_path = chrome_driver)
	browser.get(url)

	videos = browser.find_elements_by_tag_name('ytd-grid-video-renderer')

	div_video = ''
	for x in range(5):
		div_video += builder.criar_div_video(videos[x].find_element_by_id('img').get_attribute('src'),videos[x].find_element_by_id('video-title').text,videos[x].find_element_by_id('video-title').get_attribute('href'), num)
			
	browser.close()

	return div_video

