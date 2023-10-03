"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    persons = [True] * 30
    # counter代表已经扔了几个人
    # number代表人该喊几了
    # index代表排圈的人的顺序
    counter, index, number = 0, 0, 0
    while counter < 15:
        # 若该人还在场
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        print("index+=1:",index)
        # 代表从0-30循环，即使有的人被淘汰，也可以循环到此位置，只是number不再+1，即不报数
        index %= 30
        print("index%=30:",index)

    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()