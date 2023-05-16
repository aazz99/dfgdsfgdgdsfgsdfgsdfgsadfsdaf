import os
from libraryArsein.Arsein import Robot_Rubika
os.system("clear")
from random import choice
import pyfiglet
from random import choice,randint
from random import randint
import random
red = '\033[31m' 
green = '\033[32m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
text = "  DiGi BOT"

bot = Robot_Rubika("gqlrnqmjticuhgnvurlzgrkbnuttudrk")
os.system("clear")
txt = pyfiglet.figlet_format(text,font='slant')
print(red+txt)
print(darkblue+"_"*67+white)

group_guid="g0CpJxb0b602da9b9c5d435ad40ba88e"
bot_guid="u0FYcW80eff89a2c1b439888683994a1"

#برای اضافه کردن فهش به لاین 153 بروید...!
start_bot=Chat=lock_Forward=lock_Video=lock_Voice=lock_Image=lock_Gif=HarfZedFohsh=True
answered=[]
ekhtar:list=[]
max_ekhtar=1

def star(guid,user):
	stars.append(guid)
	star_count = int(stars.count(guid))
	if star_count == 1:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [1/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 2:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [2/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 3:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [3/3] امتیاز دریافت کردید اکنون آدمین گروه می شوید 🎉😱", message_id=mesagid)
		bot.setGroupAdmin(target,guid)


# Checker for existence of necessary files...!
try:
	open('learn.json','r').read()
except:
	open('learn.json','w')
try:
	open('gif_learn.json',"r").read()
except:
	open('gif_learn.json',"w")
try:
	open('rulse.txt','r').read()
except:
	open('rulse.txt','w')
try:
	open('help.txt','r').read()
except:
	open('help.txt','w')




def zedForward(msg):
	try:
		if msg.get("author_object_guid") not in admins:
			bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
			user_guid=msg.get("author_object_guid")
			usNam=bot.getUserInfo(user_guid)['data']['user'].get('username')
			if usNam == None:
				
				name=bot.getUserInfo(user_guid)['data']['user']["first_name"]
			else:
				name="@"+usNam
			ekhtar.append(user_guid)
			ad=ekhtar.count(user_guid)
			if int(ad)<int(max_ekhtar):
				bot.sendMessage(group_guid,f"""💢 اخطار 

کاربر {name} عزیز...

شما به دلیل رعایت نکردن قوانین اخطار گرفتید!

تعداد اخطار شما : {ad}/{max_ekhtar}""",message_id=msg.get("message_id"))
			elif int(ad)==int(max_ekhtar):
				bot.banGroupMember(group_guid,user_guid)
				bot.sendMessage(group_guid,f"""❌ کاربر {name} عزیز

شما به علت تبلیغات از گروه بن میشوید!

باید قوانین رو رعایت میکردی!""",message_id=msg.get("message_id"))
			elif int(ad)>int(max_ekhtar):
				bot.banGroupMember(group_guid,user_guid)
	except: pass

def zedLInk(msg):
	try:
		if msg.get("author_object_guid") not in admins and msg.get("author_object_guid") != bot_guid:
			links = ["join","rubika.ir/post","@"]
			for link in links:
				if link in msg.get("text") :
					bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
					user_guid=msg.get("author_object_guid")
					usNam=bot.getUserInfo(user_guid)['data']['user'].get('username')
					if usNam == None:
						name=bot.getUserInfo(user_guid)['data']['user']["first_name"]
					else:
						name="@"+usNam
					ekhtar.append(user_guid)
					ad=ekhtar.count(user_guid)
					if int(ad)<int(max_ekhtar):
						bot.sendMessage(group_guid,f"""💢 اخطار 

کاربر {name} عزیز...

شما به دلیل رعایت نکردن قوانین اخطار گرفتید!

تعداد اخطار شما : {ad}/{max_ekhtar}""",message_id=msg.get("message_id"))
					elif int(ad)==int(max_ekhtar):
						bot.banGroupMember(group_guid,user_guid)
						bot.sendMessage(group_guid,f"""❌ کاربر {name} عزیز

شما به حداکثر اخطار رسیدید به همین دلیل از گروه بن میشوید!

باید قوانین رو رعایت میکردی!""",message_id=msg.get("message_id"))
					elif int(ad)>int(max_ekhtar):
						bot.banGroupMember(group_guid,user_guid)
	except: pass

def LERNINg_j(msg,M_ID):
	try:
		try:
			user=msg[6:]
			file = open('learn.json', 'a')
			file.write(f'\n{user}')
			file.close()
			text=user.split('=')
			bot.sendMessage(group_guid,f"""یادگرفتم!
از این به بعد هرکس گفت {text[0]} به صورت رندوم بهش یکی از ﴿{text[1]}﴾ میگم""", message_id=M_ID)
		except:
			bot.sendMessage(group_guid,f"خطا در یادگیری!", message_id=M_ID)
	except: pass

def upLERNINg_j(msg,M_ID):
	try:
		try:
			text=msg[8:]
			file_1=open('learn.json','r+').read().split('\n')
			open('learn.json','w+')
			for i in file_1:
				g=open('learn.json','a')
				n=i.split("=")
				if text != n[0]:
					if i != "":
						g.write(f'{i}\n')
			bot.sendMessage(group_guid,f"کلمه {text} با موفقیت از لیست حذف شد!",message_id=M_ID)
		except:
			bot.sendMessage(group_guid,f"خطا در یادگیری!", message_id=M_ID)
	except:pass

def zadFohsh(msg):
	try:
		if HarfZedFohsh== True:
			if msg.get("author_object_guid") not in admins:
				for fohsh in ["خر","گاو","کیری","کونی","@","خارکسته","مادرجنده","کص","کس","کوص","کوس","مادرت","خارت","کستمادر","کیرم","کیری","بکیرم","کصی","کونده","جنده","کونکش","سگ","میمون"]:#تویه این لیست میتونید طبق همون الگو عمل کنید بین هر کلمه  از یدونه (,) استفاده کنید
					if fohsh in msg.get("text"):
						bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
	except: pass








while 1:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(group_guid)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(group_guid)["data"]["chat"]["last_message_id"]
		
		
		while 1:
			try:
				messages = bot.getMessages(group_guid,min_id)
				break
			except:
				continue

		for msg in messages:
			if msg['type'] == 'Text' :
					try:
						if msg.get('message_id') not in answered:
							if "forwarded_from" in msg.keys():
								if lock_Forward == True:
									zedForward(msg)
							zedLInk(msg)
							zadFohsh(msg)
							print(msg.get("text"))
							answered.append(msg.get("message_id"))
							if start_bot ==True and msg.get("author_object_guid")!=bot_guid:
								if Chat==True:
									try:
										text =msg.get("text")
										t = open('learn.json','r').read().split('\n')
										for a in t:
											n = a.split('=')
											try:
												if text.startswith(n[0]):
													pasokh=choice(n[1].split(','))
													bot.sendMessage(group_guid,f"{pasokh}",message_id=msg.get('message_id'))
											except:pass
									except:pass
									
								if msg.get("text").startswith("uplearn ") :
									if msg.get('author_object_guid') in admins:
										upLERNINg_j(msg.get("text"),msg.get("message_id"))
										
								elif msg.get("text").startswith("learn ") :
									if msg.get('author_object_guid') in admins:
										LERNINg_j(msg.get("text"),msg.get("message_id"))
										
								elif msg.get("text").startswith("gif learn") :
									texlearn=msg.get("text").replace("gif learn","")
									try:
										replay__guid=""
										for ii in bot.getMessagesInfo(group_guid, [msg.get("reply_to_message_id")]):
											g=open('gif_learn.json','a')
											g.write(f"\n{ii['file_inline']['file_id']}:{texlearn}")
											g.close()
										bot.sendMessage(group_guid,f'یادگرفتم!\n از این به بعد هرکس این گیفو بفرسته من میگم {choice(texlearn.split("="))}', message_id=msg.get("message_id"))
									except: pass
								elif msg.get("text").startswith("ازاد") and msg.get('author_object_guid') in admins or msg.get("text").startswith("!unban") and msg.get('author_object_guid') in admins:
									try:
										if msg.get("text")=="!unban" or msg.get("text")=="ازاد" :
											try:
												replay__guid=""
												for ii in bot.getMessagesInfo(group_guid, [msg.get("reply_to_message_id")]):
													replay__guid=ii['author_object_guid']
												if replay__guid not in admins:
													try:
														bot.unbanGroupMember(group_guid,replay__guid)
														bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت از لیست سیاه حذف شد!",message_id=msg.get("message_id"))
													except:
														bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
												else:
													bot.sendMessage(group_guid,f"کاربر ادمین میباشد!(:",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
										else:
											try:
												user_guid=bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
												bot.unbanGroupMember(group_guid,user_guid)
												bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت از لیست سیاه حذف شد!",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
									except:
										bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("!بن") and msg.get('author_object_guid') in admins or msg.get("text").startswith("!ban") and msg.get('author_object_guid') in admins:
									try:
										if msg.get("text")=="!بن" or msg.get("text")=="!ban" :
											try:
												replay__guid=""
												for ii in bot.getMessagesInfo(group_guid, [msg.get("reply_to_message_id")]):
													replay__guid=ii['author_object_guid']
												if replay__guid not in admins:
													try:
														bot.banGroupMember(group_guid,replay__guid)
														bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت از گروه حذف شد!",message_id=msg.get("message_id"))
													except: pass
												else:
													bot.sendMessage(group_guid,f"کاربر ادمین میباشد!(:",message_id=msg.get("message_id"))
											except: pass
										else:
											try:
												user_guid=bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
												bot.banGroupMember(group_guid,user_guid)
												bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت از گروه حذف شد!",message_id=msg.get("message_id"))
											except: pass
									except: pass
								elif msg.get("text").startswith("افزودن_ادمین") and msg.get('author_object_guid') in admins or msg.get("text").startswith("add_admin") and msg.get('author_object_guid') in admins:
									try:
										if msg.get("text")=="افزودن_ادمین" or msg.get("text")=="add_admin" :
											try:
												replay__guid=""
												for ii in bot.getMessagesInfo(group_guid, [msg.get("reply_to_message_id")]):
													replay__guid=ii['author_object_guid']
												if replay__guid not in admins:
													try:
														bot.setGroupAdmin(group_guid,replay__guid)
														bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت ادمین شد!",message_id=msg.get("message_id"))
													except:
														bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
												else:
													bot.sendMessage(group_guid,f"کاربر ادمین میباشد!(:",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
										else:
											try:
												user_guid=bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
												bot.setGroupAdmin(group_guid,user_guid)
												bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت ادمین شد!",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
									except:
										bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("حذف_ادمین") and msg.get('author_object_guid') in admins or msg.get("text").startswith("del_admin") and msg.get('author_object_guid') in admins:
									try:
										if msg.get("text")=="حذف_ادمین" or msg.get("text")=="del_admin" :
											try:
												replay__guid=""
												for ii in bot.getMessagesInfo(group_guid, [msg.get("reply_to_message_id")]):
													replay__guid=ii['author_object_guid']
												if replay__guid in admins:
													try:
														bot.deleteGroupAdmin(group_guid,replay__guid)
														bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت برکنار شد!",message_id=msg.get("message_id"))
													except:
														bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
												else:
													bot.sendMessage(group_guid,f"کاربر ادمین نمیباشد!(:",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
										else:
											try:
												user_guid=bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
												bot.deleteGroupAdmin(group_guid,user_guid)
												bot.sendMessage(group_guid,f"کاربر مورد نظر با موفقیت برکنار شد!",message_id=msg.get("message_id"))
											except:
												bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
									except:
										bot.sendMessage(group_guid,f"خطا در عملیات...!",message_id=msg.get("message_id"))
										
								elif msg.get("text").startswith("Profile") or msg.get("text").startswith("profile") or msg.get("text").startswith("پروفایل"):
									try:
										adress=os.getcwd()+"/Profile"
										name_file=adress+"/"+choice(os.listdir(adress))
										bot.sendPhoto(group_guid,name_file,message_id=msg.get("message_id"))
									except:pass
								elif msg.get("text").startswith("قفل گیف روشن") or msg.get("text").startswith("/UNLOCKG") or msg.get("text").startswith("Lock_Gif"):
									if msg.get('author_object_guid') in admins:
										if lock_Gif != True:
											lock_Gif=True
											bot.sendMessage(group_guid,f"قفل گیف با موفقیت فعال شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل گیف از قبل فعال بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text")=="قفل گروه":
									if msg.get('author_object_guid') in admins:
										bot.setMembersAccess(group_guid, ["AddMember"])
										bot.sendMessage(group_guid,f"گروه با موفقیت قفل شد🔐",message_id=msg.get("message_id"))
									else:
										bot.sendMessage(group_guid,f"گروه از قبل قفل بود🔐🌚",message_id=msg.get("message_id"))
								elif msg.get("text")=="باز کردن گروه":
									if msg.get('author_object_guid') in admins:
										bot.setMembersAccess(group_guid, ["SendMessages","AddMember"])
										bot.sendMessage(group_guid,f"🔓 گروه اکنون باز است",message_id=msg.get("message_id"))
									else:
										print("ok")
										#bot.sendMessage(group_guid,f"گروه از قبل باز بود🔐🌚",message_id=msg.get("message_id"))
								elif msg.get("text")=="قطع کال":
									if msg.get('author_object_guid') in admins:
										GAP = bot.getGroupInfo(group_guid)["data"]["chat"]
										VOICE_CHAT = GAP["group_voice_chat_id"]
										bot.finishVoiceChat(group_guid,VOICE_CHAT)
										bot.sendMessage(group_guid,f"✅ با موفقیت قطع شد",message_id=msg.get("message_id"))
									else:
										bot.sendMessage(group_guid,f"این دستور مخصوص ادمین ها است.🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("قفل گیف خاموش") or msg.get("text").startswith("/LOCKP") or msg.get("text").startswith("Unlock_Gif"):
									if msg.get('author_object_guid') in admins:
										if lock_Gif != False:
											lock_Gif=False
											bot.sendMessage(group_guid,f"قفل گیف با موفقیت خاموش شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل گیف از قبل خاموش بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("قفل عکس روشن") or msg.get("text").startswith("/UNLOCKP") or msg.get("text").startswith("Lock_Image"):
									if msg.get('author_object_guid') in admins:
										if lock_Image != True:
											lock_Image=True
											bot.sendMessage(group_guid,f"قفل عکس با موفقیت فعال شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل عکس از قبل فعال بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("قفل عکس خاموش") or msg.get("text").startswith("unlock_image") or msg.get("text").startswith("Unlock_Image"):
									if msg.get('author_object_guid') in admins:
										if lock_Image != False:
											lock_Image=False
											bot.sendMessage(group_guid,f"قفل عکس با موفقیت خاموش شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل عکس از قبل خاموش بود🌚",message_id=msg.get("message_id"))

								elif msg.get("text").startswith("قفل فیلم روشن") or msg.get("text").startswith("/UNLOCKF") or msg.get("text").startswith("Lock_Video"):
									if msg.get('author_object_guid') in admins:
										if lock_Video != True:
											lock_Video=True
											bot.sendMessage(group_guid,f"قفل فیلم با موفقیت فعال شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل فیلم از قبل فعال بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("قفل فیلم خاموش") or msg.get("text").startswith("/LOCKF") or msg.get("text").startswith("Unlock_Video"):
									if msg.get('author_object_guid') in admins:
										if lock_Video != False:
											lock_Video=False
											bot.sendMessage(group_guid,f"قفل فیلم با موفقیت خاموش شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل فیلم از قبل خاموش بود🌚",message_id=msg.get("message_id"))

								elif msg.get("text").startswith("قفل ویس روشن") or msg.get("text").startswith("/UNLOCKV") or msg.get("text").startswith("Lock_Voice"):
									if msg.get('author_object_guid') in admins:
										if lock_Voice != True:
											lock_Voice=True
											bot.sendMessage(group_guid,f"قفل ویس با موفقیت فعال شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل ویس از قبل فعال بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("قفل ویس خاموش") or msg.get("text").startswith("/LOCKV") or msg.get("text").startswith("Unlock_Voice"):
									if msg.get('author_object_guid') in admins:
										if lock_Voice != False:
											lock_Voice=False
											bot.sendMessage(group_guid,f"قفل ویس با موفقیت خاموش شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"قفل ویس از قبل خاموش بود🌚",message_id=msg.get("message_id"))

								elif msg.get("text").startswith("ضد فهش روشن") or msg.get("text").startswith("/UNLOCKO") or msg.get("text").startswith("Lock_Fohsh"):
									if msg.get('author_object_guid') in admins:
										if HarfZedFohsh != True:
											HarfZedFohsh=True
											bot.sendMessage(group_guid,f"ضد فهش با موفقیت فعال شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"ضد فهش از قبل فعال بود🌚",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("ضد فهش خاموش") or msg.get("text").startswith("/LOCKO") or msg.get("text").startswith("Unlock_Fohsh"):
									if msg.get('author_object_guid') in admins:
										if HarfZedFohsh != False:
											HarfZedFohsh=False
											bot.sendMessage(group_guid,f"ضد فهش با موفقیت خاموش شد😄🚶‍♂",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"ضد فهش از قبل خاموش بود🌚",message_id=msg.get("message_id"))

								elif msg.get("text").startswith("حالت سخنگو روشن") or msg.get("text").startswith("/UNLOCKH"):
									if msg.get('author_object_guid') in admins:
										if Chat != True:
											Chat=True
											bot.sendMessage(group_guid,f"حالت سخنگو با موفقیت روشن شد!(:",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"حالت سخنگو از قبل روشن بود!:)",message_id=msg.get("message_id"))
								elif msg.get("text").startswith("حالت سخنگو خاموش") or msg.get("text").startswith("/LOCKH"):
									if msg.get('author_object_guid') in admins:
										if Chat != False:
											Chat=False
											bot.sendMessage(group_guid,f"حالت سخنگو با موفقیت خاموش شد!(:",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"حالت سخنگو از قبل خاموش بود!:)",message_id=msg.get("message_id"))
								elif msg.get('text').startswith("ربات خاموش") or msg.get('text').startswith("/OF"):
									try:
										if msg.get('author_object_guid') in admins and msg.get('author_object_guid') != bot_guid:
											if start_bot == True:
												start_bot=False
												bot.sendMessage(group_guid,f" ‌ربات با موفقیت خاموش شد!",message_id=msg.get("message_id"))
									except: pass
								elif msg.get("text").startswith("دستورات") or msg.get("text").startswith("help") or msg.get("text").startswith("!help") :
									try:
										if msg.get('author_object_guid') != bot_guid:
											help_file=open("help.txt","r").read()
											bot.sendMessage(group_guid,f'{help_file}', message_id=msg.get("message_id"))
									except: pass
#								elif msg.get("text").startswith("اپدیت دستورات") or msg.get("text").startswith("آپدیت دستورات") or msg.get("text").startswith("update_rules") :
#									try:
#										if msg.get('author_object_guid') in admins :
#											if msg.get('author_object_guid') != bot_guid:
#												new_help=msg.get("text").replace("آپدیت دستورات","").replace("اپدیت دستورات",'').replace("update_rules","")
#												open('help.txt','w+')
#												g=open('help.txt','a')
#												g.write(f'{new_help}')
#												g.close()
#												bot.sendMessage(group_guid,f'لیست دستورات با موفقیت بروز شد!', message_id=msg.get("message_id"))
#									except: pass
								elif msg.get("text").startswith("قوانین")or msg.get("text").startswith("rules") or msg.get("text").startswith("Rules") :
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											🚫 قوانین 🚫
❌ارسال لینک و پیام تبلیغاتی ممنوع!❌
⛔️ارسال فیلم ، عکس ، ویس ممنوع⛔️
📛فهش ممنوع📛
بی احترامی به ادمین ها کاملا ممنوع❗️

@User_Coder
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text").startswith("سازندت")or msg.get("text").startswith("سازنده") or msg.get("text").startswith("خرید") :
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f'سازنده من (@ID_Coder) است جهت خرید ربات پیام بدهید', message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text").startswith("پنل")or msg.get("text").startswith("/Panel") or msg.get("text").startswith("panel") or msg.get("text").startswith("دستورات") :
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/LOCKS လ قفل

/GAMES လ بازی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/SETTING" or msg.get("text")=="تنظیمات":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | 𝕊𝔼𝕋𝕋𝕀ℕ𝔾: 

/MTNP လ تنظیم متن پاسخگویی

/MTNG လ تنظیم متن پاسخگویی گیف

/DELP လ حذف متن پاسخ

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/BACK" or msg.get("text")=="برگشت":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/LOCKS လ قفل

/GAMES လ بازی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/MTNP":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											🔆دستور برای یادگیری کلمات از دستور زیر استفاده کنید
  ⭕👉🏼     learn    👈🏼⭕
با این دستور شما میتونین ربات رو سخنگو کنید که هرچی بگید جواب بده

❇️ برای مثال :

    →_→     learn ربات=بله     ←_← 

    /BACKS လ برگشت به منوی قبلی
‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌											
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/MTNG":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💢یادگیری گیف!

💯یادگیری گیف با دستور gif learn 
برای مثال:

ریپلای رویه گیف(gif learn سلام سید)

‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌			/BACKS လ برگشت به منوی قبلی								
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/DELP":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											📛برای پاک کردن اون از دستور زیر استفاده کنید📛

⛔ 👉🏼     uplearn     👈🏼⛔

❇️برای مثال :

 →_→     uplearn ربات    ←_← 
 
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌		/BACKS လ برگشت به منوی قبلی							
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/BACKS":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | 𝒞𝒪𝒩𝒟𝐼𝒯𝐼𝒪𝒩: 

/MTNP လ تنظیم متن پاسخگویی

/MTNG လ تنظیم متن پاسخگویی گیف

/DELP လ حذف متن پاسخ

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/CONDITION" or msg.get("text")=="وضعیت":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											پلن یک ماهه برای شما فعال است |💠
											
											/BACK လ برگشت به منوی اصلی
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/STATUS" or msg.get("text")=="آمار":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											لینک هایی که ربات در انها فعال است |💠
											___________________________________
											https://rubika.ir/joing/EAIBAABJ0QTTOEKTUBTTSPQMSRCZWNYU
											___________________________________
											___________________________________
											https://rubika.ir/joing/ECBDABCC0AEEBIQIWWSFNCFASVIDTWKK
											___________________________________
											___________________________________
											https://rubika.ir/joing/EBFBIIBD0XNOKETFAAOHCVCOPHMXABSK
											___________________________________
											جهت ثبت لینک خود به ایدی (@ID_Coder) پیام بدهید |💠
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/LOCKS" or msg.get("text")=="/LOCKS":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | 𝓛𝓞𝓒𝓚𝓢: 

/ON လ روشن کردن ربات

/OF လ خاموش کردن ربات

/LOCKH လ خاموش کردن حالت سخنگو

/UNLOCKH လ روشن کردن حالت سخنگو

/LOCKO လ خاموش کردن حالت ضد فحش

/UNLOCKO လ روشن کردن حالت ضد فحش

/UNLOCKG လ فعال کردن ضد گیف

/LOCKG လ خاموش کردن ضد گیف

/LOCKP လ خاموش کردن ضد عکس

/UNLOCKP လ روشن کردن ضد عکس

/LOCKF လ خاموش کردن ضد فیلم

/UNLOCKF လ روشن کردن ضد فیلم

/LOCKV လ روشن کردن ضد ویس

/UNLOCKV လ خاموش کردن ضد ویس

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/GAMES" or msg.get("text")=="بازی":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
											💠 | 𝓖𝓐𝓜𝓔𝓢: 

/JRAT လ بازی جرعت حقیقت

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""", message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="/JRAT" or msg.get("text")=="ج ج" or msg.get("text")=="جرعت قیقت" or msg.get("text")=="جرعت و حقیقت":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,f"""
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
											""", message_id=msg.get("message_id"))
											bot.sendMessage(group_guid,f'سوالات فرستاده شده اند با کلمه (بپرس) ربات از شما سوال میپرسد.', message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="بپرس" or msg.get("text")=="پرسش":
									if msg.get('author_object_guid') != bot_guid:
										try:
											rando = ["۱۱۸🔓تاحالا احساس کردی یکی روت کراش زده باشه؟","۱۱۹🔓اگه یکی رو ناراحت ببینی چیکار میکنی؟","۱۲۰🔓بی رحمی یا دلت زود به رحم میاد؟","۱۲۱🔓تاحالا پیش کسی گوزیدی؟","۱۲۲🔓تاحالا خودتو خیس کردی؟","۱۲۳🔓اگه بیدار شی ببینی یکی خوابیده روت واکنشت چیه؟","۱۲۴🔓اگه روی یه صندلی کیک باشه یکیش کیر باشه،رو کدوم میشینی و کدومو میخوری؟","۱۲۵🔓جنسیتتو دوس داری عوض کنی؟","۱۲۶🔓دوس داری بری سربازی؟","۱۲۷🔓عکس یهوی بده؟","۱۲۸🔓شام دعوتت کنم قبول میکنی؟","۱۲۹🔓اگه همین الان بهت بگم دوست دارم واکنشت چیه؟","۱۰۰🔓اگه یه نفر مزاحم ناموست بشه باهاش چجوری رفتار میکنی؟","۱۰۱🔓شمارتو بده","۱۰۲🔓چقد آرایش میکنی؟","۱۰۳🔓پسر بازی رو دوس داری؟","۱۰۴🔓دختر بازی رو دوس داری؟","۱۰۵🔓اگه یه کص مفتی گیرت بیاد بازم پسش میزنی؟😁👍🏻","۱۰۶🔓پشمالو دوس داری؟🤧","۱۰۷🔓دوس داری شوهر آیندت چجوری باشه؟","۱۰۸🔓دوس داری زن آیندت چجوری باشه؟","۱۰۹🔓دوس داری چند تا بچه داشته باشی؟","۱۱۰🔓قشنگ ترین اسم پسر بنظرت؟","۱۱۱🔓قشنگ ترین اسم دختر بنظرت؟","۱۱۲🔓من خوشگلم یا زشت؟","۱۱۳🔓خوشگل ترین پسر گپ کیه؟","۱۱۴🔓خوشگل ترین دختر گپ کیه؟","۱۱۵🔓کی صداش از همه زیباتره؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۷🔓خوشتیپ هستی یا خوش قیافه؟","۸۰🔓سیگار یا قلیون میکشی؟","۸۱🔓منو میبری خونتون؟","۸۲🔓میذاری بیام خونتون؟","۸۳🔓تاحالا شکست عشقی خوردی؟💔","۸۴🔓اگه به زور شوهرت بدن تو چیکار میکنی؟","۸۵🔓اگه به زور زنت بدن تو چیکار میکنی؟","۸۶🔓تاحالا با پسر غریبه خوابیدی؟","۸۷🔓تاحالا با دختر غریبه خوابیدی؟","۸۸🔓با همجنست خوابیدی؟","۸۹🔓مدرسه یا گوشی؟","۹۰🔓سر کار میری؟","۹۱🔓کلن اخلاقت چجوریه؟","۹۲🔓هنوز پرده داری؟😐","۹۳🔓قلقلکی هستی؟","۹۴🔓سکس خشن دوس داری یا ملایم؟","۹۵🔓کصکش ناله های دختر مردمو میخوای ببینی😐⚔","۹۶🔓چند بار سوتی میدی؟","۹۷🔓مواظب کصت باش تا بیام بگیرمت باشه؟🤭👍🏻","۹۸🔓تاحالا مچ عشقتو موقع لب بازی با یه دختر دیگه گرفتی؟","۹۹🔓تاحالا مچ عشقتو موقع لب بازی با یه پسر دیگه گرفتی؟","۶۰🔓پیش کسی ضایع شدی؟","۶۱🔓از مدرسه فرار کردی؟","۶۲🔓میخوای چند سالگی ازدواج کنی؟","۶۳🔓اگه مامان و بابات اجازه ندن با عشقت ازدواج کنی چیکار میکنی؟","۶۴🔓چند سالگی پ....ری....و..د شدی؟😶","۶۵🔓وقتی پریودی چجوری هستی؟","۶۶🔓رنگ مورد علاقت؟","۶۷🔓غذای مورد علاقت؟","۶۸🔓پولدارین یا فقیر؟","۶۹🔓دوس داری با من بری بیرون؟","۷۰🔓منو بوس میکنی؟☺️😚","۷۱🔓منو میکنی؟😬","۷۲🔓س...ک...س چت داشتی؟","۷۳🔓خوشت میاد از س....ک.....س؟","۷۴🔓خجالتی هستی یا پررو؟","۷۵🔓دوس داری بکنمت؟🤤","۷۶🔓تاحالا کسی برات خورده؟😁","۷۷🔓من ببوسمت خوشحال میشی؟","۷۸🔓خفن ترین کاری که تا الان کردی؟","۷۹🔓آرزوت چیه؟","۳۰🔓خاستگار داری؟عکسش یا اسمش","۳۱🔓به کی اعتماد داری؟","۳۲🔓تاحالا با کسی رفتی تو خونه خالی؟","۳۳🔓چاقی یا لاغر؟","۳۴🔓قد بلندی یا کوتاه؟","۳۵🔓رنگ چشمت؟","۳۶🔓رنگ موهات؟","۳۷🔓موهات فرفریه یا صاف و تا کجاته؟","۳۸🔓تاریخ تولدت؟","۳۹🔓تاریخ تولد عشقت؟","۴۰🔓عشقت چجوری باهات رفتار میکنه؟","۴۱🔓با دوس پسرت عشق بازی کردی؟🤤","۴۲🔓پیش عشقت خوابیدی؟","۴۳🔓عشقتو بغل کردی؟","۴۴🔓حاضری ۱۰ سال از عمرتو بدی به عشقت؟","۴۵🔓مامان و بابات چقد دوست دارن؟","۴۶🔓دعوا کردی؟","۴۸🔓چند بار کتک زدی؟","۴۹🔓چند بار کتک خوردی؟","۵۰🔓تاحالا تورو دزدیدن؟","۵۱🔓تاحالا کسی ل..خ....ت تورو دیده؟🤭","۵۲🔓تاحالا ل...خ...ت کسیا دیدی؟","۵۳🔓دست نام....حرم بهت خورده؟","۵۴🔓دلت برا کی تنگ شده؟","۵۵🔓دوس داشتی کجا بودی؟","۱🔓عاشق شدی؟اسمش❤️","۲🔓رل زدی تاحالا؟اسمش","۳🔓کراش داری؟اسمش","۴🔓چند بار تا الان رابطه جنسی داشتی؟با کی😐💦","۵🔓از کی خوشت میاد؟","۶🔓از کی بدت میاد؟","۷🔓منو دوس داری؟بهم ثابت کن","۸🔓کی دلتو شکونده؟","۹🔓دل کیو شکوندی؟","۱۰🔓وقتی عصبانی هستی چجوری میشی؟","۱۱🔓دوس داری کیو بزنی یا بکشی؟","۱۲🔓دوس داری کیو بوس کنی؟😉💋","۱۳🔓از تو گالریت عکس بده","۱۴🔓از مخاطبینت عکس بده","۱۵🔓از صفحه چت روبیکات عکس بده","۱۶🔓لباس زیرت چه رنگیه؟🙊","۱۷🔓از وسایل آرایشت عکس بده","۱۷🔓از وسایل آرایشت عکس بده","۱۸🔓از لباسای کمدت عکس بده","۱۹🔓از کفشات عکس بده","۲۰🔓تالا بهت تجاوز شده؟😥","۲۱🔓تاحالا مجبور شدی به زور به کسی بگی دوست دارم؟","۲۲🔓تاحالا یه دخترو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۴🔓با کی ل....ب گرفتی؟😜","۲۵🔓خود ار.ض..ای..ی کردی؟😬💦"]
											renn= choice(rando)
											bot.sendMessage(group_guid, renn , message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text")=="کال" or msg.get("text")=="ایجاد کال" or msg.get("text")=="/call":
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.startVoiceChat(group_guid)
											bot.sendMessage(group_guid,f'✅ با موفقیت ایجاد شد', message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text").startswith("مونو"):
									if msg.get('author_object_guid') != bot_guid:
										try:
											bot.sendMessage(group_guid,textMono, metadata=[{"from_index": 0,"length": len(metn),"type":"Mono"}], message_id=msg.get("message_id"))
										except: pass
								elif msg.get("text").startswith("اپدیت قوانین")or msg.get("text").startswith("آپدیت قوانین")or msg.get("text").startswith("update_rules"):
									 try:
									 	if msg.get('author_object_guid') in admins :
									 		if msg.get('author_object_guid') != bot_guid :
									 			
									 			new_rules=msg.get("text").replace("آپدیت قوانین ","").replace("اپدیت قوانین ",'').replace("update_rules ","")
									 			
									 			open('rulse.txt','w+')
									 			g=open('rulse.txt','a')
									 			g.write(f'{new_rules}')
									 			g.close()
									 			
									 			bot.sendMessage(group_guid,f'قوانین با موفقیت بروز شد!', message_id=msg.get("message_id"))
									 except: pass
							elif msg.get('text').startswith("ربات روشن") or msg.get('text').startswith("/ON"):
								try:
									if msg.get('author_object_guid') in admins and msg.get('author_object_guid') != bot_guid:
										if start_bot == False:
											start_bot=True
											bot.sendMessage(group_guid,f" ‌ربات با موفقیت روشن شد!",message_id=msg.get("message_id"))
										else:
											bot.sendMessage(group_guid,f"‌ربات از قبل روشن بود!(:",message_id=msg.get("message_id"))
								except:pass
					except:pass


			elif msg['type'] != 'Text':
				try:
					try:
						#locked Gif...
						if  msg['file_inline']['type']=="Gif":
							try:
								if msg.get("message_id") not in answered  and lock_Gif == False:
									for giif in open('gif_learn.json',"r").read().split("\n"):
										gof=giif.split(":")
										if str(msg['file_inline']['file_id']) == str(gof[0]):
											pasGif=choice(gof[1].split(","))
											bot.sendMessage(group_guid,f"{pasGif}",message_id=msg.get("message_id"))
											answered.append(msg.get("message_id"))
							except:pass
							if lock_Gif == True:
								if msg.get("author_object_guid") not in admins:
									bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
					except:pass
							#locked forwarded...
					if "forwarded_from" in msg.keys():
						if lock_Forward == True:
							zedForward(msg)
							#locked Image
					elif msg['file_inline']['type'] == 'Image':
						if lock_Image == True:
							if msg.get("author_object_guid") not in admins:
								bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
								#locked Video...
					elif msg['file_inline']['type'] == 'Video':
						if lock_Video == True:
							if msg.get("author_object_guid") not in admins:
								bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
								#locked Voice...
					elif msg['file_inline']['type'] == 'Voice':
						if lock_Voice == True:
							if msg.get("author_object_guid") not in admins:
								
								bot.deleteMessages(group_guid, [str(msg.get("message_id"))])
					
				except:pass
	except:pass
