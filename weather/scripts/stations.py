'''
Evan Harry

List all stations from the Oracle weather project.
'''
import json
import time

import click
import requests

URL = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'


def get_stations():
    start = time.time()
    print('Fetching data...')

    stations = requests.get(URL).json()

    end = time.time()
    time_taken = end - start
    print('Time taken for API call: {0:.2f} seconds.'.format(time_taken))

    print('Total no. of registered stations: {0}.'.format(len(stations['items'])))


@click.command('get-stations')
def get_stations_command():
    '''Gets all weather stations.'''
    get_stations()
