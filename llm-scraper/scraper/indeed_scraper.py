import os
import pdb
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"http://www.indeed.com/jobs?q={position}&l={location}&start={start}&vjk=67f4c335f087a0eb")
    driver.find_element(By.TAG_NAME, 'html')
    return driver.page_source

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  pass

def extract_text_from_card(card):
  text_elements = card.find_all(string = True)
  cleaned_elements = [element.strip() for element in text_elements if element.strip()]
  elements = [element for element in cleaned_elements if not element.startswith('.css')]
  return elements

def get_id_from(card):
  pass

def get_card_info(card):
  pass

def get_card_infos(cards):
  pass

def build_text(card_infos):
  pass

def retrieve_text(position, location, idx):
  cards = get_job_cards(position = position, location = location, start = idx)
  card_infos = get_card_infos(cards)
  combined_text = build_text(card_infos)
  return combined_text
  
def write_to_file(text, position, location, idx = 0, directory = '../data/text_docs'):
  full_dir = directory_name_builder(position, location, directory)
  filename = f'{full_dir}/results_{idx}.txt'.replace(' ', '_').lower()
  if not os.path.exists(full_dir):
    os.makedirs(full_dir)
  with open(filename, 'w') as file:
    file.write(text)
  return filename
    
def retrieve_and_write(position, location, idx, directory = '../text_docs'):
  
  combined_text = retrieve_text(position, location, idx)
  file_name = write_to_file(combined_text, position, location, idx, directory)
  return file_name

def retrieve_and_write_pages(position, location, pages = 5):
  step_size = 15
  file_names = []
  
  for i in range(0, pages*step_size, step_size):
    
    file_name = retrieve_and_write(position, location, i)
    file_names.append(file_name)
  return file_names
  

def directory_name_builder(position, location, directory = '../data/text_docs', date = 'today'):
  pass
