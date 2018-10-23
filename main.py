# https://api.stackexchange.com/docs
import requests
import json

def formatjson(data):
    return json.dumps(data, sort_keys=True, indent=4)

def savejsonfile(data, name):
    try:
        with open(name + '.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)
            return True
    except (OSError, IOError) as e:
        return False

def getquestions():
    # Endpoint: /2.2/questions?fromdate=1514764800&order=desc&sort=creation&site=pt.stackoverflow
    payload = {
        'fromdate': '1514764800',
        'order': 'desc',
        'sort': 'creation',
        'site': 'pt.stackoverflow'
    }
    url = 'https://api.stackexchange.com/2.2/questions'
    req = requests.get(url, params=payload)
    return req.json() if req.status_code == 200 else None

def gettags():
    # Endpoint: /2.2/tags?pagesize=5&order=desc&sort=popular&site=pt.stackoverflow
    payload = {
        'pagesize':'5',
        'order':'desc',
        'sort':'popular',
        'site':'pt.stackoverflow'
    }
    url = 'https://api.stackexchange.com/2.2/tags'
    req = requests.get(url, params=payload)
    return req.json() if req.status_code == 200 else None

def main():
    questions = getquestions()
    if questions:
        if savejsonfile(questions, 'questions'):
            print('Arquivo JSON salvo.')

    tags      = gettags()
    if tags:
        if savejsonfile(tags, 'tags'):
            print('Arquivo JSON salvo.')

if __name__ == '__main__':
    main()