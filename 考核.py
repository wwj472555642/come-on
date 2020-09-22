txt=input('请输入加密内容：')
x=int(input('请输入偏移量：'))
for new in txt:
    if 'a'<=new<='z':
        print(chr(ord('a')+(ord(new)-ord('a')+x)%26),end='')
    elif'A'<=new<='Z':
        print(chr(ord('A')+(ord(new)-ord('A')+x)%26),end='')
    else:
        print(end='请输入英文语句且不输入符号')
        break