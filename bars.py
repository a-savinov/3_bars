import json
import sys

from geohelper import distance


def check_json_data(input_json):
    try:
        return json.loads(input_json)
    except ValueError:
        print('JSON syntax error')
        raise SystemExit


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_data = check_json_data(input_file.read())
    return raw_data


def get_biggest_bar(json_data):
    biggest_bar = max(json_data, key=lambda x: x['SeatsCount'])
    bar_name = biggest_bar['Name']
    return bar_name


def get_smallest_bar(json_data):
    smallest_bar = min(json_data, key=lambda x: x['SeatsCount'])
    bar_name = smallest_bar['Name']
    return bar_name


def get_closest_bar(json_data, user_longitude, user_latitude):
    closest_bar = min(json_data, key=lambda dist: distance.get_distance(dist['geoData']['coordinates'][1],
                                                                        dist['geoData']['coordinates'][0],
                                                                        user_latitude,
                                                                        user_longitude))
    bar_name = closest_bar['Name']
    return bar_name


if __name__ == '__main__':
    if len(sys.argv) > 3:
        filepath = sys.argv[1]
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
        print('The biggest Bar: ', get_biggest_bar(load_data(filepath)))
        print('The smallest Bar: ', get_smallest_bar(load_data(filepath)))
        print('The closest Bar: ', get_closest_bar(load_data(filepath), longitude, latitude))
    else:
        print(' Not all parameters provided. \n Example: python bars.py <file.json> <user_longitude> <user_latitude>')
