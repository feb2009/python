import sys
with open(sys.argv[1], 'r')as f:
    isUser = False
    activeUser = list()
    for i in f.readlines():
        line = i.strip()
        if line == '':
            continue
        if line[0] == '#':
            continue

        elif line == '[users]':
            isUser = True
        elif isUser == True:
            if line[0] == '[':
                isUser = False
            else:
                activeUser.append(line.split(' = ')[0])
    for i in activeUser:
        print i