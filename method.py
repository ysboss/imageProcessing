import numpy as np 
import cv2

def process(image, lowGray, highGray):
    img = cv2.imread(image)
    img = img[1950:2100, :5200]
    height, width, c = img.shape
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    means = []
    diffs = []

    for i in range(width):
        values = []
        for j in range(height):
            value = int(img_gray[j, i])
            if(value > lowGray and value < highGray):
                values.append(value)
        means.append(int(np.mean(values)))

    for index in range(1, len(means)):
        left = []
        right = []
        for i in range(index):
            left.append(means[i])
        for j in range(index, len(means)):
            right.append(means[j])
        diffs.append(int(np.mean(right)) - int(np.mean(left)))

    largest = max(diffs)
    total = diffs.index(largest)
    amount = 1
    for i in range(diffs.index(largest), diffs.index(largest) + 30):
        if(diffs[i] == largest):
            total+=i
            amount+=1

    return (image, int(total/amount))

# def write2file(imgIndex, pos):
#     with open('result.txt', 'w') as fd:
#         line = imgIndex + ', ' + pos + '\n'
#         fd.write


def saveImage(image, pos):
    img = cv2.imread(image)
    height, width, c = img.shape
    img = cv2.line(img, (pos,0), (pos,height), (0,0,255), 5)
    cv2.imwrite('images_final/'+image[16:], img)
    #cv2.imshow('new', img)
    #cv2.waitKey()


# img = cv2.imread('settling_column/MFDC6201.JPG')
# #img = cv2.resize(img, None, None, 0.3, 0.3)
# print(img.shape)

# height, width, c = img.shape

# img = img[2000:2500, :5200]
# height, width, c = img.shape

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# means = []
# with open('compare.txt', 'w') as fd:
#     for i in range(width):
#         #diffs = []
#         values = []
#         for j in range(height):
#             #diff = abs(img_gray[j, col] - img_gray[j, i])
#             value = int(img_gray[j, i])
#             if ( value > 20 and value < 220 ):
#                 values.append(value)
#             #values.append(value)
#         means.append(int(np.mean(values)))
#         line = str(int(np.mean(values))) + '\n'
#         fd.write(line)
# fd.close()

# diffs = []
# with open('diffs.txt', 'w') as fd1:
#     for index in range(1, len(means)):
#         left = []
#         right = []
#         for i in range(index):
#             left.append(means[i])
#         for j in range(index, len(means)):
#             right.append(means[j])
    
#         diffs.append(int(np.mean(right)) - int(np.mean(left)))

#         line = str(int(np.mean(right)) - int(np.mean(left))) + '\n'
#         fd1.write(line)
# fd1.close()



# largest = max(diffs)
# total = diffs.index(largest)
# amount = 1
# for i in range(diffs.index(largest), diffs.index(largest) + 30):
#     if(diffs[i] == largest):
#         total+=i
#         amount+=1

# print (diffs.index(largest))
# print (int(total/amount))


    




    # if(means[index] - means[index - 30] > 40):
    #     print (index)
    #     break


# img_x = cv2.Sobel(img_gray, cv2.CV_16S, 1, 0, None, 3)
# img_absx = cv2.convertScaleAbs(img_x)
# img_canny = cv2.Canny(img_gray, 100, 120)

# with open('compare.txt', 'w') as fd:
#     for i in range(height):
#         #line = str(img_gray[i, 3000]) + ',' + str(img_gray[i, 6000]) + '\n'
#         line = str(img_gray[i, 5000] - img_gray[i, 3000]) + '\n'
#         fd.write(line)

# fd.close()

# col = 5200    

# with open('compare.txt', 'w') as fd:
#     for i in range(col):
#         diffs = []
#         for j in range(height):
#             diff = abs(img_gray[j, col] - img_gray[j, i])
#             if ( diff < 230 ):
#                 diffs.append(diff)
#         line = str(int(np.mean(diffs))) + '\n'
#         fd.write(line)

# fd.close()
    
# mean = []
# with open('compare.txt', 'w') as fd:
#     for i in range(col):
#         diffs = []
#         for j in range(height):
#             diff = abs(int(img_gray[j, col]) - int(img_gray[j, i]))
#             if ( diff < 230 ):
#                 diffs.append(diff)
#         mean.append((int(np.mean(diffs))))
#         line = str(int(np.mean(diffs))) + '\n'
#         fd.write(line)
        
# fd.close()

# index = []
# for idx in range(100, len(mean)):
#     if(mean[idx - 100] - mean[idx] > 25):
#         print (idx)
#         index.append(idx)

#     length = len(index)

#     if(length > 2):
#         if(index[length - 1] - index[length - 2] > 100):
#             index.pop()
#             break


# print ('***********')
#print (int(np.mean(index)))

# img[width, height, k], k = 0, 1, 2 = blur, green, red
# img.shape = (height, width, 3)


# img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)



# cv2.imshow('img_gray', img_gray)
# cv2.imshow('img_lab', img_lab)
# cv2.imshow('img_absx', img_absx)
# # cv2.imshow('img_canny', img_canny)
# # cv2.imshow('img', img)
# cv2.waitKey()