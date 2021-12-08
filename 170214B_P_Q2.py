
def linearFilter(mask, img, param):
    offset = len(mask)//2
                          
    if(param == "O" or param == 'S'):
        val = 0
        img.insert(0, [val]*len(img[0]))
        img.append([val]*len(img[0]))
        for row in img:
            row.insert(0, val)
            row.append(val)

    elif(param == "P"):
        whiteOrBlack = 0
        img.insert(0, [whiteOrBlack]*len(img[0]))
        img.append([whiteOrBlack]*len(img[0]))
        for row in img:
            row.insert(0, whiteOrBlack)
            row.append(whiteOrBlack)

    elif(param == "R"):
        img.insert(0, img[0]+[])
        img.append(img[-1]+[])
        for row in img:
            row.insert(0, row[0])
            row.append(row[-1])

    elif(param == "W"):
        img.insert(0, img[-1])
        img.append(img[1])
        for a in range (len(img)-2):
            img[a].insert(0, img[a][-1])
            img[a].append(img[a][1])
        print(img)
    outputImg = []

    for i in range(offset, len(img)-offset):
        outputRow = []
        for j in range(offset, len(img[0])-offset):
            val = 0
            for x in range(len(mask)):
                for y in range(len(mask)):
                    xn = i+x-offset
                    yn = j+y-offset
                    val += (img[xn][yn] * mask[x][y])
            outputRow.append(val)
        outputImg.append(outputRow)

    return outputImg
                                

mask = [[1,1,1],[1,1,1],[1,1,1]]
img = [[9,9,9,9,9],[9,9,9,9,9],[9,9,9,9,9],[9,9,9,9,9],[9,9,9,9,9]]
param = 'W'
out = linearFilter(mask, img, param)
print("------")
for t in out:
    print(t)

