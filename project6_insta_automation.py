from instabot import Bot
bot=Bot()
bot.login(username="your_username",password="Your_password")
bot.follow("Account_name") 
bot.upload_photo("Path_of_the_photo/name_of_photo.jpg","caption="Captions_place")
bot.unfollow("Account_name")
#we can send messages to mutlitple account by the following methods:
bot.send_message("Hola como estas, Mi muy bien, tu ere bonito y yo amo es",["account_name","account_name"])
followers= bot.get_user_followers("Your_account_name")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_followinng("your_account_name")
for follwin in following:
    print(bot.get_user_info(follwin))