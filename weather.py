from metno_locationforecast import Place, Forecast

# https://520liyan.xyz/Rory-Sullivan/metno-locationforecast

def getYRdata():
    trondheim = Place("Trondheim", 63.4228, 10.3911, 10)
    ny_forecast = Forecast(trondheim, "metno-locationforecast/2.0 https://github.com/apadget/HueSunSync")
    ny_forecast.update()
    #print(vars(ny_forecast.data.intervals[0]).keys())
    datanow = ny_forecast.data.intervals[0]
    clouds = datanow.variables["cloud_area_fraction"]
    return clouds

# 0% = sol    100% = overskyet

