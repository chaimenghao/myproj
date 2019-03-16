#如果在list中既包含字符串，又包含其它类型数据
# 如何修改1中的生成式实现把一个list中所有的字符串变成小写？
# （内建的isinstance(x, str)函数可以判断一个变量是不是字符串）
if __name__ == '__main__':

    L = ['Hello', 'World',1,'IBM', 'Apple',2.25]
    ll = []
    for l in L:
        if isinstance(l,str):
            l = l.lower()
        ll.append(l)
    print(ll)





if __name__ == '__main__':

    L = ['Hello', 'World',1,'IBM', 'Apple',2.25]
    ll = []
    for l in L:
        if isinstance(l,str):
            l = l.lower()
        ll.append(l)
    print(ll)

