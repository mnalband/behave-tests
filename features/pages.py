import attr
from selenium import webdriver


@attr.s
class MainPage:
    driver: webdriver.remote.webdriver.WebDriver = attr.ib()

    def get_title(self):
        return self.driver.title

    def get_first_number_element(self):
        return self.driver.find_element_by_id("a")

    def get_first_number(self):
        return self.get_first_number_element().get_attribute("value")

    def get_second_number_element(self):
        return self.driver.find_element_by_id("b")

    def get_second_number(self):
        return self.get_second_number_element().get_attribute("value")

    def get_result_element(self):
        return self.driver.find_element_by_id("r")

    def get_result(self):
        return self.get_result_element().get_attribute("value")

    def get_operator_element(self):
        return self.driver.find_element_by_id("operator")

    def get_operator(self):
        return self.get_operator_element().text

    def get_submit_element(self):
        return self.driver.find_element_by_id("submit")

    def get_ruler_element(self):
        return self.driver.find_element_by_class_name("rulercontainer")

    def get_ruler_value_element(self):
        return self.driver.find_element_by_id("rulervalue")

    def get_ruler_value(self):
        return self.get_ruler_value_element().text

    def get_ruler_more(self):
        return self.driver.find_element_by_class_name("more")

    def get_ruler_less(self):
        return self.driver.find_element_by_class_name("less")

    def get_ruler_start(self):
        return self.driver.find_element_by_class_name("rulerstart")

    def get_ruler_continue(self):
        return self.driver.find_elements_by_class_name("rulercont")

    def get_operation_result_element(self):
        return self.driver.find_element_by_css_selector(".showresult img")

    def get_good_result(self):
        return self.driver.find_element_by_id("good")

    def get_bad_result(self):
        return self.driver.find_element_by_id("bad")
