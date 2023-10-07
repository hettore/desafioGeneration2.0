from flask import request, jsonify
from mysql.connector import (connection)
import mysql.connector


def criando_aluno():
        obj = request.json
        values = (obj['nome'], obj['idade'], obj['nota_1_semestre'], obj['nota_2_semestre'], obj['nome_professor'], obj['numero_da_sala'])
        conn = mysql.connector.connect(host='localhost', user='root', password='12345', database='alunos')
        cursor = conn.cursor()
        sql_insert = "INSERT INTO resumo_aluno (nome,idade,nota_1_semestre,nota_2_semestre,nome_professor,numero_da_sala) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_insert, (values))
        obj_id = cursor.lastrowid
        aluno = {
                "id":obj_id,
                "nome": obj['nome'],
                "idade": obj['idade'],
                "nota_1_semestre":obj['nota_1_semestre'],
                "nota_2_semestre": obj['nota_2_semestre'],
                "nome_professor": obj['nome_professor'],
                "numero_da_sala": obj['numero_da_sala']
                }
        conn.commit()
        print(aluno)
        print(values)
        print(obj_id)
        conn.close()
        return aluno

def retornando_alunos():
        resultado = []
        
        conn = mysql.connector.connect(host='localhost', user='root', password='12345', database='alunos')

        cursor = conn.cursor()
        sql_select = "SELECT * FROM resumo_aluno"
        cursor.execute(sql_select)
        alunos = cursor.fetchall()
        conn.close()
        for item in alunos:
            alunos = {
                         'id': item[0],
                         'nome': item[1],
                         'idade': item[2],
                         'nota_1_semestre': item[3],
                         'nota_2_semestre': item[4],
                         'nome_professor': item[5],
                         'numero_da_sala': item[6]
                       }
            resultado.append(alunos)
        return resultado

def retornando_aluno(id:int):
        conn = connection.MySQLConnection(host='localhost', user='root', password='12345', database='alunos')
        cursor = conn.cursor()

        sql_select = "SELECT * FROM resumo_aluno WHERE id = %s"
        cursor.execute(sql_select, (id, ))
        id, nome, idade, nota_1_semestre, nota_2_semestre, nome_professor, numero_da_sala = cursor.fetchone()
        conn.close()
        return {
                "id":id,
                "nome": nome,
                "idade": idade,
                "nota_1_semestre": nota_1_semestre,
                "nota_2_semestre": nota_2_semestre,
                "nome_professor": nome_professor,
                "numero_da_sala": numero_da_sala
                }

def atualizar_aluno(id:int, nome, idade, nota_1_semestre, nota_2_semestre, nome_professor, numero_da_sala):
    try:
        #Tentar atualizar
        conn = connection.MySQLConnection(host='localhost', user='root', password='12345', database='alunos')
        cursor = conn.cursor()
        sql_update = "UPDATE resumo_aluno SET nome = %s, idade = %s, nota_1_semestre = %s, nota_2_semestre = %s, nome_professor = %s, numero_da_sala = %s WHERE id = %s"
        cursor.execute(sql_update, (nome, idade, nota_1_semestre, nota_2_semestre, nome_professor, numero_da_sala, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
    #Remove um resumo de aluno
def remover_aluno(id:int):
    try:
        conn = connection.MySQLConnection(host='localhost', user='root', password='12345', database='alunos')
        cursor = conn.cursor()
        sql_delete = "DELETE FROM resumo_aluno WHERE id = %s"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False