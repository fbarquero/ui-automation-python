#!/usr/bin/python
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from nose.plugins.attrib import attr


@attr('all')
class TestPythonOrgSearch(TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org_1(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.get_screenshot_as_file("screenshot.png")
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_2(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.get_screenshot_as_file("screenshot.png")
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_3(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.get_screenshot_as_file("screenshot.png")
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_4(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.get_screenshot_as_file("screenshot.png")
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_5(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.get_screenshot_as_file("screenshot.png")
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.quit()
