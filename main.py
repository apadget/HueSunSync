from metno_locationforecast import Place, Forecast
import json
import requests
import weather
import sun
import hue
import time

#def getYRdata():
#    locationURL = https://api.met.no/weatherapi/nowcast/2.0/complete?altitude=10&lat=63.422881&lon=10.391192
#    urlContent = requests.get("https://github.com/apadget/HueSunSync", "https://api.met.no/weatherapi/sunrise/2.0/.xml?date=2022-02-26&lat=63.4228&lon=10.3911&offset=%2B01%3A00")
#    data = urlContent.json()


#def parseYRdata(dump):

# def updateYRdata():
# While loop getYRdata every 5 minutes
def updatedata():
    w = weather.getYRdata()
    sd = sun.getsundown()
    ss = sun.getsunrise()
    return w, sd, ss


def gettime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return current_time

def sunmath():
    timenow = gettime()
    if timenow < sun.getsunrise():
        print("Mørkt før soloppgang")
    elif timenow > sun.getsundown():
        print("Mørkt etter solnedgang")
    else:
        print("Lyst ute")



def main():
    print(weather.getYRdata())
    print(sun.getsunrise())
    print(sun.getsundown())
    print(gettime())
    sunmath()
    #hue.bridgestate()
    #hue.changebrightness("Hue lightstrip", 254)
    #hue.changetemp("Hue lightstrip", 250)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/