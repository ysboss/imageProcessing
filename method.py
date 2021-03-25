import numpy as np 
import cv2

def process(image, lowGray, highGray):
    img = cv2.imread(image)
    
    # Cuts off irrelevant part, only keep the tube.
    img = img[1950:2100, :5200]
    height, width, c = img.shape
    
    # Converts the image from RGB to grayscale.
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Stores the average pixel value of each column. 
    means = []
    
    # Stores the diff of the average pixel value of left side [0, x-1] and 
    # the average pixel value of right side [x+1, n] at the position x. 
    #
    # Example: for a 5 column image, means = [10,18,30,50,70], at the position 2
    # (means[2] = 30), the diff = (50 + 70) / 2 - (10 + 18) / 2 = 46.
    diffs = []

    # Calculates the average pixel value for each column. 
    for i in range(width):
        values = []
        for j in range(height):
            value = int(img_gray[j, i])
            if(value > lowGray and value < highGray):
                values.append(value)
        means.append(int(np.mean(values)))

    # Calculates the diff of the average pixel value of left side [0, x-1] and 
    # the average pixel value of right side [x+1, n] at the position x.
    for index in range(1, len(means)):
        left = []
        right = []
        for i in range(index):
            left.append(means[i])
        for j in range(index, len(means)):
            right.append(means[j])
        diffs.append(int(np.mean(right)) - int(np.mean(left)))

    # Gets the largest diff value.
    largest = max(diffs)
    
    # Gets the frist index of the largest diff value in diffs. 
    total = diffs.index(largest)
    
    # The number of the largest diff value.
    amount = 1
    
    # Calculates how many columns have the largest diff value in a 30 width. 
    # (30 is a reasonable range cause the width of the water interface is less 
    #  than 30 typically)
    for i in range(diffs.index(largest), diffs.index(largest) + 30):
        # Finds a column has the largest diff value, adds its index to 'total' 
        # increments 'amount' by 1.
        if(diffs[i] == largest):
            total+=i
            amount+=1

    # Returns the image and the index of the most possible water interface.
    return (image, int(total/amount))

# Draws a red line at the column 'pos' and saves the image.
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
def saveImage(image, pos):
    img = cv2.imread(image)
    height, width, c = img.shape
   
    # Draws a red(0,0,255) line from (pos, 0) to (pos, height) with thickness of 5 px.
    img = cv2.line(img, (pos,0), (pos,height), (0,0,255), 5)
    cv2.imwrite('images_final/'+image[16:], img)
    #cv2.imshow('new', img)
    #cv2.waitKey()


#############################################################################
#############################################################################
#############################################################################

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
