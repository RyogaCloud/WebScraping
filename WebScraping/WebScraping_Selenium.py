from selenium import webdriver
import time
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import sys
import os

args = sys.argv
root_query = input("キーワードを入力してください：　")
browser = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
columns = []