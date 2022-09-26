#coding=utf-8
import requests
import re

max_searchpage = 20
currentpage = 0
defaultpath = "pictures"
needsave = 0

def image_filer(content):
    return re.findall('"objUrl":"(.*?)"', content, re.S)

def next_source(content):
    next = re.findall('<div id="page">.*<a href="(.*?)" class="n">', content, re.S)[0]
    print("___________________" +"http://image.baidu.com" + next)
    return next
'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%A4%AA%E9%98%B3%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=0&spn=0&di=7136437450519347201&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3447420258%2C1913331054&os=1611167360%2C99750263&simid=3447420258%2C1913331054&adpicid=0&lpn=0&ln=1749&fr=&fmq=1664212115899_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimg.lanrentuku.com%2Fimg%2Fallimg%2F2002%2F15824262085093.jpg%26refer%3Dhttp%3A%2F%2Fimg.lanrentuku.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1666804260%26t%3D6e712dcd445c976845078285cd2f4b45&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bswg6jgp7h7_z%26e3Bv54AzdH3Fejvp56AzdH3Fvw6p55gAzdH3Fhwp5g21wywg3tg2pwtywg2-fitstwg2_z%26e3Bip4s&gsm=100000000000001&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCwzLDYsNCwxLDUsOCw3LDIsOQ%3D%3D'
'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CC%AB%D1%F4%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDYsNCwxLDUsOCw3LDIsOQ%3D%3D'
def spidler(source):
    content = requests.get(source).text
    image_arr = image_filer(content)
    global currentpage
    print("current page:" + str(currentpage) + "*******************")
    for image_url in image_arr:
        print(image_url)
        global needsave
        if needsave:
            global defaultpath
            try:
                picture = requests.get(image_url, timeout = 10)
            except:
                print("download image error!errorurl:" + image_url)

            image_url = image_url.replace("/", "").replace(":", "").replace("?", "")
            picture_save_path = defaultpath + image_url
            with open(picture_save_path, "wb") as fp:
                print("保存文件")
                fp.write(picture.content)
    global max_searchpage
    if currentpage <= max_searchpage:
        if next_source(content):
            currentpage +=1
            spidler("http://image.baidu.com" + next_source(content))
def begin_search(page = 1, save = 0 , savepath = "pictures/"):
    global max_searchpage, next_source, defaultpath
    max_searchpage = page
    needsave = save
    defaultpath = savepath
    key = input("请输入你想要搜索的内容：")
    start_source = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+str(key)+"&ct=201326592&v=flip"
    spidler(start_source)
begin_search(page = 2, save = 1, savepath = r'D:\Files\FangHuiExampleSource\pachong')