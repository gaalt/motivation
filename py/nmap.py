#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nmap as np
rango_ip='192.168.12-13.90-92'
class ScanMap:
    def __init__(self):
        self.discover = np.PortScanner()
    def scan_camaras(self,rango_ip):
        comand='-sS -p80 -v {}'.format(rango_ip)
        self.discover.scan(comand)
ScanMap.scan_camaras(rango_ip)