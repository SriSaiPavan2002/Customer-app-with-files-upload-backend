import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://admin:1972@localhost:3306/customer_dashboard")
