import icons

def check_desc(desc):
    if desc == "clear sky":
        icons.clear()
    elif desc == "few clouds":
        icons.fclouds()
    elif desc == "scattered clouds":
        icons.sclouds()
    elif desc == "broken clouds":
        icons.bclouds()
    elif desc == "shower rain":
        icons.srain()
    elif desc == "rain":
        icons.rain()
    elif desc == "thunderstorm":
        icons.tstorm()
    elif desc == "snow":
        icons.snow()
    elif desc == "mist":
        icons.mist()
    elif desc == "overcast clouds":
        icons.occlouds()