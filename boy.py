import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Telegram bot tokeninizi buraya daxil edin
TOKEN = '7621341828:AAGtJ2Ee2m1xfhFGofuZqR1q-hrdZgeoMpg'

# Logging konfiqurasiyası
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# İstifadəçinin mesajlarına əsaslanan cavab funksiyası
def echo(update: Update, context: CallbackContext) -> None:
    # Gələn mesajı alın
    user_message = update.message.text
    
    # Mesajı loga yazın
    logger.info(f"Received message: {user_message}")
    
    # Bu hissə burada sadə bir cavab verilir, amma bunu daha mürəkkəb hala gətirə bilərsiniz
    update.message.reply_text(f"Siz yazdınız: {user_message}")

# Komanda funksiyaları
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Salam! Mən sizin botunuzam. Mənə mesaj yaza bilərsiniz.")

# Əsas funksiya: Botu işə salır
def main():
    # Updater obyektini yaradın və tokeni daxil edin
    updater = Updater(TOKEN)
    
    # Dispatcher əldə et
    dispatcher = updater.dispatcher
    
    # Komanda handlerləri əlavə et
    dispatcher.add_handler(CommandHandler("start", start))
    
    # İstifadəçilərin mesajlarını idarə etmək üçün MessageHandler əlavə et
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # Botu başlat
    updater.start_polling()
    
    # Bot işlədikcə davam et
    updater.idle()

if __name__ == '__main__':
    main()
  
