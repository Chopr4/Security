import cv2
import dropbox
import time
import random

start_time = time.time()

def takeSnapshot():
    number = random.randint(0, 100)
    #0 Indicates the default camera
    videoCaptureObject = cv2.VideoCapture(0)

    result = True
    while(result):
        #We'll read the frames whilst the camera is on
        # ret is a dummy varible to check is a value has been returned or not
        # Frame has or stores the the frame of the video
        ret, frame = videoCaptureObject.read()
        
        imageName = "Img"+str(number)+".png"
        #.imwrite() method is used to save an image to any storage device
        cv2.imwrite(imageName, frame)
        start_time = time.time
        result = False
    
    return imageName
    print("snapshotTaken")
    #Release the camera
    videoCaptureObject.release()
    #Close all applications that might be opened or might have opened during the process
    cv2.destroyAllWindows()

def uploadFile(imageName):
    access_token = "Vo4uPvxRDQ0AAAAAAAAAAa8Ucw0l96aeqAs4GpkUnVulcZlEKRqQihVHvj4kZjvu"
    file = imageName
    file_from = file
    file_to = "/testFolder/"+(imageName)
    dbx = dropbox.Dropbox(access_token)


    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")

def main():
    while(True):
        if((time.time()-start_time >=3.76)):
            name = takeSnapshot()
            uploadFile(name)

main()