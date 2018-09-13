import time
import random
from selenium import webdriver
aux=0
while(aux<30):
	chromedriver = "C:/Users/pablo/AppData/Local/Programs/Python/Python37-32/google form/chromedriver"
	driver = webdriver.Chrome(chromedriver)

	link = 'https://docs.google.com/forms/d/e/1FAIpQLSfmkfcNrWouCmb-j4jpF6ztHzHsCwqzNcY6OEz4Tpd6RWmEwQ/viewform?usp=sf_link'
	driver.get(link)
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div/content/span'
	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(2)
	xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
	xpm = ']/div[2]/div/content/div/label['
	xpe = ']/div[2]/div/div[3]/div'
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span'
	maxnum = [5,5,5,5,5]  #number of choice for each questions

	num_ans = []
	for i in range(0, len(maxnum)):
		num_ans.append(random.randint(4,maxnum[i]))


	nqT = len(maxnum)

	for i in range(2,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.1)

	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(0.2)
		
	xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
	xpm = ']/div[2]/div/content/div/label['
	xpe = ']/div[2]/div/div[3]/div'
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span'
	maxnum = [5,5,5,5]  #number of choice for each questions

	num_ans = []
	for i in range(0, len(maxnum)):
		num_ans.append(random.randint(4,maxnum[i]))


	nqT = len(maxnum)

	for i in range(2,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.1)

	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(0.2)

		
	xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
	xpm = ']/div[2]/div/content/div/label['
	xpe = ']/div[2]/div/div[3]/div'
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span'
	maxnum = [5,5,5,5,5,5,5,5]  #number of choice for each questions

	num_ans = []
	for i in range(0, len(maxnum)):
		num_ans.append(random.randint(4,maxnum[i]))


	nqT = len(maxnum)

	for i in range(2,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.1)

	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(0.2)

		
	xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
	xpm = ']/div[2]/div/content/div/label['
	xpe = ']/div[2]/div/div[3]/div'
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span'
	maxnum = [5,5,5,5]  #number of choice for each questions

	num_ans = []
	for i in range(0, len(maxnum)):
		num_ans.append(random.randint(4,maxnum[i]))


	nqT = len(maxnum)

	for i in range(2,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.1)

	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(0.1)

		
	xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
	xpm = ']/div[2]/div/content/div/label['
	xpe = ']/div[2]/div/div[3]/div'
	submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span'
	maxnum = [5,5,5]  #number of choice for each questions

	num_ans = []
	for i in range(0, len(maxnum)):
		num_ans.append(random.randint(4,maxnum[i]))


	nqT = len(maxnum)

	for i in range(2,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.1)

	xinput='//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input'
	submit = driver.find_element_by_xpath(xinput)
	submit.send_keys('Anonimo')
	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(0.2)
	aux=aux+1