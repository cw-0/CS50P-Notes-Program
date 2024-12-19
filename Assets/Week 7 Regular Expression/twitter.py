import re

url = input("What is your Profile URL: ").strip()

username = re.search(r"^https?://(?:www\.)?x\.com/([a-zA-Z0-9_]+)", url, re.I)
if username:
    print(f"Username: {username.group(1)}")




