import sys
import uuid
from .api import yelp
from .api import geolocation
import geocoder
import os
import click
import pprint
import time
# from blessings import Terminal
from pydoc import pipepager
from termcolor import colored, cprint
from colorama import Fore, Back, Style

@click.command()
@click.option('--term', default='Restaurants', type=click.STRING)
@click.option('--location', default='San Francisco', type=click.STRING)
@click.option('--latitude', default=37.780817, type=click.FLOAT)
@click.option('--longitude', default=-122.472149, type=click.FLOAT)
@click.option('--radius', default=5000)
@click.option('--categories', default="")
@click.option('--locale', default="")
def search(term, location, latitude, longitude, radius, categories, locale):
    print(term, location, latitude, longitude, radius)

    if not latitude and not longitude:
            # using google maps geolocation API if you have a key
            if 'GOOGLE_API_KEY' in os.environ:
                print('using Google API')
                geo = geolocation.geolocate()
                print(geo)
                latitude = geo['location']['lat']
                longitude = geo['location']['lng']
            else:
                # uses this inaccurate api as test
                print('using geocoder')
                g = geocoder.ip('me')
                print(g.latlng)
    bus = yelp.query_api(term, latitude, longitude)
        
    for i in range(len(bus)):
        # print(businesses[i])
        pprint.pprint(bus[i]['name'], indent=2)

    # pipepager(Fore.RED + str(bus), cmd='less -R')

@click.group()
def whateat():
    pass

whateat.add_command(search)

    # pager('hello world\n' * 20 + 'hello world2\n' * 20)
    # pager()
        # time.sleep(10)


    # if there is latlong addes as arguments
    # if not lat and not lng:
    #     # using google maps geolocation API if you have a key
    #     if 'GOOGLE_API_KEY' in os.environ:
    #         print('using Google API')
    #         geo = geolocation.geolocate()
    #         print(geo)
    #         lat = geo['location']['lat']
    #         lng = geo['location']['lng']
    #     else:
    #         # uses this inaccurate api as test
    #         print('using geocoder')
    #         g = geocoder.ip('me')
    #         print(g.latlng)

    # bus = yelp.query_api(term, lat, lng)
    
    # # for i in range(len(businesses)):
    # #     # print(businesses[i])
    # #     pprint.pprint(businesses[i], indent=2)

    # pipepager(Fore.RED + str(bus), cmd='less -R')
