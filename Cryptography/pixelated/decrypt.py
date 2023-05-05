import cv2
img1 = cv2.imread('scrambled1.png')
img2 = cv2.imread('scrambled2.png')

width = img1.shape[0]
height = img1.shape[1]

dst = img1.copy()
for i in range(0, width):
    for j in range(0, height):
        dst[i][j][0] = (img1[i][j][0] + img2[i][j][0])%256
        dst[i][j][1] = (img1[i][j][1] + img2[i][j][1])%256
        dst[i][j][2] = (img1[i][j][2] + img2[i][j][2])%256

cv2.imwrite('dst.jpg',dst)
