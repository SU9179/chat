
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: 
#讀取同一資料夾的檔案  去掉開頭的空格要加上-sig
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] 
    #時間的長度一致，字串可以當作是清單，所以可以用[:5]來取出
    name = s[0][5:]
    print(name)