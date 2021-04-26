# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import requests
from pandas import Series
import pandas as pd
import multiprocessing




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# with open("buycurecare1.html",encoding="utf-8") as f:
#     data = f.read()
# a = re.findall("\"//(www.buypurecare.com/hosted/images/.*?)\"",data)
# for b in a:

proxies = {'http':'http://127.0.0.1:1080'}
headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36"}
url = "https://consumertrendsnews.com/surprising-new-tech-pv/?cep=bEFnuxCqnHxeBLr9BzEXeGK3W9USRn_aHK4a59S76CghUX_QW2HLhc8q4jPSmiHfqGP5aHubhv_RO78D3fYhslGFD9hh8xV5xoh9VMN_JhfMXa5iM2KzAIkor6GYZ9XMSKBMNfAGwp3tZq17e3Y3A7OwHAwhCulbAdvOcRPAzueW73_JZAzP-7tqRFMvo54Gg4y_PrBkaNokGzDZi3vXIwhP7WcQW31ntkd6csPqEzCiVNEd_J0pfBOoQfJYF_ob1ULTkuPz07X42vjdqItGAFoFwbvaD_kula5_k-Tj0_VUtQ2nTMTtTgh2coBOqaBcYhJM5JIaIrcg2OfoWthpNs8fNV5iEL8-yWypFxlBde2b-3dORD8Kothg2jc5XppPSS8oSiz_ZD4eDxYHRU3Gr4Q03cqRq2CyfPW-LKFAqXVjM3wPMRoCDYFFp6rpoaHeB0_MDHWwIUnVbC0VSKvsYMsdjAaK5nmI19nQAaIEU0kwB4a6dtJ53ERWYqEmJtg_6kSo_Glly8St1V6ytDD_cqCz9uWZo0jS6AYlxiHcJgOQGVXQdOnXO9dH7D72hCZj1OmbX3gPsXchlvkT7yhzAvJVwttgRdeR6YJgIOyNX-cMzhlHV257bc3VRClWHzol&lptoken=16ee198e33f743cc426a&oty=wTUwwFjVPVDLppX50eYtfpj0VTQrLymurp_Se0-2lfZKHTSSAV4ka5Wzc8AJlDwKzmA8o9bq02JOS4TUcXBDUHOvqYcSlXuh1cpoMNj01MAANcMlfjcFVLbO3HJxyoNayuKuj1vDPIvsJ4ScjbH-PVhYRAVKpKt8uXuLs7V8xEn_ybb3eKVBzprCIEZ2GKDG2I0FJvQx5Dd8mM5Lmndn7Kp33PdFI9-T5w65JqATFMiqFVhz6H1y-0FZ0h07FnO74ih28ezw22J8ar-a2aOK12rwB3jDBMfM3YQyeVDPcTupIVOoPg_Jv9B2tipmWZ91cburG7YfUwuQomKUx-UYVjYfRPMUFL8h2InJAWBxlu-yEwWa0aWjmb6g_UPBavgzPw_XJ6KwM0AVEDnsDAhQHfswEKlJZ_PzCvNWz8HqlvF9IuuE-sugQruj927TTzGvSVZ_ae3UgoqWDSNrBJQZuQh5MWdzC5EO943IsQvg7fNsRZ8q-3n7HZnI7CepFw9oVB3j0MGHdQcCZmtS8dAGOLo6r5yBM2zlA_d8vosKDaLtMsL4l72fda30jXpi-NgWFXPEophcnKZCYyjHzsKFzKCMJ1jUAPPPvOW850MIEsez3gmvi4AJSa3KVSex7a1gKsTO1_yQlCvuwPCNKIrj7ar6rUGA9DTpgqMa6dA1iqe_LaxRR4_2P8mTOX8snwiZ&rev_campaign_id=390908&rev_campaign_id=390908"
url = "https://baidu.com"
# r = requests.get(url,headers = headers,proxies = proxies)
#
# filename = "title.html"
# with open(filename,'w',encoding='utf-8') as file_object:
#     file_object.write(r.text)

excelname = "E:\studyFile\泽鸿-原生广告.xlsx"
data = pd.read_excel(excelname,None,engine='openpyxl')
print(data.keys())
links_arr = []
for sh_name in data.keys():
    # print('sheet name:')
    sh_data = pd.DataFrame(pd.read_excel(excelname,sh_name,engine='openpyxl',usecols=[1,2,3]))
    links = sh_data.values.tolist()
    print(links)
    for link in links:
        if link:
            links_arr.append(link)




