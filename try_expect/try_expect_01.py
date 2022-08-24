def main():
    a = 10
    b = '10'
    try:
        print(a + b)
        print(b)
    # except TypeError as e:
    #     print('输入错误：', e)
    except: #TypeError as e:
        print('输入错误：')
    print(a)
main()


