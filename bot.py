import os
import datetime
from lunarcalendar import Converter, Solar
from telegram import Bot

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

bot = Bot(token=TELEGRAM_TOKEN)

def is_lunar_1_or_15(date):
    lunar_date = Converter.Solar2Lunar(Solar(date.year, date.month, date.day))
    return lunar_date.day in [1, 15], lunar_date.day

def run():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=7)  # Giờ VN
    today = now.date()
    tomorrow = today + datetime.timedelta(days=1)

    is_tomorrow_special, lunar_day = is_lunar_1_or_15(tomorrow)
    if is_tomorrow_special:
        bot.send_message(chat_id=CHAT_ID, text=f"🔔 Ngày mai là mùng {lunar_day} âm lịch!")

    is_today_special, lunar_day = is_lunar_1_or_15(today)
    if is_today_special and now.hour < 8:
        bot.send_message(chat_id=CHAT_ID, text=f"🌕 Hôm nay là mùng {lunar_day} âm lịch!")

if __name__ == "__main__":
    run()
