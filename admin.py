import easygui as g
import user
import net


'''
admin.main(): 管理员界面
'''
def main():
    while True:
        retval = g.buttonbox(msg="尊敬的管理员您好，欢迎使用管理界面，请选择您的操作",
                             title="管理员程序",
                             choices=("管理用户", "管理单车"))
        if retval == "管理用户":
            yonghu()
        elif retval == "管理单车":
            danche()
        else:
            break
    return


'''
yonghu(): 管理用户
删除用户
net发送: shanchu user
net返回: ok/not_exist
'''
def yonghu():
    while True:
        retval = g.buttonbox(msg="您想要对用户做什么？",
                             title="管理用户",
                             choices=("查看账户", "查看订单", "删除用户"))
        if retval == None:
            break
        if retval == "查看账户":
            fieldval = g.enterbox("请输入您要查看的用户名", title="查看账户")
            if fieldval == None:
                continue
            user.zhanghu(fieldval)
        if retval == "查看订单":
            fieldval = g.enterbox("请输入您要查看的用户名", title="查看订单")
            if fieldval == None:
                continue
            user.dingdan(fieldval)
        elif retval == "删除用户":
            fieldval = g.enterbox("请输入您要删除的用户名", title="删除用户")
            if fieldval == None:
                continue
            l = net.sent("shanchu " + fieldval)
            if l == "ok":
                g.msgbox("删除成功", title="管理用户")
            elif l == "not_exist":
                g.msgbox("用户不存在", title="管理用户")
    return


'''
danche(): 管理单车
增加单车
net发送: jiache ID info
net返回: ok/exist
删除单车
net发送: shanche ID
net返回: ok/not_exist
查询单车:
net发送: chache ID
net返回: (ok info)/not_exist
'''
def danche():
    while True:
        retval = g.buttonbox(msg="您想要对单车做什么？",
                             title="管理单车",
                             choices=("增加单车", "删除单车", "查询单车"))
        if retval == None:
            break
        if retval == "增加单车":
            fieldNames = ["ID", "info"]
            fieldValues = []
            fieldValues = g.multenterbox("填写单车信息", "增加单车", fieldNames)
            if fieldValues == None:
                continue
            if net.sent("jiache " + " ".join(fieldValues)) == "ok":
                g.msgbox("增加成功", title="增加单车")
            else:
                g.msgbox("单车已经存在", title="增加单车")
        elif retval == "删除单车":
            fieldNames = ["ID"]
            fieldValues = []
            fieldValues = g.multenterbox("填写单车信息", "删除单车", fieldNames)
            if fieldValues == None:
                continue
            l = net.sent("shanche " + " ".join(fieldValues))
            if l == "ok":
                g.msgbox("删除成功", title="删除单车")
            elif l == "not_exist":
                g.msgbox("单车不存在", title="删除单车")
        elif retval == "查询单车":
            fieldNames = ["ID"]
            fieldValues = []
            fieldValues = g.multenterbox("填写单车信息", "查询单车", fieldNames)
            if fieldValues == None:
                continue
            l = net.sent("chache " + " ".join(fieldValues)).split()
            if l[0] == "ok":
                s = ""
                s += "info: " + l[1] + "\n"
                g.textbox(msg="单车信息如下:", title="单车信息", text=s)
            elif l[0] == "not_exist":
                g.msgbox("单车不存在", title="删除单车")
    return
