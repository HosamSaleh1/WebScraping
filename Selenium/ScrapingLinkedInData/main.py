import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import parameters
from parsel import Selector
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/")

username = driver.find_element_by_class_name('login-email')
username.send_keys(parameters.linkedin_username)
sleep(0.5)
password = driver.find_element_by_class_name('login-password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)
log_in_button = driver.find_element_by_class_name('login-submit')
log_in_button.click()

writer = csv.writer(open(parameters.file_name, 'wb', encoding = 'utf-8'))

writer.writerow(['Name','Job Title','Company','College','Location','URL'])

driver.get('https://www.google.com/')

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)
search_query.send_keys(keys.RETURN)
sleep(3)

linkedin_urls = driver.find_element_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

driver.quit()

driver.get("https://www.linkedin.com/in/pauljgarner")

driver.page_source

linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    sleep(5)
    sel = Selector(text=driver.page_source)

    name = sel.xpath('//*[startswith(@class, "pv-top-card-section__name")]/text()').extract_first
    if name:
        name = name.strip()
    else:
        name = 'N/A'
    job_title = sel.xpath('//*[startswith(@class, "pv-top-card-section__headline")]/text()').extract_first()
    if job_title:
        job_title = job_title.strip()
    else:
        job_title = 'N/A'
    company = sel.xpath('//*[startswith(@class, "pv-top-card-section__company-name")]/text()').extract_first()
    if company:
        company = company.strip()
    else:
        company = 'N/A'
    college = sel.xpath('//*[startswith(@class, "pv-top-card-section__college-name")]/text()').extract_first()
    if college:
        college = college.strip()
    else:
        college = 'N/A'
    location = sel.xpath('//*[startswith(@class, "pv-top-card-section__location")]/text()').extract_first()
    if location:
        location = location.strip()
    else:
        location = 'N/A'

    linkedin_url = driver.current_url
    if linkedin_url:
        pass
    else:
      linkedin_url = 'N/A'
    print(name)
    con = ['Name: 'name, 'Job Title: 'job_title, 'Company: 'company, 'College: 'college, 'Location: 'location, 'URL: 'linkedin_url,'\n']
    print(con)
    writer.writerow(con)

driver.quit()
