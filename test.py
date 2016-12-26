from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Safari()
    driver.get('http://google.com')
    driver.find_element_by_css_selector(
        'input[name="q"]').send_keys("Hello, world!")
    driver.find_element_by_css_selector('input[type="submit"]').click()
