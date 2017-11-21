from enum import Enum
class NetRouter_Handler:
	FSM = Enum('FSM_STATES',('DISCONNECT','BUSY','READY'))

	def __init__(self,device_drive):
		self.__device = device_drive # set device
		self.__device.setup() # device setup
		self.FSM_state = NetRouter_Handler.FSM.READY # change state
		print(type(self.FSM_state))

<---- ---->
from netRouter import NetRouter_Handler
import e3372_drive

LTE_Dongle = NetRouter_Handler(e3372_drive)
print(LTE_Dongle.FSM_state)
if LTE_Dongle.FSM_state == LTE_Dongle.FSM.READY:
	print('Yes!')