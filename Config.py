import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21091579"))
    API_HASH = os.environ.get("API_HASH", "138584f91574f64630d01d24770a4a4c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5972186104:AAEkAYTFEmoa9cmD43ObdJNLz87K3JwQQTw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGYBu2pMfA44243nMiLd-_wd_om_GAadJKPS4dtx5h0NhIqrnh77ngIgxRuyeOfHYAjODxxVAfQZJ6Uq-P9jkBF3CTKEQMemWrCMxgdFhJx5NDG5VIazyx4VBjIhbgRQqk_-ThpaMvpvrIOfdwK1uO5IqgtNDgkc9LVuH4LQ2YNYb4_m2CRwwhf3KfRh_LLKLlx-YGNL2kW-WJ1ocIGo5uAJFJtf_7DuCb8uqcviWGygxtcrHiFUSnEOLtq89J_WMd-exid1ulIu8kBUFhH_4MU3uQKFVGsSAHdAFLHdx9DZr87ptYZSFtyTq9pPxmpxZf0SuDBcoUNIrh5xLkNrqToryEI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "iBranzyRobot")
    SUPPORT = os.environ.get("SUPPORT", "t.me/+A8Io2ywT-DAwZWI1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Stigmaken") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5411346689")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
