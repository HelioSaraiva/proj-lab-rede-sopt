# https://api.stackexchange.com/docs
import requests
import json

def formatjson(data):
    return json.dumps(data, sort_keys=True, indent=4)

def savejsonfile(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
    print('Salvo em arquivo.')

def main():
    payloadrespostas = {
        'todate': '1514764800',
        'order': 'desc',
        'sort': 'votes',
        'site': 'pt.stackoverflow'
    }
    respostas = requests.get('https://api.stackexchange.com/2.2/answers', params=payloadrespostas)
    if respostas.status_code == 200:
        savejsonfile(respostas.json())        

if __name__ == '__main__':
    main()