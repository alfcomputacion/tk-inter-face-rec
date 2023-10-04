import cv2
from deepface import DeepFace


def recognize_faces():
    cap = cv2.VideoCapture('mainproj/VIDEO/entrada.mp4')

    while True:

        ret, frame = cap.read()
        if ret == False:

            break

        # El tamaño original es 3840 × 2160
        # frame = imutils.resize(frame, width=840)
        # scale_percent = 50  # percent of original size
        # idth = int(frame.shape[1] * scale_percent / 100)
        # height = int(frame.shape[0] * scale_percent / 100)
        # frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('mainproj/temp/myimage.jpg', frame)
        dfs = DeepFace.find(img_path='mainproj/temp/myimage.jpg',
                            db_path='pics',  enforce_detection=False, silent=True)

        for ide in range(0, len(dfs)):
            x = dfs[ide]['source_x'][0]
            y = dfs[ide]['source_y'][0]
            w = dfs[ide]['source_w'][0]
            h = dfs[ide]['source_h'][0]
            identidad = dfs[ide]['identity'][0].split('/')[1].split('.')[0]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            org = (50, 50)
            fontScale = 1
            color = (255, 0, 0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            thickness = 2
            frame = cv2.putText(frame, identidad, org, font,
                                fontScale, color, thickness, cv2.LINE_AA)
            cv2.imshow('frame', frame)

        t = cv2.waitKey(1)
        if t == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
