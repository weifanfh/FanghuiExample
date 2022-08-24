from multiprocessing import Process
def test(interval):
    print('我是子进程')
def main():
    print('主进程开始')
    p = Process(target = test, args = (1, ))
    p.start()
    print('主进程结束')
if __name__=='__main__':
    main()
