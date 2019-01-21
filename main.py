import os
from method import process, saveImage

with open('results5.txt', 'w') as fd:
    #for file in os.walk('settling_column'):
        # imgPath = 'settling_column/' + file
        # result = process(imgPath, 20, 220)
        # line = result[0]image + ' ' + str(result[1]) + '\n'
        # print (line)
        #fd.write(line)
    
    files = os.listdir('settling_column')
    files.sort()
    files.pop(0)
    for file in files:
        imgPath = 'settling_column/' + file
        result = process(imgPath, 20, 220)
        saveImage(result[0], result[1])
        line = result[0] + ' ' + str(result[1]) + '\n'
        print (line)
        fd.write(line)
fd.close()

# results.txt :   20,220
# results2.txt:   15,235
# results3.txt:   no mean for largest
# results4.txt:   1950:2200,  20,220
# results5.txt:   1950:2100,  20,220

