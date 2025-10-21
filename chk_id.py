import icons

def id_to_icon(id):
    if id == 1000:
        icons.clear()
    elif id == 1003:
        icons.fclouds()
    elif id == 1006 or id == 1009:
        icons.sclouds()
    elif id == 1009:
        icons.bclouds()
    elif id == 804:
        icons.occlouds()
    elif id == 1171 or id == 1192 or id == 1195 or id == 1201 or id == 1243 or id == 1246:
        icons.srain()
    elif id == 1009 or id == 1072 or id == 1150 or id == 1153 or id == 1168 or id == 1180 or id ==1183 or id ==1186 or id ==1189 or id == 1198 or id == 1240:
        icons.rain()
    elif id == 1087:
        icons.tstorm()
    elif id == 1066 or id == 1069 or id == 1114 or id == 1117 or id == 1204 or id == 1207 or id == 1210 or id == 1213 or id == 1216 or id == 1219 or id == 1222 or id == 1225 or id == 1237:
        icons.snow()
    elif id == 1030 or id == 1135 or id == 1147:
        icons.mist()

def all():
    icons.clear()
    icons.fclouds()
    icons.sclouds()
    icons.bclouds()
    icons.occlouds()
    icons.srain()
    icons.rain()
    icons.tstorm()
    icons.snow()
    icons.mist()
