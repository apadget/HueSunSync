from metno_locationforecast import Place, Forecast

def getYRdata():
#    locationURL = https://api.met.no/weatherapi/nowcast/2.0/complete?altitude=10&lat=63.422881&lon=10.391192
#    urlContent = requests.get("https://api.met.no/weatherapi/nowcast/2.0/complete?altitude=1&lat=63.422&lon=10.391")
#    text = urlContent.text
    trondheim = Place("Trondheim", 63.4228, 10.3911, 1)
    ny_forecast = Forecast(trondheim, "metno-locationforecast/2.0 https://github.com/apadget/HueSunSync")
    ny_forecast.update()
    print(ny_forecast)
    ny_forecast.update()
    return

#def parseYRdata(dump):

# def updateYRdata():
# While loop getYRdata every 5 minutes


def main():
    getYRdata()
    #data = getYRdata()
    #print(data)
    #dataParsed = parseYRdata(data)
    #print(dataParsed)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/