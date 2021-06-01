from selenium import webdriver
from selenium.webdriver.firefox.options import Options



class FindElements7():
    def test(self):
        print("Case IV")
        options = Options()
        options.binary_location = r'C:\Users\Home\AppData\Local\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Users\Home\Desktop\Testassignment\Selenium\geckodriver.exe', options=options)

        baseUrl = "http://automationpractice.com/index.php"

        #driver.maximize_window()

        driver.get(baseUrl)
        currentUrl = driver.current_url
        title = driver.title
        driver.implicitly_wait(10)

        #1
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on main page")
            print("Page url: " + currentUrl + " and title: " + title)

        womenCatLink = driver.find_element_by_xpath("//li[@class='last']//a[contains(text(),'Women')]")
        womenCatLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #2
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Women categories page")
            print("Page url: " + currentUrl + " and title: " + title)


        specialsInfLink = driver.find_element_by_xpath("//a[contains(text(),'Specials')]")
        specialsInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #3
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Specials information page")
            print("Page url: " + currentUrl + " and title: " + title)


        newProductsInfLink = driver.find_element_by_xpath("//a[contains(text(),'New products')]")
        newProductsInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #4
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on New products information page")
            print("Page url: " + currentUrl + " and title: " + title)


        bestSellersInfLink = driver.find_element_by_xpath("//a[contains(text(),'Best sellers')]")
        bestSellersInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #5
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Best sellers information page")
            print("Page url: " + currentUrl + " and title: " + title)


        ourStoresInfLink = driver.find_element_by_xpath("//a[contains(text(),'Our stores')]")
        ourStoresInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #6
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Our stores information page")
            print("Page url: " + currentUrl + " and title: " + title)


        contactUsInfLink = driver.find_element_by_xpath("//li[@class='item']//a[contains(text(),'Contact us')]")
        contactUsInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #7
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Contact us information page")
            print("Page url: " + currentUrl + " and title: " + title)


        termsInfLink = driver.find_element_by_xpath("//a[contains(text(),'Terms and conditions of use')]")
        termsInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #8
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Terms and conditions of use information page")
            print("Page url: " + currentUrl + " and title: " + title)


        aboutUsInfLink = driver.find_element_by_xpath("//a[contains(text(),'About us')]")
        aboutUsInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #9
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on About us information page")
            print("Page url: " + currentUrl + " and title: " + title)


        sitemapInfLink = driver.find_element_by_xpath("//a[contains(text(),'Sitemap')]")
        sitemapInfLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #10
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on Sitemap information page")
            print("Page url: " + currentUrl + " and title: " + title)


        myOrdersLink = driver.find_element_by_xpath("//a[contains(text(),'My orders')]")
        myOrdersLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #11
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on My Orders page")
            print("Page url: " + currentUrl + " and title: " + title)

        myCreditSlipsLink = driver.find_element_by_xpath("//a[contains(text(),'My credit slips')]")
        myCreditSlipsLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #12
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on My credit slips page")
            print("Page url: " + currentUrl + " and title: " + title)

        myAddressesLink = driver.find_element_by_xpath("//a[contains(text(),'My addresses')]")
        myAddressesLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #13
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on My addresses page")
            print("Page url: " + currentUrl + " and title: " + title)

        myPersonalInfoLink = driver.find_element_by_xpath("//a[contains(text(),'My personal info')]")
        myPersonalInfoLink.click()
        currentUrl = driver.current_url
        title = driver.title

        #14
        siteLogo = driver.find_element_by_xpath("//img[@class='logo img-responsive']")
        if siteLogo is not None:
            print("+ Logo is present on My personal info page")
            print("Page url: " + currentUrl + " and title: " + title)

        driver.quit()








ff = FindElements7()

#ff.test()