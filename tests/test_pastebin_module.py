from app.modules.pastebin import PastebinWrapper
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(
  level=logging.INFO,
  filename='tests.log',
  filemode='w',
)

def test_get_userinfo():
  api_key = os.getenv("PASTEBIN_DEV_APIKEY")
  user_key = os.getenv("PASTEBIN_USER_APIKEY")

  assert api_key is not None, "PASTEBIN_DEV_APIKEY is not set in .env"
  assert user_key is not None, "PASTEBIN_USERKEY is not set in .env"

  pastebin = PastebinWrapper(api_key, user_key)
  user_info = pastebin.get_userinfo()

  assert user_info is not None, "Failed to get user info"

def test_userkey_generation(caplog):
  caplog.set_level(logging.INFO)
  api_key = os.getenv("PASTEBIN_DEV_APIKEY")
  username = os.getenv("PASTEBIN_USERNAME")
  password = os.getenv("PASTEBIN_PASSWORD")

  assert api_key is not None, "PASTEBIN_DEV_APIKEY is not set in .env"
  assert username is not None, "PASTEBIN_USERNAME is not set in .env"
  assert password is not None, "PASTEBIN_PASSWORD is not set in .env"

  user_api_key =  PastebinWrapper.generate_userkey(api_key, username, password)
  
  assert user_api_key is not None, "Failed to generate user key"