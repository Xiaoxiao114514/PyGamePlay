import urllib.request
import requests
import urllib.parse
import json
import time
import random
import hashlib
import tkinter
from tkinter import ttk

text = ""

# 清空输入框
def qing_kong(shu_ru):
    shu_ru.delete(0, tkinter.END)

# 确定开始查询
def que_ding(a, b, content, shu_chu):
    global text
    # content = input('请输入需要翻译的内容：')
    # from_s = input("请输入待翻译的语种，中文请输入ZH,英文请输入EN：")
    # to_s = input("请输入目标语种，中文请输入ZH,英文请输入EN：")
    if a == "汉语":
        from_s = 'ZH'
    else:
        from_s = 'EN'
    if a == "英语":
        to_s = 'EN'
    else:
        to_s = 'ZH'

    # url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}

    u = 'fanyideskweb'
    d = content
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'

    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    data['i'] = content
    data['from'] = from_s
    data['to'] = to_s
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = f
    data['sign'] = sign
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'true'

    data = urllib.parse.urlencode(data).encode('utf-8')

    res = requests.post(url, data=data)
    request = urllib.request.Request(url=url, data=data, method='POST')
    response = urllib.request.urlopen(request)

    # print(response.read().decode('utf-8'))
    pre_js = response.read().decode('utf-8')

    # pat=re.compile(r'[\u4e00-\u9fa5]+')
    # result=pat.findall(pre_js)
    # result = '\n'.join(result[5:])

    a = pre_js.split('[[')
    b = a[1].split(']]')
    c = b[0]

    j = json.loads(c)
    text = j['tgt']
    shu_chu.set(text)
    print(j['tgt'])
    # for i in result:
    #    print(i+'\n')
    # print(pre_js)


# 主函数
def jie_main():
    global text
    win = tkinter.Tk()
    win.title("翻译")
    win.geometry("500x400")
    win.resizable(0, 0)

    shu_chu = tkinter.StringVar()
    shu_chu.set(text)

    tkinter.Label(win, text='翻译', font=('Arial', 12)).place(x=100, y=30, anchor='nw')

    tkinter.Label(win, text='翻译语言选项', font=('Arial', 12)).place(x=10, y=70, anchor='nw')
    yu_yan1 = ttk.Combobox(win, width=10)
    yu_yan1['value'] = ('汉语', '英语')
    yu_yan1.current(0)
    yu_yan1.place(x=120, y=70, anchor='nw')
    tkinter.Label(win, text='>>>>>', font=('Arial', 12)).place(x=220, y=70, anchor='nw')
    yu_yan2 = ttk.Combobox(win, width=10)
    yu_yan2['value'] = ('英语', '汉语')
    yu_yan2.current(0)
    yu_yan2.place(x=270, y=70, anchor='nw')

    tx1 = tkinter.Label(win, text='原文：', font=('Arial', 12))
    tx1.place(x=10, y=120, anchor='nw')
    shu_ru = tkinter.Entry(win)
    shu_ru.place(x=120, y=120, anchor='nw')
    guess = shu_ru.get()

    tx2 = tkinter.Label(win, text='译文：', font=('Arial', 12))
    tx2.place(x=10, y=160, anchor='nw')
    tkinter.Label(win, textvariable=shu_chu, font=('Arial', 12)).place(x=100, y=160, anchor='nw')

    bt1 = tkinter.Button(win, text='清空', command=lambda: qing_kong(shu_ru))
    bt1.place(x=10, y=210, anchor='nw')
    bt2 = tkinter.Button(win, text='确定', command=lambda: que_ding(yu_yan1.get(), yu_yan2.get(), shu_ru.get(), shu_chu))
    bt2.place(x=100, y=210, anchor='nw')

    win.mainloop()


if __name__ == '__main__':
    jie_main()