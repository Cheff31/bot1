# Тестириуем код для sql запроса 
def sql_adr(cond):
    sqlq = "SELECT adr"  \
        + " FROM adress "   \
        + " WHERE key" \
        + " = " + kav(cond)
    return sqlq

def sql_list(cond): 
    sqlq = "SELECT fullname FROM new " \
        + "WHERE keys = '" + cond + "'"
    return sqlq

def sql_list1(cond): 
    sqlq = "SELECT key, name  FROM new1 " \
        + "WHERE rest = '" + cond + "'"
    return sqlq


def kav(word):
    c = "'" + word + "'"
    return c

def sql_restlist(cond):
    sqlq = "SELECT key FROM new1 " \
        + "WHERE rest = '" + cond + "'"
    return sqlq


def sql_telurl(cond):
    sqlq = "SELECT phone , url"  \
        + " FROM new1 "   \
        + " WHERE key" \
        + " = " + kav(cond)
    return sqlq

def sql_count_rest(cond): 
    sqlq = "SELECT count(rest) "  \
        + " FROM new1 "   \
        + " WHERE rest" \
        + " = " + kav(cond)
    return sqlq

#a = "Таблица"
#b = "Поле"
#f = "Поле условия"
#f1= "условия"
#
#print(sql_q(a,b,f,f1))
#

#def test()