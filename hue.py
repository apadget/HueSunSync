from phue import Bridge

BridgeIP = Bridge('192.168.35.115')


def connectbridge(bridgeip):
    bridgeip.connect()


def bridgestate():
    print(BridgeIP.get_api())


def changebrightness(lightname, value):
    #BridgeIP.get_light(lightname)
    BridgeIP.set_light(lightname, 'bri', int(value))
    print("Set brightness to " + str(value))


def changetemp(lightname, value):
    #BridgeIP.get_light(lightname, value)
    BridgeIP.set_light(lightname, 'sat', int(value))
    print("Set temperature to " + str(value))
