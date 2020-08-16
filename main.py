import cv2
import dlib
import time
def get_info(frame):
    #https://www.tutorialkart.com/opencv/python/opencv-python-get-image-size/
    img = frame
    height = img.shape[0]
    width = img.shape[1]
    return  height, width

# def put_text(a,x,y):
#     # https://stackoverflow.com/questions/16615662/how-to-write-text-on-a-image-in-windows-using-python-opencv2
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     bottomLeftCornerOfText = (x,y)
#     fontScale = 1
#     fontColor = (255, 255, 255)
#     lineType = 2
#     cv2.putText(frame,a,
#                 bottomLeftCornerOfText,
#                 font,
#                 fontScale,
#                 fontColor,
#                 lineType)

def i_timer():
    for i in range(30):
        print(i)
        if not is_img_out():
            # time.sleep(0)
            pass
        else:
            o_timer()
            break
    else:
        print("time over")
def o_timer():
    for i in range(30):
        print(i)
        if is_img_out():
            time.sleep(0.03333333333)
        else:
            i_timer()
            break
    else:
        print("time over")
def is_img_out():
    # timer()
    # https://pysource.com/2019/03/12/face-landmarks-detection-opencv-with-python/
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    while True:
        # print("in while")
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        h, w = get_info(frame)
        h, w = h // 2, w // 2
        cv2.circle(frame, (w, h), 5, (0, 255, 0), -1)
        a1, a2, a3, a4 = w - 120, h - 120, w + 120, h + 120
        cv2.circle(frame, (a1, a2), 5, (255, 0, 255), -1)
        cv2.circle(frame, (a3, a4), 5, (255, 0, 255), -1)
        cv2.rectangle(frame, (a1, a2), (a3, a4), (0, 0, 255), 1)  # <--

        faces = detector(gray)
        x1,x2,x3,x4=0,0,0,0
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)  # <--

            cv2.circle(frame, (x1, y1), 5, (255, 0, 0), -1)
            cv2.circle(frame, (0, 0), 5, (255, 0, 0), -1)
            cv2.circle(frame, (x1, y1), 5, (255, 0, 0), -1)
            cv2.circle(frame, (640, 480), 5, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 5, (255, 0, 0), -1)
            # cv2.imshow("hello", frame)
            # print('imshow is working')
            ret, jpeg = cv2.imencode('.jpg', frame)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            if x1 < a1 or y1 < a2 or x2 > a3 or y2 > a4:
                # print('outer')
                return True
            else:
                # print('inner')
                return False
# print(is_img_out())
def check():
    if is_img_out():
        o_timer()
    else:
        i_timer()
check()