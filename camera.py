import time
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

class NeckErgo(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.outer_count = 0
        self.inner_count = 0
        self.outer_stopper=180
        self.inner_stopper=1200
    def __del__(self):
        self.video.release()

    def get_frame(self):
        p1,q1,p2,q2=299,226,84,84
        # extracting frames
        ret, frame = self.video.read()
        # time.sleep(0.3)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        print(face_rects)
        for (x1, y1, x2, y2) in face_rects:
            p1,q1,p2,q2=x1,y1,x2+x1,y2+y1
            cv2.circle(frame, (p1, q1), 5, (255, 0, 154), -1)
            cv2.circle(frame, (p2, q2), 5, (0, 0, 154), -1)
            cv2.rectangle(frame, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)
            # break
        h, w = 480,640
        h, w = h // 2, w // 2
        cv2.circle(frame, (w, h), 5, (0, 255, 0), -1)
        a1, a2, a3, a4 = w - 120, h - 120, w + 120, h + 120
        cv2.circle(frame, (a1, a2), 5, (255, 0, 54), -1)
        cv2.circle(frame, (a3, a4), 5, (255, 0, 69), -1)
        cv2.rectangle(frame, (a1, a2), (a3, a4), (0, 0, 255), 1)

        if p1 < a1 or q1 < a2 or p2 > a3 or q2 > a4:
            cv2.putText(frame,'outer',(20, 80),cv2.FONT_HERSHEY_SIMPLEX,2,(255, 255, 0),2)
            self.inner_count=0
            self.outer_count+=1
            if(self.outer_count>=3*self.outer_stopper):
                cv2.putText(frame, 'Outer Time up', (20, 150), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), 2)
        else:
            cv2.putText(frame,'inner', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
            self.outer_count=0
            self.inner_count+=1
            if(self.inner_count>=3*self.inner_stopper):
                cv2.putText(frame, 'take a break', (20, 150), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
