# -*- coding: utf-8 -*-

import jwt
import requests
import base64
import json

# 公開鍵を取得するためにヘッダからkidを取得する
encoded_jwt = input("paste data:")
jwt_headers = encoded_jwt.split('.')[0]
decoded_jwt_headers = base64.b64decode(jwt_headers)
decoded_json = json.loads(decoded_jwt_headers)
kid = decoded_json['kid']

# ALBが提供する公開鍵を取得
url = 'https://public-keys.auth.elb.ap-northeast-1.amazonaws.com/' + kid
#print(url)
req = requests.get(url)
#print(req)
pub_key = req.text

# 公開鍵を使って、ペイロード部をデコード
payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES256'])
print(json.dumps(payload, ensure_ascii=False, indent=4))

email = payload['email']
name = payload['name']
print("email:%s\nname:%s" % (email,name))
