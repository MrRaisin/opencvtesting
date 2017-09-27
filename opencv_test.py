import io
import picamera
import cv2
import numpy
import time

def captureImage():
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)

    #Load a cascade file for detecting faces
    #face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
    face_cascade = cv2.CascadeClassifier('/home/pi/Documents/Python_Projects/opencv/haarcascade_frontalface_default.xml')
    #face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print ("Found "+str(len(faces))+" face(s)")

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

    #Save the result image (updated below)
    #cv2.imwrite('result.jpg',image)

    #show image
    cv2.imshow('img',image)

    k = cv2.waitKey(0)
    if k == 27: # wait for the ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for the 's' key to save and exit
        cv2.imwrite('result.jpg',image)
        cv2.destroyAllWindows()


def validateMenuChoice(string, chars):
    return True in [c in string for c in chars]

def menu():
    print('1. Take a picture & detect your face')
    print('2. Recognise a car number plate')
    print('3. Quit')
    valid = False
    while not valid:
        choice = input('Please enter your option: ')
        if not validateMenuChoice(choice, '123'):
            print('Invalid option, choose 1, 2 or 3')
        else:
            if choice == '1':
                print('Counting down... 3')
                time.sleep(0.95)
                print('             ... 2')
                time.sleep(0.95)
                print('             ... 1')
                time.sleep(0.95)
                print('press ESC key to return to menu')
                # now the capture    
                captureImage()
            elif choice == '2':
                print('Sorry I\'m still working on this functionality :-)')
            else:
                print('Bye Bye')
                exit()

        menu()
        valid = True

menu()
