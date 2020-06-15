# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
from datetime import datetime

import bluetooth._bluetooth as bluez

class Device():
	def __init__(self, mac, udid, major, minor, power, rssi, ultima_vez_visto):
		self.mac = mac
		self.udid = udid
		self.major = major
		self.minor = minor
		self.power = power
		self.rssi = rssi
		self.ultima_vez_visto = ultima_vez_visto
		
	def __str__(self):
		return self.mac + ',' + self.udid + ',' + self.major + ',' + self.minor + ',' + self.power + ',' + self.rssi + ',' + str(self.ultima_vez_visto)

def mac_esta_na_lista(mac, devices):
	for i, device in enumerate(devices):
		if device.mac == mac:
			return True, i
	return False, -1

detected_devices = []

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "Deteccao Iniciada!"

except:
	print "Erro ao acessar dispositivo bluetooth"
	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	try:
		returnedList = blescan.parse_events(sock, 10)
		for beacon in returnedList:
			#print beacon
			
			params = beacon.split(',')
			mac = params[0]
			udid = params[1]
			major = params[2]
			minor = params[3]
			power = params[4]
			rssi = params[5]
			ultima_vez_visto = datetime.now()
			
			ta_na_lista, i = mac_esta_na_lista(mac, detected_devices)
			if ta_na_lista:
				detected_devices[i].major = major
				detected_devices[i].minor = minor
				detected_devices[i].power = power
				detected_devices[i].rssi = rssi
				detected_devices[i].ultima_vez_visto = ultima_vez_visto
			else:
				detected_devices.append(Device(mac, udid, major, minor, power, rssi, ultima_vez_visto))
				
		print "\n----------" + str(datetime.now()) + '----------'
		print 'Dispositivos detectados: '+ str(len(detected_devices))
		print '\nMAC,UDID,MAJOR,MINOR,POWER,RSSI,ULTIMA_VEZ_VISTO'
		for detected_device in detected_devices:
			print detected_device
		print '----------------------------------------------'
		
	except KeyboardInterrupt:
		break