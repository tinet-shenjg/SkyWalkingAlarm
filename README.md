# SkyWalkingAlarm
配合SkyWalking实现钉钉告警

## 需要在钉钉群创建机器人，获取secret和access_token

## python版本3.6
```
curl 'https://oapi.dingtalk.com/robot/send?access_token=your access_token' \
   -H 'Content-Type: application/json' \
   -d '{"msgtype": "text", 
        "text": {
             "content": “告警啦，快来看"
        }
      }'
```
