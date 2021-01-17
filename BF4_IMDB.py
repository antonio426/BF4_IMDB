# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:00:42 2020

@author: AntonioTseng
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
quote_page = 'https://www.imdb.com/list/ls091520106/?ref_=tt_rels_1'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all('h3', attrs={'class': 'lister-item-header'})
context_box = soup.find_all('p', attrs={'class': ''})
i=1
rename=[]
recontext=[]
import pandas as pd # 引用套件並縮寫為 pd
for name in name_box:
    i+=1
    rname = name.select_one("a").getText()
    rename.append(rname)
    #print("編號",i,": ",name.select_one("a").getText())
    
for context in context_box:
    rcontext = context.getText().strip()
    recontext.append(rcontext)
    #print("內容",context.getText().strip())
recontext.remove(recontext[0])
#print(rename)
#print(recontext)

dict = {"name": rename,  
        "context": recontext
       }
select_df = pd.DataFrame(dict)
csv_pandas = select_df.to_csv(r'C:\Users\AntonioTseng\Desktop\BF4_IMDB.csv',encoding='utf_8_sig')
#print(select_df) # 看看資料框的外觀  
#print(dict)

# =============================================================================
# with open('BF4_IMDB.csv','w', newline='',encoding="utf-8") as csvFile:
#     # 定義欄位
#     # 將 dictionary 寫入 CSV 檔
#     fieldnames = ['name','context']
#     writer = csv.DictWriter(csvFile, fieldnames = fieldnames)
#     writer.writeheader()
#     writer.writerow(dict)
# =============================================================================
    
    
    
# =============================================================================
#     writer.writeheader()
#     writer = csv.writer(csvFile)
#     print(rename)
#     for row in dict:
#         #print(row)
#         writer.writerow([row])
# =============================================================================






#name = name_box
#print (name)
# strip() 函數用於去除前後空格

# =============================================================================
# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text
# print (price)
# =============================================================================
