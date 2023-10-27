import cv2
import os
import json
from datetime import datetime
from deepface import DeepFace
from mainproj.utils.createjson import create_json, append_json
from mainproj.utils.sendText import SendTxt
import asyncio
name = "FACE"
# cap = cv2.VideoCapture('entrada_2.mp4')


def recognize_faces():
    cap = cv2.VideoCapture('mainproj/VIDEO/Salida_2.mp4')
    # cap = cv2.VideoCapture(0)
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
    contador = 0
    org = (10, 50)
    fontScale = 1
    color = (255, 68, 51)
    detectColor = (0, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    detect = "Detectando..."
    name = ""
    x = 0
    y = 0
    w = 0
    h = 0
    cara = 'Verificando'
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
        verificado = '0%'
        cv2.imwrite('mainproj/temp/myimage.jpg', frame)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 0, 255), 2)
        frame = cv2.putText(frame, cara, org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        frame = cv2.putText(frame, name, (x, y - 10),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

        frame = cv2.putText(frame, cara, (x-18, y - 25),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 210, 0), 1)
        frame = cv2.putText(frame, detect, (x-18, y - 40),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, detectColor, 1)
        if contador > 5:
            contador = 0
            try:
                dfs = DeepFace.find(img_path='mainproj/temp/myimage.jpg',
                                    db_path='pics',  enforce_detection=False, silent=True)

                # task = asyncio.create_task(dfsFunc())

                for ide in range(0, len(dfs)):

                    x = dfs[ide]['source_x'][0]
                    y = dfs[ide]['source_y'][0]
                    w = dfs[ide]['source_w'][0]
                    h = dfs[ide]['source_h'][0]
                    # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.rectangle(frame, (x, y), (x+w, y+h),
                                  (0, 0, 255), 2)
                    frame = cv2.putText(frame, cara, org, font,
                                        fontScale, color, thickness, cv2.LINE_AA)
                    frame = cv2.putText(frame, name, (x, y - 10),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

                    frame = cv2.putText(frame, cara, (x-18, y - 25),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 210, 0), 1)
                    frame = cv2.putText(frame, detect, (x-18, y - 40),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.5, detectColor, 1)
                    verificado = str(
                        (100 - round(dfs[0]['VGG-Face_cosine'][0]*100, 2))) + '%'

                    identidad = dfs[ide]['identity'][0].split(
                        '/')[1].split('.')[0]
                    name = dfs[0]['identity'][0].split('\\')[-1].split('/')[0]

                    filepath = os.path.join('pics/' + name + '/data.json')

                    with open(filepath, 'r') as fp:
                        information = json.load(fp)
                        if str(information['Alumno'][0]['matricula']) not in lista:
                            # print('alumno ya entro a la escuela')
                            # print(rostro)
                            matricula = str(
                                information['Alumno'][0]['matricula'])
                            nombre = str(information['Alumno'][0]['nombre'])
                            apellidos = str(
                                information['Alumno'][0]['apellidos'])
                            tel_contacto = str(
                                information['Alumno'][0]['tel_contacto'])

                            append_json(today, matricula, nombre,
                                        apellidos, tel_contacto)
                            lista.append(
                                str(information['Alumno'][0]['matricula']))

                    org = (10, 50)
                    fontScale = 1
                    color = (255, 68, 51)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    thickness = 2

                    # print('before dfs if')
                    if len(dfs[0]) > 1:

                        # print('after dfs if')
                        print(dfs[0]['identity'][0])

                        if x != 0 and dfs[0]['VGG-Face_cosine'][0] < 0.28:

                            # obj = DeepFace.verify(
                            #     'mainproj/temp/myimage.jpg', dfs[0]['identity'][0])

                            # print(obj['verify'])
                            name = dfs[0]['identity'][0].split(
                                '\\')[-1].split('/')[0]
                            detect = 'DETECTADO CON UN ' + verificado
                            detectColor = (0, 255, 0)
                        else:
                            name = "Face"
                            detect = "No se puede detectar"
                            detectColor = (0, 0, 255)
                            if x == 0:
                                detectColor = (255, 255, 255)
                                detect = "Detectando..."
                        # frame = cv2.putText(frame, name, (x, y - 10),
                        #                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

                        # frame = cv2.putText(frame, detect, org, font,
                        #                     fontScale, color, thickness, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x+w, y+h),
                                      (0, 0, 255), 2)
                        frame = cv2.putText(frame, cara, org, font,
                                            fontScale, color, thickness, cv2.LINE_AA)
                        frame = cv2.putText(frame, name, (x, y - 10),
                                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

                        frame = cv2.putText(frame, cara, (x-18, y - 25),
                                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 210, 0), 1)
                        frame = cv2.putText(frame, detect, (x-18, y - 40),
                                            cv2.FONT_HERSHEY_COMPLEX, 0.5, detectColor, 1)
            except:
                print(KeyError)
                cv2.rectangle(frame, (x, y), (x+w, y+h),
                              (0, 0, 255), 2)
                frame = cv2.putText(frame, cara, org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
                frame = cv2.putText(frame, name, (x, y - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

                frame = cv2.putText(frame, cara, (x-18, y - 25),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 210, 0), 1)
                frame = cv2.putText(frame, detect, (x-18, y - 40),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, detectColor, 1)
                # frame = cv2.putText(frame, name, (x, y - 10),
                #                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
                # frame = cv2.putText(frame, "VERIFICADO con un " + verificado, org, font,
                #                     fontScale, color, thickness, cv2.LINE_AA)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # frame = cv2.putText(frame, name, org, font,
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        frame = cv2.putText(frame, cara, org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        frame = cv2.putText(frame, name, (x, y - 10),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

        frame = cv2.putText(frame, cara, (x-18, y - 25),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 210, 0), 1)
        frame = cv2.putText(frame, detect, (x-18, y - 40),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, detectColor, 1)
        cv2.imshow('frame', frame)
        contador += 1
        t = cv2.waitKey(1)
        if t == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    # SendTxt(today)
