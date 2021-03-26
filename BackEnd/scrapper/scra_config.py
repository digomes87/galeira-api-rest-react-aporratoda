from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

DIRECTORY       = 'reports'
CATEGORIES      = ['PS', 'TV','Iphone', 'smarttv', 'Lego', 'printer','pc', 'computer', 'notebook']
CURRENCY        = '$'
BASE_URL        = "https://www.amazon.com"
API_BASE_URL    = 'https://127.0.0.1:8000/'

def get_chrome_web_driver(options):
    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_automation_as_head_less(options):
    options.add_argument('--headless')
