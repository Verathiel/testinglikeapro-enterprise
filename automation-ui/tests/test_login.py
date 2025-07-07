from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    driver = webdriver.Chrome()  # nebo webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Najdeme pole pro uživatele a heslo
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    # Zadáme přihlašovací údaje
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    # Potvrdíme Enterem nebo kliknutím na tlačítko
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)  # počkáme na načtení stránky

    # Ověříme, že jsme na dashboardu (podle URL nebo elementu)
    assert "dashboard" in driver.current_url.lower() or "dashboard" in driver.page_source.lower()

    driver.quit()

if __name__ == "__main__":
    test_login()
