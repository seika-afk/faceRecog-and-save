from datetime import datetime
import time
import cv2
import face_recognition
import threading
now = datetime.now()
current_time=now.strftime("%H:%M:%S")


        
          
        



known_face_encoding=[]
known_face_names=[]

# load

known_person1_image=face_recognition.load_image_file("C:/Users/vanshika/Desktop/Personal_Stuff/Coding related stuff/Python projects/FaceDetection__/gagan.jpg")
known_person2_image=face_recognition.load_image_file("C:/Users/vanshika/Desktop/Personal_Stuff/Coding related stuff/Python projects/FaceDetection__/r3.jpg")



# face encoding
known_person1_encoding=face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding=face_recognition.face_encodings(known_person2_image)[0]

# making encoding on arrays
known_face_encoding.append(known_person1_encoding)
known_face_encoding.append(known_person2_encoding)
# inputing names
known_face_names.append("gagan")
known_face_names.append("Ullu")

# initializing webcam
cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FORCC,cv2.VideoWriter_fourcc(*"MJPG"))

def start():
    i=0;
    while True:
       
        i+=1;
        # capture frame by frame
        sucess,frame=cam.read()

        # find face location inthe video
        face_locations =face_recognition.face_locations(frame)
        face_encoding=face_recognition.face_encodings(frame,face_locations)
        # loop through each face on frame
        for (top,right,bottom,left),face_encoding in zip(face_locations,face_encoding):
            # check matching of face
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            name="unknown";
            if True in matches:
                first_match_index=matches.index(True)
                name=known_face_names[first_match_index]
    # draw box
            cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)

                    
            
            #    STEPS LEFT
            # 1 make it run every 3 seconds.//making further process to go on ,while this process keeps working in background
            
            if (i % 2==0):
                with open ("names.txt","a+" )as f:
                    f.write(name +" ["+current_time+"] " +"\n")
                    print(name)
       



            #DISPLAYING RESULTING FRAME
            
    
        cv2.imshow("video",frame)
        if cv2.waitKey(10) == ord("q") :
            break

start();

cam.release() 

cv2.destroyAllWindows()

    


















# FACE DETECTION

# face_cap=cv2.CascadeClassifier("C:/Users/vanshika/Desktop/Personal_Stuff/Coding related stuff/Python projects/FaceDetection__/a.xml")

# cam=cv2.VideoCapture(0)

# while True:
#     ret,frame=cam.read()
#     col =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces=face_cap.detectMultiScale(
#         col,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30),
#         flags=cv2.CASCADE_SCALE_IMAGE


#     )

#     for(x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

#     cv2.imshow("Video",frame)
#     if cv2.waitKey(10) == ord("q") :
#         break
# cam.release()

# cv2.destroyAllWindows()

    
