import requests
import time
import json
#from bs4 import BeautifulSoup

while True: # 开始循环
    t = str(int(time.time())) #获取时间戳
    h1 = 'https://service-3ncp55qk-1301649787.gz.apigw.tencentcs.com/release/?account=hzlg301240217&promise=%E6%88%91%E4%BC%9A%E5%A5%BD%E5%A5%BD%E5%AD%A6%E4%B9%A0&ts='
    h2 = '&from=github'
    url2 = h1 + t + h2 #暴力拼接
    print (t)


    if __name__ == '__main__':
        url = url2
        #伪装头信息
        header = {"User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
        req = requests.get(url=url,headers = header) #返回爬取网站信息
        req.encoding = 'gbk'  #查看head中charset编码信息
        html = req.text #转化为文本
        print(html)

    data = json.loads(html)
    signature = data[0]["signature"] #将signature作为一个键来获取值
    print(signature) # 打印结果

    f = open("license.txt", "w") #准备写入
    f.write(signature) # 把signature的值写入到文件中
    f.close() # 关闭文件
    print ('done')

    time.sleep(80) # 暂停80秒后继续循环
