import requests
from flask import Flask, render_template, request

app = Flask(__name__)


# Replace with your Telegram Bot Token and Chat ID
BOT_TOKEN = '7817538360:AAGBPHfM8yYQDwgVIEflafwRutW542m_JWU'
CHAT_ID = '6688651029'

# Telegram API URL
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Function to send the IP address to the Telegram bot
def send_ip_to_telegram(ip_address):
    message = f"New visitor IP: {ip_address}"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(TELEGRAM_URL, data=payload)

# Route for the website
@app.route('/')
def home():
    # Get the user's IP address from the request
    user_ip = request.remote_addr
    
    # Send the IP address to Telegram
    send_ip_to_telegram(user_ip)
    
    # Render the HTML page with the IP address
    return render_template('index.html', ip_address=user_ip)

if __name__ == '__main__':
    app.run(debug=True)
