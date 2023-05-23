from rubpy import Client, handlers, models, methods
from aiohttp import ClientSession, ClientTimeout
from random import choice
from Api_DataTime import ___date____time
from asyncio import run, sleep
import aiofiles

my_group = 'g0CtNQQ008f829721933a69b9530950b'
my_filters = ('@', 'join', 'rubika.ir')
group_admins = []
silence_list = []
no_gifs = False
pasikh = False
welcome = False
GAME = False
shishe = False



my_insults = (
    'کیر',
    'کص',
    'کون',
    'کس ننت',
    'کوس',
    'کوص',
    'ممه',
    'ننت',
    'بی ناموس',
    'بیناموس',
    'بیناموص',
    'بی ناموص',
    'گایید',
    'جنده',
    'جندع',
    'جیندا',
    'پستون',
    'کسکش',
    'ننه کس',
    'اوبی',
    'هرزه',
    'قحبه',
    'عنتر',
    'فاک',
    'کسعمت',
    'کصخل',
    'کسخل',
    'تخمی',
    'سکس',
    'صکص',
    'کسخول',
    'کسشر',
    'کسشعر',
)

def getAds(string: str) -> bool:
    string = string.lower()
    for filter in my_filters:
        if filter in string:
            return True
        else:
            continue
    return False

def getInsults(string: str) -> bool:
    for filter in my_insults:
        if filter in string:
            return True
        else:
            continue
    return False

async def updateAdmins(client: Client) -> None:
    global group_admins
    results = await client(methods.groups.GetGroupAdminMembers(my_group))
    results = results.to_dict().get('in_chat_members')
    for result in results:
        GUID = result.get('member_guid')
        if not GUID in group_admins:
            group_admins.append(GUID)
        else:
            continue

async def main():
    async with ClientSession(timeout=ClientTimeout(5)) as CS:
        async with Client(session='MyBot') as client:
            await updateAdmins(client)
            @client.on(handlers.MessageUpdates(models.is_group()))
            async def updates(update):
                if update.object_guid == my_group:
                    if not update.author_guid in group_admins and 'forwarded_from' in update.to_dict().get('message').keys():
                        await client.ban_group_member(update.object_guid,update.author_guid)
                        await update.delete_messages()
                        await update.reply('شما به علت فوروارد از گروه ریم میشوید.')
                        print('Delete A Forward.')

                    if update.raw_text != None:
                        if not update.author_guid in group_admins and getAds(update.raw_text):
                            await client.ban_group_member(update.object_guid,update.author_guid)
                            await update.delete_messages()
                            await update.reply('شما به علت تبلیغات از گروه ریم میشوید.')
                            print('Delete A Link.')

                        elif getInsults(update.raw_text):
                            await update.delete_messages()
                            print('Delete A Insult.')

                        elif update.author_guid in group_admins and update.raw_text == '/OPEN' or update.raw_text == 'بازکردن گروه':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, ['SendMessages']))
                            await update.reply('گروه باز شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/CLOSE' or update.raw_text == 'قفل گروه':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, []))
                            await update.reply('گروه بسته شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن گیف' or update.raw_text == '/LOCKGIF':
                            global no_gifs
                            no_gifs = True
                            await update.reply('گیف باز شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'پاسخ گویی خاموش' or update.raw_text == '/PASOKHOF':
                            global pasikh
                            pasikh = False
                            await update.reply('پاسخگویی خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'خوش اومد گویی خاموش' or update.raw_text == '/WELCOMEOFF':
                            global welcome
                            welcome = False
                            await update.reply('خوش امد گویی خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل شیشه ای خاموش' or update.raw_text == '/OFFSHISHE':
                            global shishe
                            shishe = False
                            await update.reply('قفل شیشه ای خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل بازی روشن' or update.raw_text == '/ONGAME' or update.raw_text == 'قفل گیم روشن':
                            global GAME
                            GAME = False
                            await update.reply('قفل بازی خاموش شد.')

                        elif update.raw_text == '/ARZ' or update.raw_text == 'ارز':
                            await update.reply("""
                            ● دلار
• قیمت: 517,480 ریال
• به روزرسانی: ۳۱ اردیبهشت

● یورو
• قیمت: 560,620 ریال
• به روزرسانی: ۳۱ اردیبهشت

● درهم امارات 
• قیمت: 141,220 ریال
• به روزرسانی: ۳۱ اردیبهشت

● پوند انگلیس
• قیمت: 645,190 ریال
• به روزرسانی: ۳۱ اردیبهشت

● لیر ترکیه 
• قیمت: 26,200 ریال
• به روزرسانی: ۳۱ اردیبهشت

● فرانک سوئیس 
• قیمت: 576,900 ریال
• به روزرسانی: ۳۱ اردیبهشت

● یوان چین 
• قیمت: 73,700 ریال
• به روزرسانی: ۳۱ اردیبهشت

● ین ژاپن (100 ین) 
• قیمت: 374,220 ریال
• به روزرسانی: ۳۱ اردیبهشت

● وون کره جنوبی
• قیمت: 390 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دلار کانادا 
• قیمت: 385,000 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دلار استرالیا 
• قیمت: 344,700 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دلار نیوزیلند 
• قیمت: 325,100 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دلار سنگاپور 
• قیمت: 390,500 ریال
• به روزرسانی: ۳۱ اردیبهشت

● روپیه هند 
• قیمت: 6,260 ریال
• به روزرسانی: ۳۱ اردیبهشت

● روپیه پاکستان 
• قیمت: 1,819 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دینار عراق 
• قیمت: 404 ریال
• به روزرسانی: ۳۱ اردیبهشت

● پوند سوریه
• قیمت: 206 ریال
• به روزرسانی: ۳۱ اردیبهشت

● افغانی 
• قیمت: 5,890 ریال
• به روزرسانی: ۳۱ اردیبهشت

● کرون دانمارک 
• قیمت: 76,800 ریال
• به روزرسانی: ۳۱ اردیبهشت

● کرون سوئد 
• قیمت: 49,300 ریال
• به روزرسانی: ۳۱ اردیبهشت

● کرون نروژ 
• قیمت: 47,900 ریال
• به روزرسانی: ۳۱ اردیبهشت

● ریال عربستان 
• قیمت: 138,420 ریال
• به روزرسانی: ۳۱ اردیبهشت

● ریال قطر 
• قیمت: 142,500 ریال
• به روزرسانی: ۳۱ اردیبهشت

● ریال عمان 
• قیمت: 1,351,400 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دینار کویت 
• قیمت: 1,690,600 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دینار بحرین 
• قیمت: 1,385,300 ریال
• به روزرسانی: ۳۱ اردیبهشت

● رینگیت مالزی 
• قیمت: 114,100 ریال
• به روزرسانی: ۳۱ اردیبهشت

● بات تایلند 
• قیمت: 15,040 ریال
• به روزرسانی: ۳۱ اردیبهشت

● دلار هنگ کنگ 
• قیمت: 66,100 ریال
• به روزرسانی: ۳۱ اردیبهشت

● روبل روسیه 
• قیمت: 6,560 ریال
• به روزرسانی: ۳۱ اردیبهشت

● منات آذربایجان 
• قیمت: 305,900 ریال
• به روزرسانی: ۳۱ اردیبهشت

● درام ارمنستان 
• قیمت: 1,340 ریال
• به روزرسانی: ۳۱ اردیبهشت
                            """)

                        elif update.raw_text == 'دانستنی' or update.raw_text == '/DANSTANI':
                            async with CS.post('http://api.codebazan.ir/danestani/') as response:
                                await update.reply(await response.text())

                        elif update.raw_text == 'تاریخ' or update.raw_text == '/TIME':
                            async with CS.post('http://api.codebazan.ir/time-date/?td=all') as response:
                                await update.reply(await response.text())

                        elif update.raw_text == 'جوک' or update.raw_text == '/JOK':
                            path = choice(['jok', 'jok/khatere', 'jok/pa-na-pa', 'jok/alaki-masalan'])
                            async with CS.post(f'http://api.codebazan.ir/{path}/') as response:
                                await update.reply(await response.text())

                        elif update.raw_text == 'ذکر امروز' or update.raw_text == '/HADIS':
                            async with CS.post('http://api.codebazan.ir/zekr/') as response:
                                await update.reply(await response.text())

                        elif update.raw_text == 'حدیث' or update.raw_text == '/HADIS':
                            async with CS.post('http://api.codebazan.ir/hadis/') as response:
                                await update.reply(await response.text())

                        #LOCKS
                        elif update.author_guid in group_admins and update.raw_text == 'قفل گیم خاموش' or update.raw_text == '/lOCKG' or update.raw_text == 'قفل بازی خاموش':
                            GAME = True
                            await update.reply('قفل بازی خاموش شد.')
                            
                        elif update.author_guid in group_admins and update.raw_text == 'قفل گیف' or update.raw_text == '/UNLOCKGIF':
                            no_gifs = False
                            await update.reply('قفل گیف فعال شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'پاسخ گویی روشن' or update.raw_text == '/PASOKH' or update.raw_text == 'پاسخگویی روشن' or update.raw_text == 'سخنگو روشن' or update.raw_text == 'حالت سخنگو روشن':
                            pasikh = True
                            await update.reply('پاسخگویی روشن شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'خوش امد گویی روشن' or update.raw_text == '/WELCOME' or update.raw_text == 'حالت خوش اومد گویی روشن' or update.raw_text == 'خوش امدگویی روشن':
                            welcome = True
                            await update.reply('خوش امد گویی روشن شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل شیشه ای روشن' or update.raw_text == '/ONSHISHI':
                            shishe = True
                            await update.reply('قفل شیشه ای روشن شد.')

                        elif update.author_guid in group_admins and update.raw_text.startswith('سکوت'):
                            if update.reply_message_id != None:
                                try:
                                    result = await client(methods.messages.GetMessagesByID(my_group, [update.reply_message_id]))
                                    result = result.to_dict().get('messages')[0]
                                    if not result.get('author_object_guid') in group_admins:
                                        global silence_list
                                        silence_list.append(result.get('author_object_guid'))
                                        await update.reply('کاربر مورد نظر در حالت سکوت قرار گرفت.')
                                    else:
                                        await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                except IndexError:
                                    await update.reply('ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است.')
                            elif update.text.startswith('سکوت @'):
                                username = update.text.split('@')[-1]
                                if username != '':
                                    result = await client(methods.extras.GetObjectByUsername(username.lower()))
                                    result = result.to_dict()
                                    if result.get('exist'):
                                        if result.get('type') == 'User':
                                            user_guid = result.get('user').get('user_guid')
                                            if not user_guid in group_admins:
                                                #global silence_list
                                                silence_list.append(user_guid)
                                                await update.reply('کاربر مورد نظر در حالت سکوت قرار گرفت.')
                                            else:
                                                await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                        else:
                                            await update.reply('کاربر مورد نظر کاربر عادی نیست.')
                                    else:
                                        await update.reply('آیدی مورد نظر اشتباه است.')
                                else:
                                    await update.reply('آیدی مورد نظر اشتباه است.')
                            else:
                                await update.reply('روی یک کاربر ریپلای بزنید.')

                        elif update.author_guid in group_admins and update.raw_text.startswith('لیست سکوت خالی'):
                            if silence_list == []:
                                await update.reply('لیست سکوت خالی است.')
                            else:
                                silence_list = []
                                await update.reply('لیست سکوت خالی شد.')

                        elif update.raw_text == 'لینک':
                            result = await client(methods.groups.GetGroupLink(my_group))
                            result = result.to_dict().get('join_link')
                            await update.reply(f'لینک گروه:\n{result}')

                        elif update.raw_text == 'قوانین':
                            await update.reply("""
											📁• قوانین گروه •
📁• فحش و لینک ممنوع 
📁• توهین به کاربران و ادمین ها ممنوع
📁• تبلیغات ممنوع 
📁• دستورات مستهجن به ربات ممنوع
🗑• در صورت مشاهده و زیر پا گذاشتن قوانین فورا شما از گروه حذف میشوید!
=================================
جهت خرید ربات به ایدی زیر مراجعه کنید.
user ad Bot @User_Coder 👹""")

                        elif update.raw_text == 'پنل' or update.raw_text == '/PANEL' or update.raw_text == 'دستورات' or update.raw_text == '/panel':
                            await update.reply("""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/KARBORD လ کاربردی
 
/GAME လ بازی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")
                            
                        elif update.raw_text == '/BACK':
                            await update.reply("""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/KARBORD လ کاربردی

/GAME လ بازی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")
                            
                        elif update.raw_text == '/CONDITION' or update.raw_text == 'وضعیت':
                            await update.reply("""
											پلن یک ماهه برای شما فعال است |💠
											
											/BACK လ برگشت به منوی اصلی
											
                                            """)
                            
                        elif update.raw_text == '/GAME' or update.raw_text == 'بازی':
                            await update.reply("""
											💠 | 𝓖𝓐𝓜𝓔𝓢: 

/JRAT လ بازی جرعت حقیقت

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")
                            
                        elif update.raw_text == '/JRAT' or update.raw_text == 'بازی جرعت حقیقت':
                            await update.reply("""
											۱🔓عاشق شدی؟اسمش❤️
۲🔓رل زدی تاحالا؟اسمش
۳🔓کراش داری؟اسمش
۴🔓چند بار تا الان رابطه جنسی داشتی؟با کی😐💦
۵🔓از کی خوشت میاد؟
۶🔓از کی بدت میاد؟
۷🔓منو دوس داری؟بهم ثابت کن
۸🔓کی دلتو شکونده؟
۹🔓دل کیو شکوندی؟
۱۰🔓وقتی عصبانی هستی چجوری میشی؟
۱۱🔓دوس داری کیو بزنی یا بکشی؟
۱۲🔓دوس داری کیو بوس کنی؟😉💋
۱۳🔓از تو گالریت عکس بده
۱۴🔓از مخاطبینت عکس بده
۱۵🔓از صفحه چت روبیکات عکس بده
۱۶🔓لباس زیرت چه رنگیه؟🙊
۱۷🔓از وسایل آرایشت عکس بده
۱۸🔓از لباسای کمدت عکس بده
۱۹🔓از کفشات عکس بده
۲۰🔓تالا بهت تجاوز شده؟😥
۲۱🔓تاحالا مجبور شدی به زور به کسی بگی دوست دارم؟
۲۲🔓تاحالا یه دخترو بردی خونتون؟
۲۳🔓تاحالا یه پسرو بردی خونتون؟
۲۴🔓با کی ل....ب گرفتی؟😜
۲۵🔓خود ار.ض..ای..ی کردی؟😬💦
۲۶🔓خانوادت یا رفیقت یا عشقت؟
۲۷🔓سلامتی یا علم یا پول؟
۲۸🔓شهوتی شدی تاحالا؟😂
۲۹🔓خونتون کجاس؟
۳۰🔓خاستگار داری؟عکسش یا اسمش
۳۱🔓به کی اعتماد داری؟
۳۲🔓تاحالا با کسی رفتی تو خونه خالی؟
۳۳🔓چاقی یا لاغر؟
۳۴🔓قد بلندی یا کوتاه؟
۳۵🔓رنگ چشمت؟
۳۶🔓رنگ موهات؟
۳۷🔓موهات فرفریه یا صاف و تا کجاته؟
۳۸🔓تاریخ تولدت؟
۳۹🔓تاریخ تولد عشقت؟
۴۰🔓عشقت چجوری باهات رفتار میکنه؟
۴۱🔓با دوس پسرت عشق بازی کردی؟🤤
۴۲🔓پیش عشقت خوابیدی؟
۴۳🔓عشقتو بغل کردی؟
۴۴🔓حاضری ۱۰ سال از عمرتو بدی به عشقت؟
۴۵🔓مامان و بابات چقد دوست دارن؟
۴۶🔓دعوا کردی؟
۴۸🔓چند بار کتک زدی؟
۴۹🔓چند بار کتک خوردی؟
۵۰🔓تاحالا تورو دزدیدن؟
۵۱🔓تاحالا کسی ل..خ....ت تورو دیده؟🤭
۵۲🔓تاحالا ل...خ...ت کسیا دیدی؟
۵۳🔓دست نام....حرم بهت خورده؟
۵۴🔓دلت برا کی تنگ شده؟
۵۵🔓دوس داشتی کجا بودی؟
۵۶🔓به خودکشی فکر کردی؟
۵۷🔓عکستو بده
۵۸🔓ممه هات بزرگ شدن؟🙈
۵۹🔓با دیدن بدن خودت ح...ش....ری میشی؟
۶۰🔓پیش کسی ضایع شدی؟
۶۱🔓از مدرسه فرار کردی؟
۶۲🔓میخوای چند سالگی ازدواج کنی؟
۶۳🔓اگه مامان و بابات اجازه ندن با عشقت ازدواج کنی چیکار میکنی؟
۶۴🔓چند سالگی پ....ری....و..د شدی؟😶
۶۵🔓وقتی پریودی چجوری هستی؟
۶۶🔓رنگ مورد علاقت؟
۶۷🔓غذای مورد علاقت؟
۶۸🔓پولدارین یا فقیر؟
۶۹🔓دوس داری با من بری بیرون؟
۷۰🔓منو بوس میکنی؟☺️😚
۷۱🔓منو میکنی؟😬
۷۲🔓س...ک...س چت داشتی؟
۷۳🔓خوشت میاد از س....ک.....س؟
۷۴🔓خجالتی هستی یا پررو؟
۷۵🔓دوس داری بکنمت؟🤤
۷۶🔓تاحالا کسی برات خورده؟😁
۷۷🔓من ببوسمت خوشحال میشی؟
۷۸🔓خفن ترین کاری که تا الان کردی؟
۷۹🔓آرزوت چیه؟
۸۰🔓سیگار یا قلیون میکشی؟
۸۱🔓منو میبری خونتون؟
۸۲🔓میذاری بیام خونتون؟
۸۳🔓تاحالا شکست عشقی خوردی؟💔
۸۴🔓اگه به زور شوهرت بدن تو چیکار میکنی؟
۸۵🔓اگه به زور زنت بدن تو چیکار میکنی؟
۸۶🔓تاحالا با پسر غریبه خوابیدی؟
۸۷🔓تاحالا با دختر غریبه خوابیدی؟
۸۸🔓با همجنست خوابیدی؟
۸۹🔓مدرسه یا گوشی؟
۹۰🔓سر کار میری؟
۹۱🔓کلن اخلاقت چجوریه؟
۹۲🔓هنوز پرده داری؟😐
۹۳🔓قلقلکی هستی؟
۹۴🔓سکس خشن دوس داری یا ملایم؟
۹۵🔓کصکش ناله های دختر مردمو میخوای ببینی😐⚔
۹۶🔓چند بار سوتی میدی؟
۹۷🔓مواظب کصت باش تا بیام بگیرمت باشه؟🤭👍🏻
۹۸🔓تاحالا مچ عشقتو موقع لب بازی با یه دختر دیگه گرفتی؟
۹۹🔓تاحالا مچ عشقتو موقع لب بازی با یه پسر دیگه گرفتی؟
۱۰۰🔓اگه یه نفر مزاحم ناموست بشه باهاش چجوری رفتار میکنی؟
۱۰۱🔓شمارتو بده
۱۰۲🔓چقد آرایش میکنی؟
۱۰۳🔓پسر بازی رو دوس داری؟
۱۰۴🔓دختر بازی رو دوس داری؟
۱۰۵🔓اگه یه کص مفتی گیرت بیاد بازم پسش میزنی؟😁👍🏻
۱۰۶🔓پشمالو دوس داری؟🤧
۱۰۷🔓دوس داری شوهر آیندت چجوری باشه؟
۱۰۸🔓دوس داری زن آیندت چجوری باشه؟
۱۰۹🔓دوس داری چند تا بچه داشته باشی؟
۱۱۰🔓قشنگ ترین اسم پسر بنظرت؟
۱۱۱🔓قشنگ ترین اسم دختر بنظرت؟
۱۱۲🔓من خوشگلم یا زشت؟
۱۱۳🔓خوشگل ترین پسر گپ کیه؟
۱۱۴🔓خوشگل ترین دختر گپ کیه؟
۱۱۵🔓کی صداش از همه زیباتره؟
۱۱۶🔓خانومت خوشگله یا زشته؟
۱۱۷🔓خوشتیپ هستی یا خوش قیافه؟
۱۱۸🔓تاحالا احساس کردی یکی روت کراش زده باشه؟
۱۱۹🔓اگه یکی رو ناراحت ببینی چیکار میکنی؟
۱۲۰🔓بی رحمی یا دلت زود به رحم میاد؟
۱۲۱🔓تاحالا پیش کسی گوزیدی؟
۱۲۲🔓تاحالا خودتو خیس کردی؟
۱۲۳🔓اگه بیدار شی ببینی یکی خوابیده روت واکنشت چیه؟
۱۲۴🔓اگه روی یه صندلی کیک باشه یکیش کیر باشه،رو کدوم میشینی و کدومو میخوری؟
۱۲۵🔓جنسیتتو دوس داری عوض کنی؟
۱۲۶🔓دوس داری بری سربازی؟
۱۲۷🔓عکس یهوی بده؟
۱۲۸🔓شام دعوتت کنم قبول میکنی؟
۱۲۹🔓اگه همین الان بهت بگم دوست دارم واکنشت چیه؟
											""")
                            await update.reply('سوالات فرستاده شده اند با کلمه (بپرس) ربات از شما سوال میپرسد.')
                        
                        elif update.raw_text == 'آمار' or update.raw_text == '/STATUS':
                            await update.reply("""
											لینک هایی که ربات در انها فعال است |💠
											___________________________________
											https://rubika.ir/joing/ECBDABCC0AEEBIQIWWSFNCFASVIDTWKK
											___________________________________
											___________________________________
											https://rubika.ir/joing/EDAEACHA0MOHHMLACCJBGHSFEJYWQQZU
											___________________________________
											___________________________________
											https://rubika.ir/joing/ECEGIDGC0UBSZJEVRCQPKAYNQTUWPYLR
											___________________________________
                                            ___________________________________
											https://rubika.ir/joing/DJFJGEFI0VMXESRRPECXQPEKSNDOZDXM
											___________________________________
											جهت ثبت لینک خود به ایدی (@ID_Coder) پیام بدهید |💠
											""")

                        elif update.raw_text == 'کاربردی' or update.raw_text == '/KARBORD':
                            await update.reply("""
											💠 | ᑭᗩᑎᗴᒪ: 

/JOK လ ارسال جوک

/ZEKR လ ذکر امروز

/HADIS လ حدیث

/DANSTANI လ دانستنی

/BIO လ ارسال بیوگرافی

/TIME လ تاریخ دقیق

/ARZ လ دریافت نرخ ارز
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")
                            
                        

                        elif update.author_guid in group_admins and update.text == '/SETTING':
                            await update.reply("""
											💠 | 𝕊𝔼𝕋𝕋𝕀ℕ𝔾: 

/OPEN လ بازکردن گروه

/CLOSE လ قفل گروه

/LOCKGIF လ قفل گیف

/UNLOCKGIF လ بازکردن گیف

/PASOKH လ حالت سخنگو روشن

/PASOKHOF လ حالت سخنگو خاموش

/WELCOME လ حالت خوش اومد گویی روشن

/WELCOMEOFF လ خوش اومد گویی خاموش

/OFFSHISHE လ قفل شیشه ای خاموش

/ONSHISHI လ قفل شیشه ای روشن

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")
                            
                        elif update.raw_text == '/SETTING' or update.raw_text == 'تنظیمات':
                            await update.reply("این دستور مخصوص ادمین هست")

                        elif update.author_guid in group_admins and update.text == '/update-admins':
                            reply = await update.reply('در حال به روزرسانی لیست ادمین ها...')
                            await updateAdmins(client)
                            await sleep(2)
                            await reply.edit('به روزرسانی لیست ادمین ها انجام شد.')

                        elif update.author_guid in group_admins and update.text.startswith('/ban'):
                            if update.reply_message_id != None:
                                try:
                                    result = await client(methods.messages.GetMessagesByID(my_group, [update.reply_message_id]))
                                    result = result.to_dict().get('messages')[0]
                                    if not result.get('author_object_guid') in group_admins:
                                        result = await client(methods.groups.BanGroupMember(my_group, result.get('author_object_guid')))
                                        await update.reply('کاربر مورد نظر از گروه حذف شد.')
                                    else:
                                        await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                except IndexError:
                                    await update.reply('ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است.') # created by shayan heidari | rubpy
                            elif update.text.startswith('/ban @'):
                                username = update.text.split('@')[-1]
                                if username != '':
                                    result = await client(methods.extras.GetObjectByUsername(username.lower()))
                                    result = result.to_dict()
                                    if result.get('exist'):
                                        if result.get('type') == 'User':
                                            user_guid = result.get('user').get('user_guid')
                                            if not user_guid in group_admins:
                                                result = await client(methods.groups.BanGroupMember(my_group, user_guid))
                                                await update.reply('کاربر مورد نظر از گروه حذف شد.')
                                            else:
                                                await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                        else:
                                            await update.reply('کاربر مورد نظر کاربر عادی نیست.')
                                    else:
                                        await update.reply('آیدی مورد نظر اشتباه است.')
                                else:
                                    await update.reply('آیدی مورد نظر اشتباه است.')
                            else:
                                await update.reply('روی یک کاربر ریپلای بزنید.') # created by shayan heidari | rubpy

            @client.on(handlers.MessageUpdates(models.is_group()))
            async def updates(update):
                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if no_gifs:
                            if not update.author_guid in group_admins:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Gif':
                                    await update.delete_messages() # created by shayan heidari | rubpy
                                    print('Delete A Gif.')

                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if shishe:
                            if not update.author_guid in group_admins:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                date = ___date____time.historyIran()
                                time = ___date____time.hourIran()
                                if update.raw_text == 'یک عضو از طریق لینک به گروه افزوده شد.' or update.raw_text == '1 عضو جدید به گروه افزوده شد.':
                                    await update.delete_messages()
                                if update.raw_text == 'یک عضو گروه را ترک کرد.':
                                    await update.delete_messages()
                                if update.raw_text.startswith('گفتگوی صوتی به پایان رسید.'):
                                    await update.delete_messages()
                                if update.raw_text == 'گفتگوی صوتی ایجاد شده است.':
                                    await update.delete_messages()
                                if update.raw_text == 'یک پیام سنجاق شد.':
                                    await update.delete_messages()
                                if update.raw_text == '1 عضو از گروه حذف شد.':
                                    await update.delete_messages()
                                if update.raw_text == '1 عضو جدید به گروه افزوده شد.':
                                    await update.delete_messages()

                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if welcome:
                            if not update.author_guid in group_admins:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                date = ___date____time.historyIran()
                                time = ___date____time.hourIran()
                                if update.raw_text == 'یک عضو از طریق لینک به گروه افزوده شد.' or update.raw_text == '1 عضو جدید به گروه افزوده شد.':
                                    await update.reply('سلام کاربر عزیز 🌹 \n• به گروه ما خوش اومدی 😍 \n 📿 لطفا قوانین رو رعایت کن .\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی .')
                                if update.raw_text == 'یک عضو گروه را ترک کرد.':
                                    await update.reply('خدانگهدار 👋 ')

                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if GAME:
                            if not update.author_guid in group_admins:
                                if update.raw_text == 'بپرس' or update.raw_text == 'بعدی':
                                    rando = ["۱۱۸🔓تاحالا احساس کردی یکی روت کراش زده باشه؟","۱۱۹🔓اگه یکی رو ناراحت ببینی چیکار میکنی؟","۱۲۰🔓بی رحمی یا دلت زود به رحم میاد؟","۱۲۱🔓تاحالا پیش کسی گوزیدی؟","۱۲۲🔓تاحالا خودتو خیس کردی؟","۱۲۳🔓اگه بیدار شی ببینی یکی خوابیده روت واکنشت چیه؟","۱۲۴🔓اگه روی یه صندلی کیک باشه یکیش کیر باشه،رو کدوم میشینی و کدومو میخوری؟","۱۲۵🔓جنسیتتو دوس داری عوض کنی؟","۱۲۶🔓دوس داری بری سربازی؟","۱۲۷🔓عکس یهوی بده؟","۱۲۸🔓شام دعوتت کنم قبول میکنی؟","۱۲۹🔓اگه همین الان بهت بگم دوست دارم واکنشت چیه؟","۱۰۰🔓اگه یه نفر مزاحم ناموست بشه باهاش چجوری رفتار میکنی؟","۱۰۱🔓شمارتو بده","۱۰۲🔓چقد آرایش میکنی؟","۱۰۳🔓پسر بازی رو دوس داری؟","۱۰۴🔓دختر بازی رو دوس داری؟","۱۰۵🔓اگه یه کص مفتی گیرت بیاد بازم پسش میزنی؟😁👍🏻","۱۰۶🔓پشمالو دوس داری؟🤧","۱۰۷🔓دوس داری شوهر آیندت چجوری باشه؟","۱۰۸🔓دوس داری زن آیندت چجوری باشه؟","۱۰۹🔓دوس داری چند تا بچه داشته باشی؟","۱۱۰🔓قشنگ ترین اسم پسر بنظرت؟","۱۱۱🔓قشنگ ترین اسم دختر بنظرت؟","۱۱۲🔓من خوشگلم یا زشت؟","۱۱۳🔓خوشگل ترین پسر گپ کیه؟","۱۱۴🔓خوشگل ترین دختر گپ کیه؟","۱۱۵🔓کی صداش از همه زیباتره؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۷🔓خوشتیپ هستی یا خوش قیافه؟","۸۰🔓سیگار یا قلیون میکشی؟","۸۱🔓منو میبری خونتون؟","۸۲🔓میذاری بیام خونتون؟","۸۳🔓تاحالا شکست عشقی خوردی؟💔","۸۴🔓اگه به زور شوهرت بدن تو چیکار میکنی؟","۸۵🔓اگه به زور زنت بدن تو چیکار میکنی؟","۸۶🔓تاحالا با پسر غریبه خوابیدی؟","۸۷🔓تاحالا با دختر غریبه خوابیدی؟","۸۸🔓با همجنست خوابیدی؟","۸۹🔓مدرسه یا گوشی؟","۹۰🔓سر کار میری؟","۹۱🔓کلن اخلاقت چجوریه؟","۹۲🔓هنوز پرده داری؟😐","۹۳🔓قلقلکی هستی؟","۹۴🔓سکس خشن دوس داری یا ملایم؟","۹۵🔓کصکش ناله های دختر مردمو میخوای ببینی😐⚔","۹۶🔓چند بار سوتی میدی؟","۹۷🔓مواظب کصت باش تا بیام بگیرمت باشه؟🤭👍🏻","۹۸🔓تاحالا مچ عشقتو موقع لب بازی با یه دختر دیگه گرفتی؟","۹۹🔓تاحالا مچ عشقتو موقع لب بازی با یه پسر دیگه گرفتی؟","۶۰🔓پیش کسی ضایع شدی؟","۶۱🔓از مدرسه فرار کردی؟","۶۲🔓میخوای چند سالگی ازدواج کنی؟","۶۳🔓اگه مامان و بابات اجازه ندن با عشقت ازدواج کنی چیکار میکنی؟","۶۴🔓چند سالگی پ....ری....و..د شدی؟😶","۶۵🔓وقتی پریودی چجوری هستی؟","۶۶🔓رنگ مورد علاقت؟","۶۷🔓غذای مورد علاقت؟","۶۸🔓پولدارین یا فقیر؟","۶۹🔓دوس داری با من بری بیرون؟","۷۰🔓منو بوس میکنی؟☺️😚","۷۱🔓منو میکنی؟😬","۷۲🔓س...ک...س چت داشتی؟","۷۳🔓خوشت میاد از س....ک.....س؟","۷۴🔓خجالتی هستی یا پررو؟","۷۵🔓دوس داری بکنمت؟🤤","۷۶🔓تاحالا کسی برات خورده؟😁","۷۷🔓من ببوسمت خوشحال میشی؟","۷۸🔓خفن ترین کاری که تا الان کردی؟","۷۹🔓آرزوت چیه؟","۳۰🔓خاستگار داری؟عکسش یا اسمش","۳۱🔓به کی اعتماد داری؟","۳۲🔓تاحالا با کسی رفتی تو خونه خالی؟","۳۳🔓چاقی یا لاغر؟","۳۴🔓قد بلندی یا کوتاه؟","۳۵🔓رنگ چشمت؟","۳۶🔓رنگ موهات؟","۳۷🔓موهات فرفریه یا صاف و تا کجاته؟","۳۸🔓تاریخ تولدت؟","۳۹🔓تاریخ تولد عشقت؟","۴۰🔓عشقت چجوری باهات رفتار میکنه؟","۴۱🔓با دوس پسرت عشق بازی کردی؟🤤","۴۲🔓پیش عشقت خوابیدی؟","۴۳🔓عشقتو بغل کردی؟","۴۴🔓حاضری ۱۰ سال از عمرتو بدی به عشقت؟","۴۵🔓مامان و بابات چقد دوست دارن؟","۴۶🔓دعوا کردی؟","۴۸🔓چند بار کتک زدی؟","۴۹🔓چند بار کتک خوردی؟","۵۰🔓تاحالا تورو دزدیدن؟","۵۱🔓تاحالا کسی ل..خ....ت تورو دیده؟🤭","۵۲🔓تاحالا ل...خ...ت کسیا دیدی؟","۵۳🔓دست نام....حرم بهت خورده؟","۵۴🔓دلت برا کی تنگ شده؟","۵۵🔓دوس داشتی کجا بودی؟","۱🔓عاشق شدی؟اسمش❤️","۲🔓رل زدی تاحالا؟اسمش","۳🔓کراش داری؟اسمش","۴🔓چند بار تا الان رابطه جنسی داشتی؟با کی😐💦","۵🔓از کی خوشت میاد؟","۶🔓از کی بدت میاد؟","۷🔓منو دوس داری؟بهم ثابت کن","۸🔓کی دلتو شکونده؟","۹🔓دل کیو شکوندی؟","۱۰🔓وقتی عصبانی هستی چجوری میشی؟","۱۱🔓دوس داری کیو بزنی یا بکشی؟","۱۲🔓دوس داری کیو بوس کنی؟😉💋","۱۳🔓از تو گالریت عکس بده","۱۴🔓از مخاطبینت عکس بده","۱۵🔓از صفحه چت روبیکات عکس بده","۱۶🔓لباس زیرت چه رنگیه؟🙊","۱۷🔓از وسایل آرایشت عکس بده","۱۷🔓از وسایل آرایشت عکس بده","۱۸🔓از لباسای کمدت عکس بده","۱۹🔓از کفشات عکس بده","۲۰🔓تالا بهت تجاوز شده؟😥","۲۱🔓تاحالا مجبور شدی به زور به کسی بگی دوست دارم؟","۲۲🔓تاحالا یه دخترو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۴🔓با کی ل....ب گرفتی؟😜","۲۵🔓خود ار.ض..ای..ی کردی؟😬💦"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if pasikh:
                            if not update.author_guid in group_admins:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                if update.raw_text == 'سلام' or update.raw_text == 'صلام' or update.raw_text == 'ثلام' or update.raw_text == 'hello' or update.raw_text == 'hi' or update.raw_text == 'های' or update.raw_text == 'هلو':
                                    rando = ["**سلام گلم:)**","ســــــــلامـــــــــــــــ","چطوری گلم؟","همه ساکت عشقم میخوام حرف بزنه!",]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'خوبی' or update.raw_text == 'خبی' or update.raw_text == 'چطوری':
                                    rando = ["از یه ربات چی انتظار داری؟!","مرسی ممنون شما خوبید؟","خداروشکر منم خوبم اصل"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'ربات' or update.raw_text == 'رباط' or update.raw_text == 'بات' or update.raw_text == 'باط':
                                    rando = ["جان ربات؟","اسممو صدا بزن:)!","درخدمتم:)"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'اسمت چیه؟' or update.raw_text == 'اسمت چیه' or update.raw_text == 'اسمت' or update.raw_text == 'نامت چیست' or update.raw_text == 'اسمت چیست' or update.raw_text == 'اسمتو بگو' or update.raw_text == 'نامتو بگو' or update.raw_text == 'اسمتو نمیدونم':
                                    rando = ["اسم من دیجی بات هست:)","بهم بگو دیجی بات","نمیگم در حسرتش بمونی:)"]
                                    renn= choice(rando)
                                    await update.reply(renn)
                                
                                if update.raw_text == 'چیه؟' or update.raw_text == 'چی هست' or update.raw_text == 'چی هست؟' or update.raw_text == 'چیست؟' or update.raw_text == 'چیست' or update.raw_text == 'چی' or update.raw_text == 'چی؟':
                                    rando = ["مغز بادوم😐","اینم فهمید","ار پیچی😐","کوفته پیچی😐💔"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'اها' or update.raw_text == 'فهمیدم' or update.raw_text == 'باشه' or update.raw_text == 'حله':
                                    rando = ["چه عجب فهمیدی","پیچ پیچی😐","خوب شد فهمیدی"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'بای' or update.raw_text == 'فعلا' or update.raw_text == 'خداحافظ' or update.raw_text == 'من رفتم':
                                    rando = ["🖐 خدافظ عزیزم","بسلامتی","❣️خدافظ","از کنار برو نخوری زمین🤣","😄 برو ولی زود برگردیا","","☹️ رفتی پشت سرتو نگاه نکن","برو پیش ملا حافظ😂😂"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'چه خبر' or update.raw_text == 'چخبر' or update.raw_text == 'چخبر؟' or update.raw_text == 'چه خبر؟':
                                    rando = ["رالف دلش تنگه برات","سلامتی 🙂","عمت سلام میرسونه 😁","سلامتی شما چه خبر؟🙃","خبر اینکه... زمین گرده/:","بیخبری🙃"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'ریدم' or update.raw_text == 'ریدم؟' or update.raw_text == 'ریدوم' or update.raw_text == 'ریدم!':
                                    rando = ["خسته نباشی","مبارکه","بفرما دستمال🧻","بخور سرد نشه","تمیز کن زودتر"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'شب بخیر' or update.raw_text == 'شب خوش' or update.raw_text == 'شو خوش' or update.raw_text == 'شبخوش':
                                    rando = ["شبت شیک","خدانگهدارت","شبت پر ستاره","بای بای","شبت زیبا","مراقب خودت باش"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'تو؟' or update.raw_text == 'تو':
                                    rando = ["نه پس تو؟😑","بی ادب تو یعنی چی بگو شما😑","نه پس تو😒","تو نه شما😒"]
                                    renn= choice(rando)
                                    await update.reply(renn)

                                if update.raw_text == 'گمشو':
                                    rando = ["خودت گمشو😐","ادرس خونمون و بلدم😕","راه و بلدم","نترس بی ادب راه و بلدم"]
                                    renn= choice(rando)
                                    await update.reply(renn)

            await client.run_until_disconnected()

run(main())