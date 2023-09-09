# Python study

# Ttutorial em https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html

import datetime
import mysql.connector

def connect_and_find():

    # Abre conexão
    cnx = mysql.connector.connect(host='localhost', database='db_MeusLivros', user='root', password='123')
    cursor = cnx.cursor()
    vals = (datetime.date(1999, 1, 1), 
            datetime.date(1999, 12, 31))

    cursor.execute("SELECT first_name, last_name, birth_date FROM employees "
                "WHERE hire_date BETWEEN %s AND %s",
                vals)

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

    result = cursor.fetchAll()
    cnx.commit()
    cnx.close()
    return result

# :%d %b %Y => dia mês e ano no formato 16 Dec 1999
# %d => valores numéricos, dia do mês com dois dígitos.
# %b => nome do Mês.
# %Y => ano com quatro dígitos.
