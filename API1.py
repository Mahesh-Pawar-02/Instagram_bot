from instabot import Bot

bot = Bot()
username = 'official_mahesh_02'
password = '--------'
bot.login(username=username, password=password)

recipient_username = '--------'
message = 'Hello, this is a message sent using automation!'

try:
    bot.send_message(message, [recipient_username])
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred.: {e}")

bot.logout()
