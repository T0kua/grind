from termcolor import *
import time
import os 
import random
import sqlite3
import datetime
div = (__file__[0:-8]) #путь к папке файлом
db = sqlite3.connect(f'{div}server.db',check_same_thread=False)
sql = db.cursor()
db.commit()

#start game
print("выберите запись")
print("==========================================================")
for val in sql.execute(f"SELECT user FROM users"):
	print(f"{val[0]}")
print("==========================================================")
user = None
while user == None :
	user_try = input("")
	sql.execute(f"SELECT user FROM users WHERE user = '{user_try}'")
	if sql.fetchone() is None :
		print("такого пользователя нет, хотите создать нового ? да/нет")
		r = input()
		while r != "да" or r != "нет" :
			r = input()
			if r == "да" :
				sql.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)",(0,1,0,0,0,0,0,user_try,datetime.datetime.today(),datetime.datetime.today()))
				db.commit()
				user = user_try
				break
	else :
		user = user_try
print(f"здраствуйте {user}")

################################################
# functions
##############################################
def send(text,color):
	return colored(f"{text}",f"{color}")
#start
os.system("color 07")
def swet(r): #получение даты
	time = datetime.datetime.today()
	if r == "time" :
		return(time)
	if r == "minute" :
		return(together.seconds // 60)
	if r == "hours" :
		return(together.seconds // 3600)
	if r == "day" :
		return (together.day)
	if r == "month" :
		return (together.day // 30)
	if r == "age":
		return(together.day // 365)

def resurs(user):
	for val in sql.execute(f"SELECT * FROM users WHERE user = '{user}'"):
		resur = (f"""
==========================================================
деньги : [{val[4]} едениц]
==========================================================
дерево : [{val[0]} едениц] скорость [{val[1] * '#'}{(10 - val[1]) * '-'}] 
цена : [1 монета]
==========================================================
камень : [{val[5]} едениц] скорость [{val[6] * '#'}{(10 - val[6]) * '-'}]
цена : [2 монет]
==========================================================
уголь : [{val[2]} едениц] скорость [{val[3] * '#'}{(10 - val[3]) * '-'}]
цена : [5 монеты]
==========================================================

""")
		print(colored(resur,'red'))

def Help():
	print(f"""
помощь - выводит справку о командах 
==========================================================
улучшить - выводит справку о ценах на улучшение добычи ресурса
==========================================================
улучшить [ресурс] - улучшить скорость добычи [ресурс]
==========================================================
продать [ресурс] - продать [ресурс]
==========================================================
""")

def coint():
	for val in sql.execute(f"SELECT date FROM users WHERE user = '{user}'"):
		#'2022-10-25 18:45:03.931371'
		a = val[0]
		a1 = a.split(" ")
		a2 = a1[0].split("-")
		a22 = a1[1].split(":")
		a3 =[int(a2[0]),int(a2[1]),int(a2[2]),int(a22[0]),int(a22[1]),int(float(a22[2]))]
		a = datetime.datetime(a3[0],a3[1],a3[2],a3[3],a3[4],a3[5],)
		b = datetime.datetime.today()
		moment = b - a
		hour = (moment.days * 24) * 60
		munute = moment.seconds  // 60
		moment = hour + munute
		return moment
def coint_start():
	for val in sql.execute(f"SELECT start_session FROM users WHERE user = '{user}'"):
		a = val[0]
	a1 = a.split(" ")
	a2 = a1[0].split("-")
	a22 = a1[1].split(":")
	a3 =[int(a2[0]),int(a2[1]),int(a2[2]),int(a22[0]),int(a22[1]),int(float(a22[2]))]
	a = datetime.datetime(a3[0],a3[1],a3[2],a3[3],a3[4],a3[5],)
	b = datetime.datetime.today()
	moment = b - a
	hour = (moment.days * 24) * 60
	munute = moment.seconds  // 60
	moment = hour + munute
	return moment

def send():
	if r == "продать уголь" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			sql.execute(f"UPDATE users set money = {val[4] + (val[2] * 5)} WHERE user = '{user}'")
			sql.execute(f"UPDATE users set C = {0}")
			db.commit()
	if r == "продать камень" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			sql.execute(f"UPDATE users set money = {val[4] + (val[5] * 2)} WHERE user = '{user}'")
			sql.execute(f"UPDATE users set stone = {0}")
			db.commit()
	if r == "продать дерево" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			sql.execute(f"UPDATE users set money = {val[4] + (val[0] * 1)} WHERE user = '{user}'")
			sql.execute(f"UPDATE users set wood = {0}")
			db.commit()
def update():
	if r == "улучшить дерево" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			if val[4] >= (2 + val[1] * 79) and val[1] + 1 <= 10:
				sql.execute(f"UPDATE users set money = {val[4] - (2 + val[1] * 79)}")
				sql.execute(f"UPDATE users set woodspeed = {val[1] + 1}")
				db.commit()
			else :
				print("недостаточно денег")
	if r == "улучшить камень" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			if val[4] >= (70 + val[6] * 269) and val[6] + 1 <= 10:
				sql.execute(f"UPDATE users set money = {val[4] - (70 + val[6] * 269)}")
				sql.execute(f"UPDATE users set stoneSpeed = {val[6] + 1}")
				db.commit()
			else :
				print("недостаточно денег")
	if r == "улучшить уголь" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			if val[4] >= (800 + val[3] * 1569) and val[3] + 1 <= 10:
				sql.execute(f"UPDATE users set money = {val[4] - (800 + val[3] * 1569)}")
				sql.execute(f"UPDATE users set Cspeed = {val[3] + 1}")
				db.commit()
			else :
				print("недостаточно денег")
####  Game loop
####  Game loop
####  Game loop
print(f"вас не было {coint() // (24*60)} дней {coint() % (24*60)} минут")
print(f"с создания сессии прошло : {coint_start() // (365*(24*60)) } год {coint_start() // (24*60)} дней {coint_start() % (24*60)} минут")
while True:
	for val in sql.execute(f"SELECT * FROM users WHERE user = '{user}'"):
		if coint() != 0 :
			sql.execute(f"UPDATE users set wood='{val[0] + coint() * val[1]}' WHERE user='{user}'")
			sql.execute(f"UPDATE users set C='{val[2] + coint() * val[3]}' WHERE user='{user}'")
			sql.execute(f"UPDATE users set stone='{val[5] + coint() * val[6]}' WHERE user='{user}'")
			sql.execute(f"UPDATE users set date='{datetime.datetime.today()}' WHERE user='{user}'")
			db.commit()
			file = open(f"{div}statistick.txt","r")
			state = file.read()
			file.close
			file = open(f"{div}statistick.txt","w")
			file.write(f"{state}\n{val[7]}|{val[4]}|{val[0]}#{val[1]} |{val[2]}#{val[3]}|{val[5]}#{val[6]}| {val[8]}")
			file.close()
	resurs(user)
	r = input("действие :")
	os.system("cls")
	if r == "помощь" :
		Help()
	elif r == "улучшить" :
		for val in sql.execute(f"SELECT * from users WHERE user = '{user}'"):
			print(f"""
==========================================================
добыча дерева :
скорость [{val[1] * '#'}{(10 - val[1]) * '-'}] 
цена : [{2 + val[1] * 79} монет]
==========================================================
добыча камня :
скорость [{val[6] * '#'}{(10 - val[6]) * '-'}]
цена : [{70 + val[6] * 269} монет]
==========================================================
добыча угля : 
скорость [{val[3] * '#'}{(10 - val[3]) * '-'}]
цена : [{800 + val[3] * 1569} монеты]
==========================================================
\n""")
	elif "улучшить" in r :
		update()
	elif "продать" in r :
		send()