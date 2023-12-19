img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
newArray = []
for i in range(len(img)):
    newRow = []
    for j in range(len(img[i])):
        sum = 0
        counter = 0
        # top left
        if j - 1 >= 0 and i - 1 >= 0:
            counter += 1
            sum += img[i - 1][j - 1]
        # top
        if i - 1 >= 0:
            counter += 1
            sum += img[i - 1][j]
        # top right
        if j + 1 < len(img[i]) and i - 1 >= 0:
            counter += 1
            sum += img[i - 1][j + 1]
        # right
        if j + 1 < len(img[i]):
            counter += 1
            sum += img[i][j + 1]
        # left
        if j - 1 >= 0:
            counter += 1
            sum += img[i][j - 1]

        # bottom left
        if j - 1 >= 0 and i + 1 < len(img):
            counter += 1
            sum += img[i + 1][j - 1]
        # bottom
        if i + 1 < len(img):
            counter += 1
            sum += img[i + 1][j]
        # bottom right
        if j + 1 < len(img[i]) and i + 1 < len(img):
            counter += 1
            sum += img[i + 1][j + 1]
        # current
        sum += img[i][j]
        counter += 1
        newRow.append(sum // counter)
    newArray.append(newRow)
print(newArray)
