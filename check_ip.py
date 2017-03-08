#coding=utf-8 
def check_ip(address):
    add = address.split('.')
    if len(add) != 4: #必须4位
        print u"位数不对"
        return None

    for i in range(4):
        try:
            add[i] = int(add[i]) #转换成整形
        except:
            print u'不要有空着的谢谢'
            break

        if add[i] <= 255 and add[i] >= 0: #ip地址必须处于0-255之间
            pass
        else:
            print u'每位请填0-255谢谢'

    else:
        print u'ip地址合法'


check_ip("10.0.0.1")

# 或者直接使用socket.inet_aton() 函数
