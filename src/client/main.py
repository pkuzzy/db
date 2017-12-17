#coding=utf-8
import easygui as g
import user
import admin
import net


'''
main.main(): 开始菜单，注册或登录，一旦登录成功，进入user或者admin
'''
def main():
    start()


'''
start(): 开始界面，登录或注册
'''
def start():
    while True:
        retval = g.buttonbox("欢迎使用共享单车\n点击图片进入登录界面(新用户请先注册)\n",
                             image="共享单车.jpg",
                             choices=("注册","退出"))
        if retval == "注册":
            register()
        elif retval == "共享单车.jpg":
            login()
            break
        else:
            break


'''
register(): 用户注册(成功后返回start()，即开始的菜单)
net发送: register username password 
net返回: ok exist
'''
def register():
    msg = "请填写一下信息(其中带*号的项为必填项)"
    title = "注册"
    fieldNames = ["*用户名", "*密码"]
    fieldValues = []
    fieldValues = g.multpasswordbox(msg, title, fieldNames)
    while True:
        if fieldValues == None:
            break
        errmsg = ""
        for i in range(len(fieldNames)):
            option = fieldNames[i].strip()
            if fieldValues[i].strip() == "" and option[0] == "*":
                errmsg += ("【%s】为必填项   " % fieldNames[i])
        if errmsg == "":
            retval = net.sent("register " + " ".join(fieldValues))
            if retval == "ok":
                g.msgbox(msg="注册成功", title="系统消息", ok_button="开始使用")
                break
            elif retval == "exist":
                errmsg = "用户名已经存在"
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)


'''
login(): 用户登录(成功后进入user.main()或者admin.main()，即用户界面)
net发送: login username password 
net返回: user admin wrong
'''
def login():
    msg = "请填写用户名密码"
    title = "登录"
    fieldNames = ["用户名", "密码"]
    fieldValues = []
    fieldValues = g.multpasswordbox(msg, title, fieldNames)
    while True:
        if fieldValues == None:
            break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ("请填写【%s】   " % fieldNames[i])
        if errmsg == "":
            retval = net.sent("login " + " ".join(fieldValues))
            if retval == "user":
                user.main(fieldValues[0])
                break
            elif retval == "admin":
                admin.main()
                break
            elif retval == "wrong":
                errmsg = "用户名或者密码错误"
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
    return

if __name__ == "__main__":
    main()
