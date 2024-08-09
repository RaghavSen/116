import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Mercury", (110, 188), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Venus", (190, 276),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Earth", (290, 273), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Mars", (380, 271), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Jupiter", (550, 102), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Saturn", (750, 111),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Uranus", (950, 133),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Neptune", (1100, 132), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)


cv2.imshow("output", img)

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.waitKey(0)




