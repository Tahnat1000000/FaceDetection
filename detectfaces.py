import os, cv2, time, shutil

face_cascade = cv2.CascadeClassifier("cascades\haarcascade_frontalface_alt.xml")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
original_image_dir = os.path.join(BASE_DIR, "images")
faces_found_dir = os.path.join(BASE_DIR, "facesfound")

shutil.rmtree(faces_found_dir)
os.mkdir(faces_found_dir)

photos_detected, faces_detected = 0, 0
for root, dirs, files in os.walk(original_image_dir):
    for file in files:
        photos_detected += 1

        image_path = os.path.join(root,file)
        image = cv2.imread(image_path)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(grayImage, scaleFactor=1.15, minNeighbors=1, minSize=(25,25))

        # CREATING NEW FOLDER WITH THE ORIGINAL IMAGE NAME FOR THE FACES THAT WILL BE FOUND
        newImageDir = os.path.join(BASE_DIR, "facesfound", file.split(".")[0])
        os.mkdir(newImageDir)

        i=1
        for (x,y,w,h) in faces:  # SAVE IMAGES OF ALL FACES FOUND
            faces_detected+=1

            cv2.imwrite(os.path.join(newImageDir,str(i)+".png"), image[y:y+h,x:x+w])
            i += 1

print("Pictures Detected: " + str(photos_detected))
print("Faces Detected: " + str(faces_detected))

time.sleep(30)

