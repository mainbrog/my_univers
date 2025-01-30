import requests

# Hardcoded Token and User ID
TOKEN = '8196702827:AAHh849BNzI4wG6D4hxcPpYFTKquPh1-ZiE'
USER_ID = '7898211502'

# Telegram API URL
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def boss(text: str):
    """
    Sends a message to a specific Telegram user.

    Args:
        text (str): The message to be sent.
    """
    data = {
        'chat_id': USER_ID,
        'text': text
    }

    try:
        response = requests.post(API_URL, data=data)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

