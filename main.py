# https://api.stackexchange.com/docs
import requests
import json

def formatjson(data):
    return json.dumps(data, sort_keys=True, indent=4)

def savejsonfile(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
    print('Salvo em arquivo JSON.')

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
    if req.status_code != 200:
        return None
    return req.json()
    
def main():    
    questions = getquestions()
    if questions:
        savejsonfile(questions)

if __name__ == '__main__':
    main()