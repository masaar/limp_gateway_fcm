# Ancora Imparo.

from config import Config

from typing import Dict, Any, TypedDict
from pyfcm import FCMNotification

def fcm_gateway(
			registration_id: str,
			message_title: str,
			message_body: str,
			data_message: Dict[str, Any],
			fcm_auth: TypedDict('GATEWAY_FCM_AUTH', token=str)=None
		):
	if not fcm_auth:
		fcm_auth = Config.vars['fcm']
	push_service = FCMNotification(api_key=fcm_auth['token'])
	notification = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body, data_message=data_message)
	return notification

def config():
	return {
		'version':5.8,

		'gateways':{
			'fcm':fcm_gateway
		}
	}