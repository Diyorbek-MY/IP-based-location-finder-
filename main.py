import json
import urllib.request

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    cont = rec['continent']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print('[*] Target' + tgt + 'GeoLocated')
    print('[+] City:', str(city) + " " + ' , Country :', str(country) + " " + ' , Continent : ', str(cont) + " ")
    print('Latitude :', str(lat) + " " + ', Longitude :', str(long))


data = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())
tgt = data["ip"]
print("Ip Address found : ", tgt)
printRecord(tgt)