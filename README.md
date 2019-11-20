# SkyWalkingAlarm
配合SkyWalking实现钉钉告警

## 需要在钉钉群创建机器人，获取secret和access_token
1. 打开钉钉群，在群管理处添加机器人
2. 选择自定义机器人---通过WebHook介入自定义服务
3. 安全设置选择加签，拷贝secret：SEC939d3c4e1a8ac539632abb4d0514f00ebb512c4ad75a3923daeca9cc325c566d
4. 点击完成即可看到钉钉webhook连接地址 https://oapi.dingtalk.com/robot/send?access_token=becd2d0c6392b8f6bdcb868fc7be9e48d1
4.配置代码中需要替换的参数即可

## python版本3.6

