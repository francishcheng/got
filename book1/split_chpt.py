import os
with open('en_cn.txt', encoding='utf-8') as f:
    lines = f.readlines()
    chp_num = 1
    flag = 0
    f = open('chapter_{chp_num}.txt'.format(chp_num=chp_num), 'w', encoding='utf-8')
    for n, line in enumerate(lines):
        if line.startswith('*'):
            flag = flag+1
        if flag == 2:
            flag = 1
            chp_num = chp_num + 1
            f.close()
            f = open('chapter_{chp_num}.txt'.format(chp_num=chp_num), 'w', encoding='utf-8')
        f.write(line)
try:
    f.close()
except:
    pass