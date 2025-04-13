from appium import webdriver
import time
from config import desired_caps
from selenium.common.exceptions import NoSuchElementException

def setup_driver():
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    driver.implicitly_wait(20)
    return driver

def login(driver, username, password):
    # Tìm và nhập tên đăng nhập
    username_field = driver.find_element("xpath", "//android.widget.EditText[1]")
    username_field.clear()
    username_field.send_keys(username)

    # Tìm và nhập mật khẩu
    password_field = driver.find_element("xpath", "//android.widget.EditText[2]")
    password_field.clear()
    password_field.send_keys(password)

    # Tìm nút đăng nhập bằng content-desc
    login_button = driver.find_element("xpath", "//android.widget.Button[@content-desc='Đăng nhập']")
    login_button.click()

def test_login_success():
    try:
        driver = setup_driver()
        login(driver, "admin", "123456")
        time.sleep(3)
        print("✅ Test login success: PASSED - Đăng nhập thành công")
    except Exception as e:
        print(f"❌ Test login success: FAILED - {str(e)}")
    finally:
        driver.quit()

def test_login_wrong_password():
    try:
        driver = setup_driver()
        login(driver, "admin", "wrongpass")
        time.sleep(3)
        
        # Kiểm tra thông báo lỗi
        try:
            error_message = driver.find_element("xpath", "//android.widget.TextView[contains(@text, 'Sai mật khẩu')]")
            print("✅ Test login wrong password: PASSED")
        except NoSuchElementException:
            print("❌ Test login wrong password: FAILED - Không tìm thấy thông báo lỗi")
    except Exception as e:
        print(f"❌ Test login wrong password: FAILED - {str(e)}")
    finally:
        driver.quit()

def test_login_wrong_username():
    try:
        driver = setup_driver()
        login(driver, "wronguser", "123456")
        time.sleep(3)
        
        # Kiểm tra thông báo lỗi
        try:
            error_message = driver.find_element("xpath", "//android.widget.TextView[contains(@text, 'Tài khoản không tồn tại')]")
            print("✅ Test login wrong username: PASSED")
        except NoSuchElementException:
            print("❌ Test login wrong username: FAILED - Không tìm thấy thông báo lỗi")
    except Exception as e:
        print(f"❌ Test login wrong username: FAILED - {str(e)}")
    finally:
        driver.quit()

def test_login_empty_fields():
    try:
        driver = setup_driver()
        login(driver, "", "")
        time.sleep(3)
        
        # Kiểm tra thông báo lỗi
        try:
            error_message = driver.find_element("xpath", "//android.widget.TextView[contains(@text, 'Vui lòng nhập đầy đủ thông tin')]")
            print("✅ Test login empty fields: PASSED")
        except NoSuchElementException:
            print("❌ Test login empty fields: FAILED - Không tìm thấy thông báo lỗi")
    except Exception as e:
        print(f"❌ Test login empty fields: FAILED - {str(e)}")
    finally:
        driver.quit()

def run_all_tests():
    print("=== Bắt đầu chạy test cases ===")
    test_login_success()  # Test case đăng nhập đúng
    test_login_wrong_password()
    test_login_wrong_username()
    test_login_empty_fields()
    print("=== Kết thúc test cases ===")

if __name__ == "__main__":
    run_all_tests()
