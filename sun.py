from suntime import Sun, SunTimeException

# https://github.com/SatAgro/suntime/blob/master/suntime/suntime.py


def location():
    latitude = 63.4225
    longitude = 10.3950
    sun = Sun(latitude, longitude)
    return sun


def formattime(timedate):
    formatted = format(timedate.strftime('%H:%M'))
    return formatted


def getsunrise():
    sun = location()
    today_sr = sun.get_local_sunrise_time()
    return formattime(today_sr)


def getsundown():
    sun = location()
    today_ss = sun.get_sunset_time()
    return formattime(today_ss)