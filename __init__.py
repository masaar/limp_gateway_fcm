# Ancora Imparo.

from config import Config

from pyfcm import FCMNotification

def send_fcm(registration_id, message_title, message_body, data_message):
	push_service = FCMNotification(api_key=Config.vars['fcm']['token'])
	notification = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body, data_message=data_message)
	return notification

def config():
	return {
		'version':5.8,

		'gateways':{
			'fcm':send_fcm
		}
	}