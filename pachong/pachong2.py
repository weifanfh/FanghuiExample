#coding=utf-8
import urllib.request
import re
key_name = urllib.request.quote("双肩包")
print(key_name)
def save_file(data):
    path = r"C:\Users\weifanfh\Desktop\taobao_url.text"

    with open(path, "a") as file:
        file.write(data + "\n")
for p in range(0, 6):
    url = "https://s.taobao.com/search?q="+key_name+"&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_"+str(p+20170306)
    print(url)
    data1 = urllib.request.urlopen(url).read().decode("utf-8")
    print(data1)
    save_file(url)
    pat = '"pic_url":"//(.*?)"'
    img_url = re.compile(pat).findall(data1)
    print(img_url)
    for a_i in range(0, len(img_url)):
        this_img = img_url[a_i]
        this_img_url = "http://" + this_img
        print(this_img_url)
        img_path = r"D:\Files\FangHuiExampleSource\pachong\pic" + str(p) + str(a_i) + ".jpg"
        urllib.request.urlretrieve(this_img_url, img_path)