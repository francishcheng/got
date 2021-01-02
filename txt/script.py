"""
en原版 章节前加*
"""

import os
with open('en.txt', encoding='utf-8') as f:
    cnt = 0
    cnt_ = 0
    duplicate = open('en_dub.txt', 'w', encoding='utf-8')
    for line in f.readlines():
        if line=='\n':
            cnt = cnt+1
        else:
            if cnt==5:
                print(line)
                
                line = '*'+line
                cnt_ = cnt_ + 1
            cnt = 0
        duplicate.write(line)
    duplicate.close()
print(cnt_)