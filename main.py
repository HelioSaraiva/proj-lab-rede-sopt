# https://api.stackexchange.com/docs
import requests
import json

def formatjson(data):
    return json.dumps(data, sort_keys=True, indent=4)

def savejsonfile(data):
    try:
        with open('data.json', 'w') as outfile:
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
    
def main():
    questions = getquestions()
    if questions:
        if savejsonfile(questions):
            print('Arquivo JSON salvo.')

if __name__ == '__main__':
    main()