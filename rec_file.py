#Записть в файл результата
def files(base):
    f = open('temp/temp.txt' , 'w')
    for item in base:
        f.write("%s\n" % item)
    f.close()

def recfiles(base):
    f = open('rest/tab_list.txt' , 'w')
    for item in base:
        f.write("%s\n" % item)
    f.close()


def search_name(word):
    file = open('rest/tab_list.txt', 'r')      
    # т.к. лист создается по умолчанию с новой строки добавил \n
    c = word + "\n" #переименовать после файл для таблиц
    for line in file:      
        if  c == line or word == line: #оставил Word т.к. последнее слово в списке без Новой строки 
            x = 0
            file.close()
            return x
        else:
            continue
            

def calls(cd):
    cursor.execute(sql_req.sql_list(cd))
    #Записать в файл результат sql запроса
    rec_file.files(cursor.fetchall())
    f = open('temp/temp.txt' , 'r')  
    bot.send_message(call.message.chat.id, f.read(), reply_markup=None) 
    f.close()

   