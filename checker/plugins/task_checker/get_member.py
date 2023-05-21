from pandas import read_excel
from os import listdir
from os.path import splitext
import re

members = read_excel(r'C:\Users\zy\Desktop\杂七杂八\classmates.xlsx')

def get_member(path:str = r'C:\Users\zy\Desktop\作业检查包\生理系统建模与仿真实验_周二'):
    uncommiteedID = []
    commiteed = listdir(path)
    commiteed_name = []
    wrong_ID = []
    for f in commiteed:
        rule = re.compile(r'\d{10}')
        name = splitext(f)
        ID = rule.search(name[0])
        try:
            commiteed_name.append(members[members['学号'] == int(ID.group())]['姓名'].values[0])
        except IndexError:
            wrong_ID.append(ID.group())
    uncommiteed_name = list(set(members['姓名'].tolist()) - set(commiteed_name))
    for e in uncommiteed_name:
        uncommiteedID.append(members[members['姓名'] == e]['QQ号'].values[0])
    if len(uncommiteedID) == 0:
        return '所有人都提交了', None
    else:
        return uncommiteedID, wrong_ID

if __name__ == '__main__':
    print(get_member(r'C:\Users\zy\Desktop\作业检查包\生理系统建模与仿真实验_周二'))