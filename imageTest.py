import sys
import numpy as np
import cv2
from openalpr import Alpr
import json

alpr = Alpr("us", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(1)
alpr.set_default_region("us")

#cap = cv2.VideoCapture("http://91.190.227.198/mjpg/video.mjpg")
cap = cv2.VideoCapture("numPlates.mpg")
count = 0
countNumber= 4
while(True):    
    #ret, frame = cap.read() 

    if True:        
        #cv2.imshow('frame', frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        
        #cv2.imwrite("img.jpg", frame)

        results = alpr.recognize_file("namcd/img" + str(countNumber) + ".jpg")

        i = 0
        countNumber = countNumber + 1
        print(json.dumps(results))
        #print('-----------------------------')
        # if(len(results['results']) == 0):
        #     pathFile = "namcd/img" + str(count) +".jpg"
        #     print(pathFile)
        #     # cv2.imwrite(pathFile, frame)
        #     count = count + 1 
        for plate in results['results']:
            i += 1
            conner = plate["coordinates"]
            #print(json.dumps(conner))
            # if(conner):
            #     cv2.line(frame,(conner[0]["x"],conner[0]["y"]),(conner[1]["x"],conner[1]["y"]),(255,0,0),1)
            #     cv2.line(frame,(conner[1]["x"],conner[1]["y"]),(conner[2]["x"],conner[2]["y"]),(255,0,0),1)
            #     cv2.line(frame,(conner[2]["x"],conner[2]["y"]),(conner[3]["x"],conner[3]["y"]),(255,0,0),1)
            #     cv2.line(frame,(conner[3]["x"],conner[3]["y"]),(conner[0]["x"],conner[0]["y"]),(255,0,0),1)
            # else:
            #     print("khong duoc")
            # if(len(conner) == 0):
            #     print("awdawdawd")
            #print("Plate #%d" % i)
            #print("   %12s %12s" % ("Plate", "Confidence"))
            for candidate in plate['candidates']:
                prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"
                #print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
            if (len(plate['candidates']) > 0):
                break
        if (countNumber >= 27):
            break
        # cv2.imshow('frame', frame)
    else:
        break

    

# When everything done, release the capture
cap.release()
alpr.unload()
cv2.destroyAllWindows()
