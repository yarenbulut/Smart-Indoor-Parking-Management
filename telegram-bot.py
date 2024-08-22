import asyncio
import psutil #Sistem kaynak kullanımlarını takip etmek için kullandığımız kütüphane.
from telegram import Bot

#Sistem kaynaklarının uyarı eşiği
CPU_USAGE = 70
MEMORY_USAGE = 71
DISK_USAGE = 73

bot_token = ""
chat_id = ""

bot = Bot(bot_token)

async def check_system_load():
    while True:
        cpu_usage = psutil.cpu_percent() #CPU kullanım yüzdesi takibi
        memory_usage = psutil.virtual_memory().percent #Bellek kullanım yüzdesi takibi
        disk_usage = psutil.disk_usage('/khas').percent #Disk kullanım yüzdesi takibi. /khas dizini üzerindeki kullanımı takip ediyoruz.

        if cpu_usage > CPU_USAGE or memory_usage > MEMORY_USAGE or disk_usage > DISK_USAGE: #Belirtilen eşik üstüne çıkıp çıkmadığını kontrol eden blok
            message = f"High Load Warning! CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%, Disk usage: {disk_usage}%"
            await bot.send_message(chat_id=chat_id, text=message)

        await asyncio.sleep(60)#Kaç saniyede bir kontrol edileceğinin belirlendiği kod.

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_system_load())
