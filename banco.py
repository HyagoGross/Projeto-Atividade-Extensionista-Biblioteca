import sqlite3 as conector
from sqlite3 import Error
import os
pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp+"\\banco_biblioteca.db"
def ConexaoBanco():
    conexao=None
    try:
        conexao=conector.connect(nomeBanco,detect_types=conector.PARSE_DECLTYPES)
        conexao.execute("PRAGMA foreign_keys = on")
    except conector.DatabaseError as erro:
        print("Erro no Banco de Dados:", erro)
    return conexao
def dql(query): #select
    vcon=ConexaoBanco()
    cursor=vcon.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    vcon.close()
    return result
def dml(query):#insert, update, delete
    try:
        vcon=ConexaoBanco()
        cursor=vcon.cursor()
        cursor.execute(query)
        vcon.commit()
        vcon.close()
    except Error as erro:
        print("Erro no Banco de Dados:", erro)
def delete_livro(query):#deleta livro
    try:
        vcon=ConexaoBanco()
        cursor=vcon.cursor()
        cursor.execute(query)
        vcon.commit()
        vcon.close()
        return True
    except Error as erro:
        print("Erro no Banco de Dados:", erro)