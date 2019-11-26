# LIMP Gateway for Firebase Cloud Messaging (FCM)
This repo is a [LIMP](https://github.com/masaar/limp) [Package](https://github.com/masaar/limp-docs/blob/APIv5.8/api/package.md) for the sole purpose of integrating [FCM](https://firebase.google.com/docs/cloud-messaging) into LIMP apps using [LIMP Gateways](https://github.com/masaar/limp-docs/blob/APIv5.8/api/gateways.md).

## How-to
1. Clone this repo into your LIMP `modules` folder.
2. Add following to your app package config:
```python
'vars':{
	'fcm':{'token':'YOUR_FCM_TOKEN_HERE'}
}
```
3. FCM gateway requires following args:
   1. `registration_id`: Target device registration identifier. Type `str`.
   2. `message_title`: Message title. Type `str`.
   3. `message_body`: Message body. Type `str`.
   4. `data_message`: Additional payload data to be sent with the message. Type `dict`.
4. FCM gateway accepts optional arg, namely `fcm_auth`, replicating `fcm` value in `vars Config Attr` for dynamic FCM API credentials.
5. Use FCM gateway using LIMP Gateway Controller:
```python
from gateway import Gateway

Gateway.send(gateway='fcm', registration_id=registration_id, message_title=message_title, message_body=message_body, data_message=data_message)
```