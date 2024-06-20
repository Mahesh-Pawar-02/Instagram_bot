import time
from instabot import Bot

def login(bot, username, password):
    bot.login(username=username, password=password)

def send_message_with_retry(bot, message, recipients, max_retries=5, delay=300):
    retries = 0
    while retries < max_retries:
        try:
            bot.send_message(message, recipients)
            print("Message sent successfully!")
            return True
        except Exception as e:
            if "429" in str(e):
                print("Rate limit exceeded. Waiting for 5 minutes before retrying...")
                time.sleep(delay)  # Wait for 5 minutes (300 seconds)
                retries += 1
            else:
                print(f"An error occurred: {e}")
                time.sleep(delay)  # Wait for 5 minutes before retrying for other errors as well
                retries += 1
    print("Max retries reached. Failed to send message.")
    return False

def main():
    bot = Bot()
    username = 'official_mahesh_02'
    password = '--------'
    recipient_username = '---------'
    message = 'Hello, this is a message sent using instabot!'

    login(bot, username, password)
    if bot.api.is_logged_in:
        print("Login successful!")
        success = send_message_with_retry(bot, message, [recipient_username])
        if success:
            print("Message sent successfully after handling rate limits.")
        else:
            print("Failed to send message after retries.")
    else:
        print("Failed to log in.")
    bot.logout()

if __name__ == "__main__":
    main()
