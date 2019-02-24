from selenium import webdriver
import unittest, time


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"
        #后台静默运行
        # chrome_options = webdriver.ChromeOptions("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(chrome_options=chrome_options)
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()