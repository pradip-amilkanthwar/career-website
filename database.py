import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

DB_USERNAME = 'postgres'
DB_PASSWORD = '@Milkanthwar12'
DB_HOST = 'localhost'
DATABASE = 'flask_db'

def get_db_connection():
    conn = psycopg2.connect(host=f'{DB_HOST}',
                            database=f'{DATABASE}',
                            user=f'{DB_USERNAME}',
                            password=f'{DB_PASSWORD}')
    return conn


