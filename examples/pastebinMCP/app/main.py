import sys
from dotenv import load_dotenv
from mcp.server import FastMCP

import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 
from app.modules.helpers import getEnv
from app.modules.pastebin import PastebinWrapper

load_dotenv()

api_key = getEnv("API_DEV_KEY")
user_key = getEnv("API_USER_KEY")

mcp = FastMCP("Personal MCP Tools")

# Create an instance of the PastebinWrapper class
pastebin = PastebinWrapper(
    api_key=api_key,
    user_key=user_key
)

@mcp.tool(
    name="Pastebin Paste Creation Tool",
    description="pastebin_create_paste",
)
def pastebin_create_paste(
    text: str,
    title: str = "Untitled",
    privacy: int = 0
) -> str:
    try:
        paste_url = pastebin.create_paste(
            text=text,
            title=title,
            privacy=privacy
        )
        return "Created paste with URL: " + paste_url
    except Exception as e:
        return f"A exeception ocurred: {e}"

@mcp.tool(
    name="Pastebin User Info",
    description="get_user_info",
)
def pastebin_userinfo() -> str:
    try:
        userinfo = pastebin.get_userinfo()
        if userinfo.get('user'):
            userinfo = userinfo['user']
        else:
            return "User not found"
        
        return f"""
        Api Key: {api_key}
        User Key: {user_key}
        Username: {userinfo.get('user_name', 'N/A')}
        Email: {userinfo.get('user_email', 'N/A')}
        Account Type: {userinfo.get('user_account_type', 'N/A')} [0=Normal, 1=Pro, N/A=Empty]
        Pro Expiration: {userinfo.get('user_expiration', 'N/A')} [N=Never, N/A=Empty]
        """
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')