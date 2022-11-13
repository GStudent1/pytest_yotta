pytest -s test_case/test_eoy_main_page.py
allure generate   ./allure-report/xml -o ./allure-report/html  --clean
