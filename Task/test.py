import time
import pytest
from testpage import OperationHelper


username = "ElenaIvan"
password = "b0f5c4418d"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("ElenaIvan")
    test_page1.enter_pswd("b0f5c4418d")
    test_page1.click_button()
    time.sleep(3)
  
    test_page1.click_contact()
    time.sleep(3)
    
    test_page1.enter_cont_name("Elena")
    test_page1.enter_cont_email("mail@mail.ru")
    test_page1.enter_cont_text("Hello world!")
    time.sleep(1)
    
    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"