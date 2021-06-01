from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random



class FindElements6():
    def test(self):
        print("Cases I-III")
        options = Options()
        options.binary_location = r'C:\Users\Home\AppData\Local\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Users\Home\Desktop\Testassignment\Selenium\geckodriver.exe', options=options)

        baseUrl = "http://automationpractice.com/index.php"

        #driver.maximize_window()

        driver.get(baseUrl)
        driver.implicitly_wait(10)

        randomNumberForEmail = str(random.randint(16, 1000))

        input = driver.find_element(By.XPATH, "//input[@id='newsletter-input']")

        input.click()

        input.send_keys("test")

        submit = driver.find_element_by_xpath("//div[@class='footer-container']//button[@type='submit']")

        submit.click()


        invalidEmail = driver.find_element_by_xpath("//p[contains(text(),'Newsletter : Invalid email address.')]")

        if invalidEmail is not None:
            print("- Invalid email check completed")


        input = driver.find_element(By.XPATH, "//input[@id='newsletter-input']")
        submit = driver.find_element_by_xpath("//div[@class='footer-container']//button[@type='submit']")

        input.click()
        input.clear()
        input.send_keys("trueapp" + randomNumberForEmail + "@gmail.com")
        submit.click()

        successText = driver.find_element_by_xpath("//p[@class='alert alert-success']")

        if successText is not None:
            print("Subscription completed successful to email: trueapp" + randomNumberForEmail + "@gmail.com")
            print("+ Subscription check completed")

        input = driver.find_element(By.XPATH, "//input[@id='newsletter-input']")
        submit = driver.find_element_by_xpath("//div[@class='footer-container']//button[@type='submit']")

        input.click()
        input.clear()
        input.send_keys("trueapp" + randomNumberForEmail + "@gmail.com")
        submit.click()

        usedEmail = driver.find_element_by_xpath("//p[contains(text(),'Newsletter : This email address is already registered.')]")

        if usedEmail is not None:
            print("Email address is already registered.")
            print("- Negative check for used email completed")




        driver.quit()








ff = FindElements6()

#ff.test()