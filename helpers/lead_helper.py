# -*- coding: utf-8 -*-
from connection.db_connection import DBConnection
from helpers.telegram_helper import TelegramHelper
import datetime
import calendar
import time
from flask import Flask,redirect, render_template


class LeadHelper:
    def __init__(self):
        self.db = DBConnection()
        self.connection = self.db.get_connection()

    def str_to_bool(self, string):
        if string == 'True':
             return True
        elif string == 'False':
             return False

    def get_file_name(self, filename):
        ts = calendar.timegm(time.gmtime())
        filename = str(ts)+filename
        return filename


    def insert_lead(self, name, email, necessity, enterprise, role, state, city, phone, celphone, origin, alert):
        cursor = self.connection.cursor()
        now = datetime.datetime.utcnow()
        sql    = "INSERT INTO lead (name, email, necessity, enterprise, role, state, city, phone, celphone, origin, date_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val    = (name, email, necessity, enterprise, role, state, city, phone, celphone, origin, now)
        cursor.execute(sql, val)
        self.connection.commit()
        print(cursor.rowcount, "lead inserted.")
        alert = self.str_to_bool(alert)
        if(alert):
            th = TelegramHelper()
            th.broadcast_alert("Novo+Lead: ")

        return "200"

    def compute_access(self, origin):
        cursor = self.connection.cursor()
        sql    = "SELECT access_amount FROM campaing WHERE origin = '%s'" % origin
        cursor.execute(sql)
        amount = cursor.fetchall()
        amount = amount[0][0]
        new_amount = int(amount) + 1
        self.update_acess(origin, new_amount)

        return str(new_amount)

    def update_acess(self, origin, amount):
        cursor = self.connection.cursor()
        sql = "UPDATE campaing SET access_amount = '%s' WHERE origin = '%s'" % (amount, origin)
        cursor.execute(sql)
        self.connection.commit()

    def formata_inscricao():
        pass

    def nova_inscricao(self, data, historico, diploma, curriculo):

        try:
            cursor = self.connection.cursor()
            now = datetime.datetime.utcnow()

            sql = "INSERT INTO inscricao (nome_completo, data_nascimento, rg, cpf, celular, email, \
            rua, numero, bairro, estado, cidade, cep, complemento, escolaridade, formacao, foco_aulas, \
            caminho_historico, caminho_diploma, lingua_estrangeira, assinatura, link_aula, caminho_curriculo,\
            link_lattes, date_time) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            val = (data['nome_completo'], data['data_nascimento'], data['rg'], data['cpf'],\
            data['celular'], data['email'], data['rua'], data['numero'], data['bairro'],\
            data['estado'], data['cidade'], data['cep'], data['complemento'], data['escolaridade'],\
            data['formacao'], data['foco_aulas'], historico, diploma,\
            data['lingua_estrangeira'], data['assinatura'], data['link_aula'], curriculo,\
            data['link_lattes'], now)

            try:
                cursor.execute(sql, val)
                self.connection.commit()
                print(cursor.rowcount, "inscricao realizada.")
                th = TelegramHelper()
                msg = ("Nova+Inscricao:+Nome:+%s+e-mail+%s") % (data['nome_completo'].split(" ")[0], data['email'])
                th.broadcast_alert(msg)
                return True
            except Exception as e:
                print ("Não foi possivel realizar a operação: %s") % (e)
                return False
        except:
            return False
