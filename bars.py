import json
import sys

from geohelper import distance


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_json_data = json.load(input_file)
    return raw_json_data


def get_biggest_bar_name(json_data):
    biggest_bar = max(json_data, key=lambda x: x['SeatsCount'])
    bar_name = biggest_bar['Name']
    return bar_name


def get_smallest_bar_name(json_data):
    smallest_bar = min(json_data, key=lambda x: x['SeatsCount'])
    bar_name = smallest_bar['Name']
    return bar_name


def get_closest_bar_name(json_data, user_longitude, user_latitude):
    closest_bar = min(json_data, key=lambda dist: distance.get_distance(dist['geoData']['coordinates'][1],
                                                                        dist['geoData']['coordinates'][0],
                                                                        user_latitude,
                                                                        user_longitude)
                      )
    bar_name = closest_bar['Name']
    return bar_name


if __name__ == '__main__':
    if len(sys.argv) > 3:
        filepath = sys.argv[1]
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
        try:
            json_data = load_data(filepath)
        except ValueError as e:
            print(e)
            raise SystemExit
        else:
            print('The biggest Bar name: ', get_biggest_bar_name(json_data))
            print('The smallest Bar name: ', get_smallest_bar_name(json_data))
            print('The closest Bar name: ', get_closest_bar_name(json_data, longitude, latitude))
    else:
        print(' Not all parameters provided. \n Example: python bars.py <file.json> <user_longitude> <user_latitude>')
