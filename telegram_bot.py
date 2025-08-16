import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ==============================================================================
# ➤➤➤ আপনার বটের টোকেন এখানে যুক্ত করবেন না! 
#      এটি Render-এর Environment Variable-এ সেট করতে হবে।
# ==============================================================================
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# ==============================================================================
# ➤➤➤ আপনার নির্দিষ্ট ওয়েবসাইটের ভিডিও লিঙ্কগুলো এখানে যোগ করুন
#      নিচের উদাহরণগুলো মুছে আপনার নিজের লিঙ্কগুলো এখানে পেস্ট করুন।
#      লিঙ্কগুলো অবশ্যই সরাসরি ভিডিও ফাইলের লিঙ্ক হতে হবে (যেমন: .mp4)।
# ==============================================================================
VIDEO_URLS = [
    "https://your-website.com/videos/video1.mp4",
    "https://your-website.com/videos/video2.mp4",
    "https://another-site.com/media/video3.mp4",
    # এখানে যত খুশি ভিডিও লিঙ্ক যোগ করতে পারেন
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """যখন কোনো ব্যবহারকারী /start কমান্ড দেবে, এই ফাংশনটি কাজ করবে।"""
    user = update.effective_user
    chat_id = update.effective_chat.id

    await update.message.reply_html(
        f"হ্যালো {user.mention_html()}! 👋\n\nআপনার জন্য একটি ভিডিও পাঠানো হচ্ছে, অনুগ্রহ করে অপেক্ষা করুন...",
    )

    try:
        # ভিডিও তালিকা থেকে র‍্যান্ডমভাবে একটি ভিডিও লিঙ্ক বেছে নেওয়া হচ্ছে
        if VIDEO_URLS:
            video_url = random.choice(VIDEO_URLS)
            # ব্যবহারকারীকে ভিডিও পাঠানো হচ্ছে
            await context.bot.send_video(chat_id=chat_id, video=video_url)
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text="দুঃখিত, ভিডিওর তালিকায় কোনো লিঙ্ক খুঁজে পাওয়া যায়নি।"
            )

    except Exception as e:
        # যদি কোনো কারণে ভিডিও পাঠাতে সমস্যা হয়
        print(f"Error sending video: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
            text="দুঃখিত, এই মুহূর্তে ভিডিওটি পাঠাতে সমস্যা হচ্ছে।"
        )

def main() -> None:
    """বটটি চালু করার জন্য মূল ফাংশন।"""
    if not BOT_TOKEN:
        print("🔴 Error: TELEGRAM_BOT_TOKEN এনভায়রনমেন্ট ভ্যারিয়েবল সেট করা নেই!")
        return

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()