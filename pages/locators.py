from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".header_user_info.login")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart > a")


class LoginPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#SubmitCreate")
    EMAIL_CREATE = (By.CSS_SELECTOR, "#email_create")
    EMAIL_ENTER = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")


class CreateUserPage:
    # Your personal information
    RADIO_BTN_MALE = (By.CSS_SELECTOR, "#uniform-id_gender1")
    RADIO_BTN_FEMALE = (By.CSS_SELECTOR, "#uniform-id_gender2")
    FIELD_PERSONAL_FIRST_NAME = (By.CSS_SELECTOR, "#customer_firstname")
    FIELD_PERSONAL_LAST_NAME = (By.CSS_SELECTOR, "#customer_lastname")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#passwd")
    DRP_DWN_LST_DAY_OF_BIRTH = (By.CSS_SELECTOR, "#days")
    DRP_DWN_LST_MONTH_OF_BIRTH = (By.CSS_SELECTOR, "#months")
    DRP_DWN_LST_YEAR_OF_BIRTH = (By.CSS_SELECTOR, "#years")
    CHECKBOX_NEWSLETTER = (By.CSS_SELECTOR, "#newsletter")
    CHECKBOX_OFFERS = (By.CSS_SELECTOR, "#optin")
    # Your address
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "#firstname")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "#lastname")
    FIELD_COMPANY = (By.CSS_SELECTOR, "#company")
    FIELD_ADDRESS_ONE = (By.CSS_SELECTOR, "#address1")
    FIELD_ADDRESS_TWO = (By.CSS_SELECTOR, "#address2")
    FIELD_CITY = (By.CSS_SELECTOR, "#city")
    DRP_DWN_LST_STATE = (By.CSS_SELECTOR, "#id_state")
    FIELD_ZIP = (By.CSS_SELECTOR, "#postcode")
    DRP_DWN_LST_COUNTRY = (By.CSS_SELECTOR, "id_country")
    FIELD_ADD_INFORM = (By.CSS_SELECTOR, "#other")
    FIELD_HOME_PHONE = (By.CSS_SELECTOR, "#phone")
    FIELD_MOBILE_PHONE = (By.CSS_SELECTOR, "#phone_mobile")
    FIELD_ALIAS = (By.CSS_SELECTOR, "#alias")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#submitAccount")
