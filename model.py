import requests

DATA = {
     "vyp3CaptchaToken": "",
     "page": "1",
     "query": "",
     "region": "", 
     "PreventChromeAutocomplete": "" 
        }
HEADERS = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

class Model:
    def __init__(self):
        self.value = ""

    def treatResult(self, result):
        
        valueDict = result["rows"]
        exceptions = ['t', 'cnt', 'k', 'pg', 'tot']
        
        fullList = []

        for e, x in enumerate(valueDict):
            for ex in exceptions:
                try:
                    x.pop(ex)
                except:
                    pass
            fullList.append(list(x.values())) 

            #print(e, len(list(x.values())), list(x.values()))
        
        return fullList
        
    def action(self, caption):
        DATA["query"] = caption
        session = requests.Session()
        requestPost = session.post("https://egrul.nalog.ru/", json=DATA, headers=HEADERS)
        url = f'https://egrul.nalog.ru/search-result/{requestPost.json()["t"]}'
        return session.get(url, headers=HEADERS).json()