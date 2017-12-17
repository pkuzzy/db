#coding=utf-8
import easygui as g
import net
import time
import threading


'''
user.main(user): 用户界面，user表示用户名
'''
def main(user):
    while True:
        retval = g.buttonbox(msg=("尊敬的%s您好，欢迎使用共享单车，请选择您的操作"%user),
                             title="用户程序",
                             choices=("租车", "充值", "查询"))
        if retval == "租车":
            zuche(user)
        elif retval == "充值":
            chongzhi(user)
        elif retval == "查询":
            chaxun(user)
        else:
            break
    return


'''
zuche(user): 租车界面， 最长租借maxTime(s)的时间，否则会有还车提醒
net发送: zuche user bikeid
net返回: ok/used/not_exist/one_bike_only/no_money
'''
def zuche(user):
    maxTime = 10
    fieldval = g.enterbox("请输入您要租的单车编号",title="租车界面")
    while True:
        if fieldval == None:
            break
        errmsg = ""
        if fieldval.strip() == "":
            errmsg += "单车号不能为空  "
        if errmsg == "":
            retval = net.sent("zuche " + user + " " + fieldval)
            if retval == "ok":

                def jishi():
                    time.sleep(maxTime)
                    if not finish:
                        g.msgbox("您已经使用了很长时间，请还车", title="系统消息")

                finish = False
                t1 = threading.Thread(target=jishi)
                t1.setDaemon(True)
                t1.start()

                begin_time = time.time()
                g.msgbox(msg="租车成功，到达目的地后请还车，祝您使用愉快",
                         title="系统消息", ok_button="确定")
                finish = True
                end_time = time.time()

                huanche(user, int(end_time - begin_time + 1 - 1e-10))
                break
            elif retval == "used":
                errmsg = "该车已经被人租借"
            elif retval == "not_exist":
                errmsg = "该编号不存在"
            elif retval == "broken":
                errmsg = "该车已经损坏"
            elif retval == "one_bike_only":
                errmsg = "您一次只能租一辆车"
            elif retval == "no_money":
                errmsg = "您已经欠费，请您充值"
        fieldval = g.enterbox(errmsg, title="租车界面")
    return


'''
huanche(user): 还车界面
net发送: huanche user time
net返回: ok
'''
def huanche(user, time):
    retval = net.sent("huanche " + user + " " + str(time))
    g.msgbox(msg=("还车成功，扣款%s元，请支付"%retval),
             title="系统消息", ok_button="支付")
    return


'''
chongzhi(user): 充值界面
net发送: chongzhi user money
net返回: money
'''
def chongzhi(user):
    fieldval = g.enterbox("请输入您要充值的金额", title="充值")
    while True:
        if fieldval == None:
            break
        errmsg = ""
        try:
            if float(fieldval) == 0:
                errmsg += "请输入合法的金额数  "
        except:
            errmsg += "请输入合法的金额数  "
        if errmsg == "":
            retval = net.sent("chongzhi " + user + " " + fieldval)
            g.msgbox(msg="充值成功，现在您的账户余额是%s"%retval, title="系统消息")
            break
        fieldval = g.enterbox(errmsg, title="租车界面")
    return


'''
zhanghu(user): 账户信息
net发送: zhanghu user
net返回: user 
'''
def zhanghu(user):
    content = net.sent("zhanghu " + user).split()
    s = ""
    s += "用户名: " + content[0] + "\n"
    s += "用户类型: " + content[1] + "\n"
    s += "账户余额: " + content[2] + "\n"
    g.textbox(msg=("账户信息:"), title="账户信息", text=s)


'''
dingdan(user): 订单信息
net发送: dingdan user
net返回: user
'''
def dingdan(user):
    content = net.sent("dingdan " + user)
    res = "用户名: " + user + "\n\n"
    for s in content.strip().split("\n"):
        s2 = s.split()
        res += "订单号: " + s2[0] + "\n"
        res += "单车号: " + s2[1] + "\n"
        res += "是否仍在租借: " + s2[3] + "\n"
        res += "\n"
    g.textbox(msg=("订单信息"), title="订单信息", text=res)


def sousuo(user):
    retval = g.buttonbox(msg="你需要哪种搜索?", title="搜索", choices=\
    ("完成订单数量最多的用户",
     "每个行政区内，共享单车数低于区域内街道平均共享单车数的街道",
     "对于在某个街道内有骑行记录的用户，找出这些用户的总消费金额",
     "附近单车"))
    print retval
    if retval == "完成订单数量最多的用户":
        result = net.sent('sousuo 1')
    elif retval == "每个行政区内，共享单车数低于区域内街道平均共享单车数的街道。":
        result = net.sent('sousuo 2')
    elif retval == "对于在某个街道内有骑行记录的用户，找出这些用户的总消费金额。":
        result = net.sent('sousuo 3')
    elif retval == "附近单车":
        dins = "shenghuo"
        street = "dajie"
        result = "nearby bike ID: " + net.sent('fujin %s %s' % (dins, street))
    g.textbox(msg=("搜索结果"), title="搜索结果", text=result)

'''
chaxun(user): 查询界面
'''
def chaxun(user):
    while True:
        retval = g.buttonbox(msg=("尊敬的%s您好，欢迎使用查询功能，请选择您的查询类别"%user),
                             title="查询",
                             choices=("订单信息", "账户信息", "搜索"))
        if retval == "订单信息":
            dingdan(user)
        elif retval == "账户信息":
            zhanghu(user)
        elif retval == "搜索":
            sousuo(user)
        else:
            break
    return
