from selenium import webdriver    #open webdriver for specific browser
import pandas as pd
import time

driver = webdriver.Chrome('E:\\chromedriver.exe')
driver.get("https://www.searchmy.bio/search?q=coach&hashtags=true")

nameslst = []
followerslst = []
biolst = []
linkslst = []
imglst = []

# extract data and stored into the above lists
def url_scrp():
	for i in range(0,1): #by increasing range it scrape more and more data
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		names = driver.find_elements_by_class_name('search-result-username')
		followers = driver.find_elements_by_class_name('search-result-data-table')
		bios = driver.find_elements_by_class_name('search-result-bio')
		profile_url = driver.find_elements_by_class_name('search-result-button')
		img_urls = driver.find_elements_by_class_name('search-result-profile-pic')

		for name in names:
			nameslst.append(name.text)

		for follower in followers:
			followerslst.append(follower.text)


		for bio in bios:
			biolst.append(bio.text)

		for link in profile_url:
			if(link.text == "View profile"):
				linkslst.append(link.get_attribute("href"))

		for img in img_urls:
			imglst.append(img.get_attribute('src'))

# import data in to csv file
def table(lst1, lst2, lst3, lst4, lst5):
	lst = [lst1, lst2, lst3, lst4, lst5]


	df = pd.DataFrame(lst).transpose()
	df.columns=['Name', 'Followers & others', 'Bio_Data', 'Profile_Link', 'Image URL']
	df.to_csv('C:\\Users\Ibad\PycharmProjects\Sellinium\profiles.csv')
	print("Data Stored Successfully...")


url_scrp()
table(nameslst, followerslst, biolst, linkslst, imglst)

driver.close()
