from selenium import webdriver
import time


# Set my webdriver path
driver = webdriver.Chrome("C:/Users/shhd/Desktop/chromedriver.exe")

# Get Adress
driver.get("https://edlus.lmt.lv/")

# Get title
get_title = driver.title

# Display title
print(get_title)


# Check if title is = "LMT EDLUS"
if (get_title == "LMT EDLUS"):
    print("Ir!")
else:
    print("Nav!")

# Navigate to funkcijas
elem = driver.find_element_by_xpath(
    '//*[@id="menu-galvena-izvelne-1"]/li[4]/a')
elem.click()

time.sleep(2)


# Navigate to start page
driver.get("https://edlus.lmt.lv/")

time.sleep(2)

# Set btn
btn1 = driver.find_element_by_xpath(
    '//*[@id="edlus"]/section/article/div/div[1]/div/a[1]')

# Check if btn is displayed
if btn1:
    time.sleep(2)
    # Navigate to start page
    driver.get("https://bizness.lmt.lv/lv/biznesa-pakalpojuma-anketa?pageId=933&type=konsultacija&hideheader=1&hidefooter=1&eldus=1")

    time.sleep(3)

    driver.find_element_by_xpath(
        '//*[@id="companyId2"]').send_keys("Test")

    time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="nameId2"]').send_keys("Test")

    time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="surnameId2"]').send_keys("Test")

    time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="phoneId2"]').send_keys("827392713")

    time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="emailId2"]').send_keys("test@test.lv")

    time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="commentId2"]').send_keys("kdjkadkhalksjdkljalsdjljasldjalsjdlkasjdlkjasldjalksdjlajslkdjlaskjdlkajsdlkajsdlkajsdlkjalksdlasjdkjh")

    time.sleep(2)

    checkBox = driver.find_element_by_xpath(
        '//*[@id="checkbox-atruna"]')

    driver.execute_script("arguments[0].click();", checkBox)

    time.sleep(2)

    submit = driver.find_element_by_xpath(
        '//*[@id="popupBtn2"]')

    submit.click()


else:
    print("Button is not displayed")
