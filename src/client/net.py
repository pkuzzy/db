import urllib


'''
sent(s): 用于和服务器交互
协议：发送，返回((/)为多选一的一项)
注册：register username password, (ok/exist)
登录：login username password, (user/admin/wrong)
查看订单信息：dingdan username, username
查看账户信息：zhanghu username, username
租车：zuche user bikeid, (ok/used/not_exist/one_bike_only/no_money)
还车：huanche user time, money
充值：chongzhi user money, money
删除用户：shanchu user, (ok/not_exist)
增加单车：jiache ID info, (ok/exist)
删除单车：shanche ID, (ok/not_exist)
查询单车：chache ID, ((ok info)/not_exist)
'''
def sent(s):
    s = s.split()
    if s[0] == "register":
        return "ok"
    elif s[0] == "login":
        if s[1] != "admin":
            return "user"
        else:
            return "admin"
    elif s[0] == "dingdan":
        return s[1]
    elif s[0] == "zhanghu":
        return s[1]
    elif s[0] == "zuche":
        return "ok"
    elif s[0] == "huanche":
        return "ok " + s[2]
    elif s[0] == "chongzhi":
        return s[2]
    elif s[0] == "shanchu":
        return "ok"
    elif s[0] == "jiache":
        return "ok"
    elif s[0] == "shanche":
        return "ok"
    elif s[0] == "chache":
        return "ok " + s[1]
