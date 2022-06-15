#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

nmap_address='192.168.12.'
nmap_command='nmap -p80 -sS '
ip_mac_scan=[]
diccionario={}

def cargar_datos():
    for i in range(80,81):
        address=str(nmap_address+str(i))
        address_key=address.replace('.','')
        address_command=str(nmap_command+address)
        br_addmac=os.popen(address_command)
        linea=[]
        for j in br_addmac.readlines():
            if j != '\n':
                h=j.replace('\n',' ').replace('(', 'Marca: ').replace(')','').replace('Nmap scan report for ','')
                linea.append(h)
        ip=linea[1]
        mac=linea[5]
    diccionario [address_key] = ip,mac

def into_mysql():
    



cargar_datos()

print(diccionario)
