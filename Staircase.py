def staircase(n):
    for index in range(n):
        lineText = ''
        spaceCount = n-1-index
        for space in range(spaceCount):
            lineText = lineText + ' '
        for stair in range(index+1):
            lineText = lineText + '#'
        print(lineText)