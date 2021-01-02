cn = open('cn.txt', encoding='utf-8')
en = open('en.txt', encoding='utf-8')

cn_lines = list(cn.readlines())
en_lines = list(en.readlines())
cn_len = len(cn_lines)
en_len = len(en_lines)
with open('en_cn.txt', 'w', encoding='utf-8') as f:
        for i in range(en_len):
            f.write(en_lines[i])
            f.write(cn_lines[i])
        for j in range(i, cn_len):
            f.write(cn_lines[j])
cn.close()
en.close()