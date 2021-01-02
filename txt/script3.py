import os
chpt_ = 0
with open('cn-1chpt', 'r', encoding='utf-8') as f:
    dub2 = open('cn_dub.txt', 'w', encoding='utf-8')
    for line in f.readlines():
        if line == '\n':
            continue
        dub2.write(line)
    dub2.close()