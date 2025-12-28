# this code will only work in python version before 3.12 because imaghdr is deleted in python 3.12

from instabot import Bot

bot = Bot()
#  to access account login into your insta account
bot.login(username = "*********", password = "**********")
# to follow write the username of the account you want to follow
bot.follow('username')
# to unfollow write the username of the account you want to follow
bot.unfollow('username')

# to post pic
bot.upload_photo('path of the photo', caption="write the caption")# while writing the path make sure to convert '\' to '/'
# to send message to other
bot.send_message("username")

# to see number of  followres
followers = bot.get_user_followers('usrname')
for follower in followers:
    print(bot.get_user_info(follower))

# similarly for followings
followings = bot.get_user_following('username')
for following in followings:
    print(bot.get_user_info(following))

