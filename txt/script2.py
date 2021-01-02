import os
chpt_ = 0
with open('en_dub.txt', 'r', encoding='utf-8') as f:
    dub2 = open('en_dub2.txt', 'w', encoding='utf-8')
    for line in f.readlines():
        if line == '\n':
            continue
        dub2.write(line)
    dub2.close()