from pandas import read_excel
from random import sample

L = read_excel(r'C:\Users\zy\Desktop\杂七杂八\classmates.xlsx')[
    '姓名'].values.tolist()


def raffle(number: int = 1):
    try:
        return sample(L,number)
    except ValueError:
        return '所抽人数超过总人数'


if __name__ == '__main__':
    print(raffle())
