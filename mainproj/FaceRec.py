import cv2
import os
import json
from datetime import datetime
from deepface import DeepFace
from mainproj.utils.createjson import create_json, append_json
from mainproj.utils.sendText import SendTxt


# cap = cv2.VideoCapture('entrada_2.mp4')
def recognize_faces():
    cap = cv2.VideoCapture('mainproj/VIDEO/salida11.mp4')
    today = "Lista_alumnos_" + str(datetime.today().day) + "_" + \
        str(datetime.today().month) + "_" + \
        str(datetime.today().year) + "_" + \
        "_.json"
    # str(datetime.today().hour) + "_" + \
    # str(datetime.today().minute) + \
    # SendTxt(today)

    alumno = {"Alumno": []}
    lista = []
    create_json(today, alumno)
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
        try:
            cv2.imwrite('mainproj/temp/myimage.jpg', frame)
            dfs = DeepFace.find(img_path='mainproj/temp/myimage.jpg',
                                db_path='pics',  enforce_detection=False, silent=True)

            for ide in range(0, len(dfs)):
                x = dfs[ide]['source_x'][0]
                y = dfs[ide]['source_y'][0]
                w = dfs[ide]['source_w'][0]
                h = dfs[ide]['source_h'][0]
                identidad = dfs[ide]['identity'][0].split('/')[1].split('.')[0]
                name = dfs[0]['identity'][0].split('\\')[-1].split('/')[0]
                # jsonpath = dfs[0]['identity'][0].split('/')[1]
                print('IDENTIDAD')
                print(dfs[0]['identity'][0].split('\\')[0])
                filepath = os.path.join('pics/' + name + '/data.json')
                with open(filepath, 'r') as fp:
                    information = json.load(fp)
                    if str(information['Alumno'][0]['matricula']) not in lista:
                        # print('alumno ya entro a la escuela')
                        # print(rostro)
                        matricula = str(information['Alumno'][0]['matricula'])
                        nombre = str(information['Alumno'][0]['nombre'])
                        apellidos = str(information['Alumno'][0]['apellidos'])
                        tel_contacto = str(
                            information['Alumno'][0]['tel_contacto'])

                        append_json(today, matricula, nombre,
                                    apellidos, tel_contacto)
                        lista.append(
                            str(information['Alumno'][0]['matricula']))
                if dfs[0]['VGG-Face_cosine'][0] < 0.31:
                    print(dfs[0]['VGG-Face_cosine'][0])
                    cv2.putText(frame, name, (x, y - 10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

                org = (50, 50)
                fontScale = 1
                color = (255, 0, 0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                thickness = 2
                frame = cv2.putText(frame, identidad, org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow('frame', frame)
        except:
            pass
        t = cv2.waitKey(1)
        if t == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    SendTxt(today)
