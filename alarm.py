from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import hmac
import hashlib
import base64
import requests
import json
from urllib.parse import quote_plus

from numpy import long


def dingding_robot(data):
    data = "serving服务异常：" + data
    datas = {
        "msgtype": "text",
        "text": {
            "content": data
        }
    }
    timestamp = long(round(time.time() * 1000))
    secret = 'your secret'
    secret_enc = bytes(secret.encode('utf-8'))
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(hmac_code))
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=your access token&timestamp=%d&sign=%s' % (
    timestamp, sign)
    headers = {'content-type': 'application/json'}
    requests.post(webhook, headers=headers, data=json.dumps(datas))


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("get")

    def do_POST(self):
        req_datas = self.rfile.read(int(self.headers['content-length']))
        print(req_datas.decode())
        req_datas = json.loads(req_datas)
        for req_data in req_datas:
            data = req_data['alarmMessage']
            dingding_robot(data)

if __name__ == "__main__":
    httpd = HTTPServer(('127.0.0.1', 10010), HttpHandler)
    httpd.serve_forever()
