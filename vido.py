from CHRLINE import *


app = "CHROMEOS"
try:
    with open("token.txt","r") as z:
        token = z.read()
        bot = CHRLINE(token, device=app)
except:
	bot = CHRLINE(device=app)
print(f"AuthToken: {bot.authToken}")
video_path = input("Video Path:")
image_path = input("Image Path:")
bot.updateProfileImage(video_path)
bot.updateProfileImage(image_path, type='vp')
print("ok.")