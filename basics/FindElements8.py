from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time



class FindElements8():
    def test(self):
        print("Cases VI-VIII")
        options = Options()
        options.binary_location = r'C:\Users\Home\AppData\Local\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Users\Home\Desktop\Testassignment\Selenium\geckodriver.exe', options=options)

        baseUrl = "http://automationpractice.com/index.php"

        #driver.maximize_window()

        driver.get(baseUrl)
        driver.implicitly_wait(10)



        searchField = driver.find_element_by_xpath("//input[@id='search_query_top']")
        searchField.click()
        searchField.send_keys("randomtext")

        searchSubmit = driver.find_element_by_xpath("//form[@id='searchbox']//button[@type='submit']")
        searchSubmit.click()

        nothingFound = driver.find_element_by_xpath("//p[contains(text(),'No results were found for your search')]")
        if nothingFound is not None:
            print("- Nothing found warning check passed")

        searchField = driver.find_element_by_xpath("//input[@id='search_query_top']")
        searchSubmit = driver.find_element_by_xpath("//form[@id='searchbox']//button[@type='submit']")

        searchField.clear()
        searchField.send_keys("Sleeve")
        searchSubmit.click()

        listItems = driver.find_element_by_xpath("//i[@class='icon-th-list']")
        listItems.click()


        addToCompare1 = driver.find_element_by_xpath("//li[@class='ajax_block_product first-in-line first-item-of-tablet-line first-item-of-mobile-line col-xs-12']//div[@class='product-container']//div[@class='row']//div[@class='right-block col-xs-4 col-xs-12 col-md-4']//div[@class='right-block-content row']//div[@class='functional-buttons clearfix col-sm-12']//div[@class='compare']//a[@class='add_to_compare'][contains(text(),'Add to Compare')]")
        if addToCompare1 is not None:
            print("+ Search is working")

        addToCompare1.click()
        time.sleep(2)


        addToCompare2 = driver.find_element_by_xpath("//li[@class='ajax_block_product last-item-of-tablet-line col-xs-12']//div[@class='product-container']//div[@class='row']//div[@class='right-block col-xs-4 col-xs-12 col-md-4']//div[@class='right-block-content row']//div[@class='functional-buttons clearfix col-sm-12']//div[@class='compare']//a[@class='add_to_compare'][contains(text(),'Add to Compare')]")
        addToCompare2.click()
        time.sleep(2)

        addToCompare3 = driver.find_element_by_xpath("//li[@class='ajax_block_product last-in-line first-item-of-tablet-line last-item-of-mobile-line col-xs-12']//div[@class='product-container']//div[@class='row']//div[@class='right-block col-xs-4 col-xs-12 col-md-4']//div[@class='right-block-content row']//div[@class='functional-buttons clearfix col-sm-12']//div[@class='compare']//a[@class='add_to_compare'][contains(text(),'Add to Compare')]")
        addToCompare3.click()
        time.sleep(2)

        addToCompare4 = driver.find_element_by_xpath("//li[@class='ajax_block_product first-in-line last-line last-item-of-tablet-line first-item-of-mobile-line last-mobile-line col-xs-12']//div[@class='product-container']//div[@class='row']//div[@class='right-block col-xs-4 col-xs-12 col-md-4']//div[@class='right-block-content row']//div[@class='functional-buttons clearfix col-sm-12']//div[@class='compare']//a[@class='add_to_compare'][contains(text(),'Add to Compare')]")
        addToCompare4.click()
        time.sleep(2)

        compareLimitError = driver.find_element_by_xpath("//p[@class='fancybox-error']")

        if compareLimitError is not None:
            print("- Compare item limit check passed")
            closeError = driver.find_element_by_xpath("//a[@class='fancybox-item fancybox-close']")
            closeError.click()

        time.sleep(2)
        compareButton = driver.find_element_by_xpath("//body[@id='search']/div[@id='page']/div[@class='columns-container']/div[@id='columns']/div[@class='row']/div[@id='center_column']/div[@class='content_sortPagiBar']/div[@class='bottom-pagination-content clearfix']/form[@class='compare-form']/button[@type='submit']/span[1]")
        compareButton.click()

        time.sleep(2)
        driver.set_window_size(340, 695)
        time.sleep(2)
        driver.save_screenshot("screenshot1_m.png")
        print("+ Screenshot for mobile ratio of Compare screen is captured")
        driver.maximize_window()
        time.sleep(2)
        driver.save_screenshot("screenshot1.png")
        print("+ Screenshot for full screen desktop ratio of Compare screen is captured")



        driver.quit()








ff = FindElements8()

#ff.test()