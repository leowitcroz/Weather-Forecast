import requests

API_KEY = '5b94b924ece19b304f1a5fc489b6aac3'


def get_data(place,days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * days
    filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place='Tokyo',days=3))