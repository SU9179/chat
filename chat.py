def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        #存檔會存入關於編碼的特殊記號，像\ufeff這種BOM(用來標記字節順序)，可以用-sig用掉
        for line in f:
            lines.append(line.strip())
            #.strip() 去除\n換行符號
    return lines

def convert(lines):
    new = []
    person = None  
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: 
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()