from dotenv import load_dotenv
import os
 
load_dotenv()

PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE = os.getenv('PG_DATABASE')
PG_USER = 'postgres'
PG_PASSWORD = 'admin'
