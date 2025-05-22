import logging
import requests
import xmltodict

logger = logging.getLogger(__name__)

class PastebinWrapper:
  __BASEURL = "https://pastebin.com/api"
  __API_DEV = None
  __USER_DEV = None
  def __init__(self, api_key: str | None, user_key: str | None):
    self.__API_DEV = api_key
    self.__USER_DEV = user_key

  def get_userinfo(self):
    logger.info("Getting user info...")

    response = requests.post(
      url=f"{PastebinWrapper.__BASEURL}/api_post.php",
      data={
        'api_dev_key': self.__API_DEV,
        'api_user_key': self.__USER_DEV,
        'api_option': 'userdetails'
      }
    )

    if response.status_code != 200:
      raise Exception(f"Error: {response.status_code} - {response.text}")

    userinfo_dict = xmltodict.parse(response.text)
    
    logger.info(f"User info: {userinfo_dict}")

    return userinfo_dict

  def create_paste(self, text: str, title: str = "Untitled", privacy: int = 0):
    logger.info(f"Creating paste with title '{title}'...")

    response = requests.post(
      url=f"{PastebinWrapper.__BASEURL}/api_post.php",
      data={
        'api_dev_key': self.__API_DEV,
        'api_user_key': self.__USER_DEV,
        'api_option': 'paste',
        'api_paste_expire_date': '10M',
        'api_paste_code': text,
        'api_paste_name': title,
        'api_paste_private': privacy
      }
    )

    if response.status_code != 200:
      raise Exception(f"Error: {response.status_code} - {response.text}")

    logger.info(f"Paste created with URL: {response.text}")

    return response.text
  @staticmethod
  def generate_userkey(
    api_key: str,
    username: str,
    password: str
  ):

    logger.info(f"Generating user key for {username}...")

    response = requests.post(
      url=f"{PastebinWrapper.__BASEURL}/api_login.php",
      data={
      'api_dev_key': api_key,
      'api_user_name': username,
      'api_user_password': password,
      }
    )

    if response.status_code != 200:
      raise Exception(f"Error: {response.status_code} - {response.text}")
    
    logger.info(f"User key {response.text} generated for {username}.")

    return response.text
