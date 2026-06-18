from dotenv import load_dotenv
import os

load_dotenv()
class config_clima:
    OPENWEATHER_API_KEY = os.getenv("API_KEY")
 

MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

DATABASE_CONNECTION_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"