from Api_DataTime.data import datetime as irTime
from Api_DataTime.time import timezone
def hourIran():
		try:
			ir = timezone("Asia/Tehran")
			return irTime.now(ir).strftime("%H : %M : %S")
		except: pass
def historyIran():
		try:
			ir = timezone("Asia/Tehran")
			return irTime.now(ir).strftime("%Y / %m / %d")
		except: pass