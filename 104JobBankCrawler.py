#!/usr/bin/env python3
# coding: utf-8
"""
    Created on Sun Jul 22 11:14:24 2018
    
    @author: wei-hsuanlien
"""

#------科技業 technology------#
#https://www.104.com.tw/area/cj/market/technology?&page=1
#https://www.104.com.tw/area/cj/market/technology?&page=2
#------製造業 manufacturing------#
#https://www.104.com.tw/area/cj/market/manufacturing?&page=1
#https://www.104.com.tw/area/cj/market/manufacturing?&page=2
#------服務業 services------#
#https://www.104.com.tw/area/cj/market/services?&page=1
#https://www.104.com.tw/area/cj/market/services?&page=2
#------金融業 financial------#
#https://www.104.com.tw/area/cj/market/financial?&page=1
#https://www.104.com.tw/area/cj/market/financial?&page=2
#------餐飲旅遊住宿業 travel------#
#https://www.104.com.tw/area/cj/market/travel?&page=1
#https://www.104.com.tw/area/cj/market/travel?&page=2

import csv
import time
import requests
from bs4 import BeautifulSoup


job_list = ['technology', 'manufacturing', 'services', 'financial', 'travel']
page = 1200

try:
    jobCrawler = open(path, 'w', newline='')
    csvDoc = csv.writer(jobCrawler)
    csvDoc.writerow(['發布日期', '公司名稱', '職務名稱', '經歷', '學歷', '地區'])
    for i in job_list:
        tStart = time.time()
        record_page = 0
        for j in range(1, page+1):
            try:
                r = 'https://www.104.com.tw/area/cj/market/' + str(i) + '?&page=' + str(j)
                r = requests.get(r, timeout = 30)
                if r.status_code == requests.codes.ok:
                    r.raise_for_status()
                    r.encoding = r.apparent_encoding
                    soup = BeautifulSoup(r.text, 'html.parser')
                    for bbleft in soup.find_all("div", class_="joblist_cont"):
                        li_list = bbleft.find_all("li")
                        try:
                            date = li_list[1].find_all("div")[0].text.strip()
                            company = li_list[2].find_all("a")[0].text.strip()
                            vacancy = li_list[3].find_all("a")[0].text.strip()
                            experience = li_list[4].find_all("div")[0].text.strip()
                            education = li_list[5].find_all("div")[0].text.strip()
                            area = li_list[6].find_all("div")[0].text.strip()
                            content = [date, company, vacancy, experience, education, area]
                            csvDoc.writerows([content])
                        except:
                            if li_list[1].find_all("div")[0] is None:
                                break
        except:
            continue
            
            if j % 100 == 1:
                pass
                print("#---- Category: " + str(i) +  ", Page " + str(record_page) + " ----#") 
            record_page = j
        tEnd = time.time()
    print("#---- Category: " + str(i) +  ", Page " + str(record_page) + "---- time: " + str(tEnd - tStart) + " ----#") 
jobCrawler.close()

except IOError as e:
    print(e)




