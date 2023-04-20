import threading
import time

#  普通版
# def sing():
#     while True:
#         print("我在唱歌，，")
#         time.sleep(1)
# def dance():
#     while True:
#         print("我在跳舞，，")
#         time.sleep(1)

def sing():
    while True:
        print("我在唱歌，，")
        time.sleep(1)
def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # sing_thread = threading.Thread(target=sing)
    # dance_thread = threading.Thread(target=dance)

    # 带args版,args是元组，单个元素末尾要加都好
    # sing_thread = threading.Thread(target=sing)
    # dance_thread = threading.Thread(target=dance,args = ("一起跳舞吧",))

    # 带kargs版,字典
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance,kwargs = {"msg":"一起跳舞吧"})

    sing_thread.start()
    dance_thread.start()