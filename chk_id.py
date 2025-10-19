import icons

def id_to_icon(id):
    if id == 800:
        icons.clear()
    elif id == 801:
        icons.fclouds()
    elif id == 802:
        icons.sclouds()
    elif id == 803:
        icons.bclouds()
    elif id == 804:
        icons.occlouds()
    elif id in range(520, 522) or id == 531:
        icons.srain()
    elif id in range(500, 504):
        icons.rain()
    elif id in range(200, 232):
        icons.tstorm()
    elif id in range(600, 622) or id == 511:
        icons.snow()
    elif id in range(701, 781):
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
