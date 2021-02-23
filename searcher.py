import os
from pathlib import Path
import glob
import googlesearch
import requests
from baidusearch.baidusearch import search
from time import sleep

class Searcher:
    def __init__(self):
        self.success = []
        self.linenum = 0
        self.result = []
        self.sub_results = []
        self.num = 10

    def LocalSearcher(self, string):
        for self.dirpath, self.dirnames, self.files in os.walk(Path.home()):
            self.listdirs = os.listdir(self.dirpath)
            for i in self.listdirs:
                if string == '':
                    pass
                else:
                    if string.lower() in i.lower():
                        if i in self.success:
                            pass
                        else:
                            self.success.append(os.path.join(self.dirpath, i))
                            pass
        return self.success

    def WebSearcher(self, string):
        # search baidu (might get banned)
        temp = search(string)
        for i in range(self.num):
            self.sub_results.append(temp[i]['url'])

        # search google (might get banned)
        googletemp = googlesearch.search(string, num_results=self.num)
        self.sub_results.append(googletemp)

        for i in self.sub_results:
            try:
                search_proxies = {
                    'https': 'https://143.110.220.192:8080',
                    'https:': 'https://143.110.220.166:8080',
                    'https': 'https://104.238.130.50:8080',
                    'https': 'https://67.205.190.164:8080',
                    'https': 'https://207.148.31.154:8080',
                    'https': 'https://67.205.169.251:3128',
                    'https': 'https://161.35.230.88:8080',
                    'https': 'https://143.110.150.2:8080'
                }

                response = requests.get(str(i), proxies=search_proxies)
                response = response.content

                if string.lower in response.lower():
                    if string in self.result:
                        pass
                    else:
                        self.result.append(i)
                        pass
                elif string.lower() in i.lower():
                    if string in self.result:
                        pass
                    else:
                        self.result.append(i)
                        pass
                else:
                    pass
            except:
                pass

            try:
                search_proxies = {
                    'https': 'https://143.110.220.192:8080',
                    'https:': 'https://143.110.220.166:8080',
                    'https': 'https://104.238.130.50:8080',
                    'https': 'https://67.205.190.164:8080',
                    'https': 'https://207.148.31.154:8080',
                    'https': 'https://67.205.169.251:3128',
                    'https': 'https://161.35.230.88:8080',
                    'https': 'https://143.110.150.2:8080'
                }

                tryresponse = requests.get(str(i), proxies=search_proxies)
                tryresponse = tryresponse.content

                if string.lower() in tryresponse.lower():
                    if string in self.result:
                        pass
                    else:
                        self.result.append(i)
                        pass
                elif string.lower() in i.lower():
                    if string in self.result:
                        pass
                    else:
                        self.result.append(i)
                        pass
                else:
                    pass
            except:
                pass

        return self.result
