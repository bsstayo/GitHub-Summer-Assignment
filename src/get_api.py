import requests


def get_url_results(url, number_of_times):
    target_url = url[:-2]+number_of_times  # target url
    results = requests.get(target_url).json()

    return results
