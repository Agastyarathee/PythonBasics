import cv2


body_cascade = cv2.CascadeClassifier('Video Full Body Detection\haarcascade_fullbody.xml')


# Initiate video capture for video file
cap = cv2.VideoCapture('Video Full Body Detection/walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    
    # Pass frame to the body classifier
    bodies = body_cascade.detectMultiScale(gray,1.1,5)
    
    
    # Extract bounding boxes for any bodies identified
    
    for (x,y,w,h) in bodies:
       
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       
      
       
    cv2.imshow("Web cam", frame)
    
    if cv2.waitKey(1) == 32: #32 ===> Space Key
        break

height, width, channels = frame.shape

size=(width,height)
print(size)
out=cv2.VideoWriter("walking.mp4",cv2.VideoWriter_fourcc(*'FMP4'),500,size)

out.release()
cap.release()
cv2.destroyAllWindows()
