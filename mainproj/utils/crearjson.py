import json
import datetime
import os

print(os.path.abspath(os.getcwd()))
path = os.path.abspath(os.getcwdb())

alumno = {
    "Alumno": [
        {
            "matricula": 1512345,
            "nombre": "Angelina",
            "apellidos": "Jolie",
            "tel_contacto": 13234233555
        }
    ]
}


def crear_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def adjuntar_json(filepath, matricula, nombre, apellidos, tel):
    now = str(datetime.datetime.now())
    with open(filepath, 'r') as fp:
        information = json.load(fp)

        information["Alumno"].append({
            "matricula": matricula,
            "nombre": nombre,
            "apellidos": apellidos,
            "tel_contacto": tel,
            "hora": now,
        })

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=2)


def delobject(name="jose"):
    obj = json.load(open('asistencia.json'))

    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in range(len(obj)):
        if obj[i]["nombre"] == name:
            print(obj[i])
            obj.pop(i)
        break


# delobject('Jose')
# append_statistics('asistencia.json', 100, 90, 15)
# crear_json("lista223.json", alumno)
# print(datetime.date.today())
# print(str(datetime.date.today().year))

# alumno = {"Alumno": []}
# print(type(alumno))
# print(type(alumno['Alumno']))
