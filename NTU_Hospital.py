from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

web = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")
#web.get("https://reg.ntuh.gov.tw/webadministration/DoctorServiceQueryByDrName.aspx?HospCode=T0&QueryName=%E6%9B%BE%E5%85%86%E9%BA%9F")

web.get("https://reg.ntuh.gov.tw/webadministration/DoctorServiceQueryByDrName.aspx?HospCode=T0&QueryName=%E4%BD%95%E5%AD%90%E6%98%8C")

while True:
    try:
        date=web.find_element_by_xpath("//*[@id='DoctorServiceListInSeveralDaysInput_GridViewDoctorServiceList__ctl8_AdminTextShow']")  
        date.click()
        break
    except :
        web.refresh();
        time.sleep(0.5)
        
ID=web.find_element_by_id("radInputNum")
ID.click()

IDBOX=web.find_element_by_id("txtIdno")
IDBOX.send_keys("L221900561")

YEARSELECT=Select(web.find_element_by_name('ddlBirthYear'))
YEARSELECT.select_by_value("1963")

MONTHSELECT=Select(web.find_element_by_name('ddlBirthMonth'))
MONTHSELECT.select_by_value("12")

DAYSELECT=Select(web.find_element_by_name('ddlBirthDay'))
DAYSELECT.select_by_value("03")
