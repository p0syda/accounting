from application.salary import calculate_salary
from application.db import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(f"Current date: {datetime.now()}")
    calculate_salary()
    get_employees()
