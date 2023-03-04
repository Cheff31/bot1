import telebot
from telebot import types
import sqlite3
#свои функции
import rec_file
import sql_req
###################################################

# Создаем экземпляр бота
bot = telebot.TeleBot()

# Подключаем базу SQL 
sqlite_connection = sqlite3.connect('baza.db' , check_same_thread=False) 
cursor = sqlite_connection.cursor() 

# Сохраняем список комманд в переменную
hello_open = open('hello.txt', encoding='utf-8')         
hello = hello_open.read()
hello_open.close()

####################################################

# Команда /start
@bot.message_handler(commands=['start'])                                                     
def start(message, res=False):                                                               
    
    #кнопка "начать"
    inMurkup = types.InlineKeyboardMarkup(row_width=1)
    button_start = types.InlineKeyboardButton(">>Начать", callback_data='b_start')
    inMurkup.add(button_start) 

    # приветствуем пользователя , список комманд 
    bot.send_message(message.chat.id, text =  "Привет, {0.first_name}. \nМеня зовут {1.first_name}. \nЯ помогу тебе с выбором места, куда можно сходить. \nНажми >>Начать".format(message.from_user, bot.get_me()), reply_markup=inMurkup)

# /kitchen 
@bot.message_handler(commands=['kitchen'], func=lambda message: True)
def kitchen(message):
    if message.chat.type == 'private':
        inMurkup = types.InlineKeyboardMarkup(row_width=3)
        b1 = types.InlineKeyboardButton("Русская", callback_data='rus')
        b2 = types.InlineKeyboardButton("Итальянская", callback_data='ita')
        b3 = types.InlineKeyboardButton("Греческая", callback_data='grc')
        b4 = types.InlineKeyboardButton("Турецкая", callback_data='tur')
        b5 = types.InlineKeyboardButton("Грузинская", callback_data='geo')
        b6 = types.InlineKeyboardButton("Европейская", callback_data='eur')
        b7 = types.InlineKeyboardButton("Французская", callback_data='fre')
        b8 = types.InlineKeyboardButton("Сербская", callback_data='ser')
        b9 = types.InlineKeyboardButton("Индийская", callback_data='ind')
        b10 = types.InlineKeyboardButton("Украинская", callback_data='ukr')
        b11 = types.InlineKeyboardButton("Мексиканская", callback_data='mex')
        b12 = types.InlineKeyboardButton("Американская", callback_data='usa')
        b13 = types.InlineKeyboardButton("Азиатская", callback_data= 'asia')

        inMurkup.add(b1, b2, b3 , b4, b5, b6, b7, b8, b9, b10, b11, b12, b13)

        bot.send_message(message.chat.id, "Выберите кухню:", reply_markup=inMurkup)




# Команда /restoran
#@bot.message_handler(commands=['restoran'], func=lambda message: True)   
#def choice_rest(message): 
#    if message.chat.type == 'private':
#        inMurkup = types.InlineKeyboardMarkup(row_width=3)
#        b1 = types.InlineKeyboardButton("Японская", callback_data='jap')
#        b2 = types.InlineKeyboardButton("Итальянская", callback_data='ita')
#        b3 = types.InlineKeyboardButton("Греческая", callback_data='grc')
#        b4 = types.InlineKeyboardButton("Русская", callback_data='rus')
#        inMurkup.add(b1, b2, b3 , b4 )
#
#        bot.send_message(message.chat.id, "Выберите кухню:", reply_markup=inMurkup)

#Комманда /bar
@bot.message_handler(commands=['bar'], func=lambda message: True)   
def bar(message):
    # Проверка что ресторан есть в базе
    com = 'bar'
    cursor.execute(sql_req.sql_count_rest(com))
    count = cursor.fetchone()
    i_count = int(count[0])
    cursor.execute(sql_req.sql_restlist(com))
    rec_file.recfiles(cursor.fetchall())

    cursor.execute(sql_req.sql_list1(com))
    
    bot.send_message(message.chat.id, t, reply_markup=None)



#Обработка различных комманд 
@bot.message_handler(commands=['test'], func=lambda message: True)
def help(message):
    bot.send_message(message.chat.id, "В разработке:")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:                                                             
        if call.data == 'b_start':                                               
            bot.send_message(call.message.chat.id, text = hello ,reply_markup=None)         
#--Начало выбора по кухни 
######## rus
        elif call.data == 'rus':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
######## ita
        elif call.data == 'ita':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
######## grc
        elif call.data == 'grc':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
####### tur
        elif call.data == 'tur':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
####### geo
        elif call.data == 'geo':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
####### eur
        elif call.data == 'eur':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)
####### fre
        elif call.data == 'fre':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None) 
####### ser 
        elif call.data == 'ser':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None) 
####### ind
        elif call.data == 'ind':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)  
#######
        elif call.data == 'ukr':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None) 
####### mex
        elif call.data == 'mex':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None) 
####### usa
        elif call.data == 'usa':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None) 
####### jap
        elif call.data == 'jap':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)         
####### kor
        elif call.data == 'kor':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)     
####### china
        elif call.data == 'china':
            cursor.execute(sql_req.sql_restlist(call.data))
            rec_file.recfiles(cursor.fetchall())
            cursor.execute(sql_req.sql_list1(call.data))
            t = ' \n '.join(map(str,  cursor.fetchall()))
            bot.send_message(call.message.chat.id, t, reply_markup=None)  
#--Конец выбора по кухни
## asia
        elif call.data == 'asia':
            inMurkup = types.InlineKeyboardMarkup(row_width=1)
            b1 = types.InlineKeyboardButton("Японская", callback_data='jap')
            b2 = types.InlineKeyboardButton("Корейская", callback_data='kor')
            b3 = types.InlineKeyboardButton("Китайская", callback_data='china')
            inMurkup.add(b1, b2, b3 )

            bot.send_message(call.message.chat.id, text = "Выберите кухню:", reply_markup=inMurkup)



#обработка callback
#@bot.callback_query_handler(func=lambda call: True)
#def callback_inline(call):
#    if call.message:                                                             
#        if call.data == 'b_start':                                               
#        	bot.send_message(call.message.chat.id, text = hello ,reply_markup=None)         
#        #rus
#        elif call.data == 'rus':
#            cursor.execute(sql_req.sql_restlist(call.data))
#            rec_file.recfiles(cursor.fetchall())
#            cursor.execute(sql_req.sql_list1(call.data))
#            t = ' \n '.join(map(str,  cursor.fetchall()))
#            bot.send_message(call.message.chat.id, t, reply_markup=None)
#
#        elif call.data == 'jap': 
#            #cursor.execute(sql_req.sql_restlist(call.data))
#            #rec_file.recfiles(cursor.fetchall())
#            #cursor.execute(sql_req.sql_list(call.data))
#            ##Записать в файл результат sql запроса
#            #rec_file.files(cursor.fetchall())
#            #f = open('temp/temp.txt' , 'r')  
#            #bot.send_message(call.message.chat.id, f.read(), reply_markup=None) 
#            #f.close()
#            cursor.execute(sql_req.sql_restlist(call.data))
#            rec_file.recfiles(cursor.fetchall())
#            #
#            cursor.execute(sql_req.sql_list1(call.data))
#            t = ' \n '.join(map(str,  cursor.fetchall()))
#            bot.send_message(call.message.chat.id, t, reply_markup=None) 
#        elif call.data == 'grc': 
#            cursor.execute(sql_req.sql_restlist(call.data))
#            rec_file.recfiles(cursor.fetchall())
#            cursor.execute(sql_req.sql_list(call.data))
#            rec_file.files(cursor.fetchall())
#            f = open('temp/temp.txt' , 'r')  
#            bot.send_message(call.message.chat.id, f.read(), reply_markup=None) 
#            f.close()
#        elif call.data == 'ita':
#             bot.send_message(call.message.chat.id, text = "Упс", reply_markup=None) 
        
            

    
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'], func=lambda message: True)
def handle_text(message):
    if message.chat.type == 'private':
            inMurkup = types.InlineKeyboardMarkup(row_width=1)
### Добавить оценки Проверка на сделал ли оценку пользователь (insert table) 
### Добавить ссылку на пост (если есть) 
            b1 = types.InlineKeyboardButton("<<Вернуться в начало", callback_data='b_start')
            inMurkup.add(b1)
    # Проверка что ресторан есть в базе 
    x = rec_file.search_name(message.text)
    if x == 0: 
        # собираем адреса 
        cursor.execute(sql_req.sql_adr(message.text))
        rec_file.files(cursor.fetchall())
        f = open('temp/temp.txt' , 'r')  
        # собираем телефон и url
        cursor.execute(sql_req.sql_telurl(message.text))
        tel = ' : '.join(map(str, cursor.fetchone()))
        bot.send_message(message.chat.id, text ="Контакты: " + tel + "\nАдрес: \n" +  f.read() , reply_markup=inMurkup)
        f.close()
    else:
        if message.chat.type == 'private':
            inMurkup = types.InlineKeyboardMarkup(row_width=1)
            b1 = types.InlineKeyboardButton("<<Вернуться в начало", callback_data='b_start')
            inMurkup.add(b1)

        bot.send_message(message.chat.id, text = "Ой. что-то пошло не так" , reply_markup=inMurkup)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
