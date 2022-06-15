#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host='localhost',
			user='motivation',
			password='C4bbbcSCBaf0qfKmow',
			db='motivation'
		)
		self.cursor=self.connection.cursor()
	def select_cam_id(self, id):
		sql='SELECT id, ip, mac FROM camaras WHERE  {}'.format(id)
		print(sql)
		try:
			self.cursor.execute(sql)
			self.cursor.fetchone()
		except Exception as e:
			raise
	def update_cam_id(self, id, mac):
		sql="UPDATE camaras SET mac='{}' WHERE {}".format(mac,id)
		print(sql)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise
	def closed_connect(self):
		self.connection.close()


id='1921681280'

mac='13:13:13:13:13:13'

DataBase.select_cam_id(id='1921681380')