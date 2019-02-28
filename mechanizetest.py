#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mechanize
import time
import json,os
from bs4 import BeautifulSoup

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'https://test'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['name'] = 'xxxxx'
browser.form['password'] = 'xxxxxxx'

# browser.form['username'] = 'c-wang'
# browser.form['password'] = 'maintec[2'
response = browser.submit()
url2 = 'https://test2'
# time.sleep(10) 
response2 = browser.open(url2)
# print(response2.read())
data = json.loads(response2.read()) 
#outdata = json.dumps(data, ensure_ascii=False)

text_file = open('autoPrintHtmlimage2.txt', "w")
#idarr = ['sort', 'Relation', 'Air', 'Which', 'string', 'Swing by', 'Dating', 'job', 'AutoUnattend', 'Calendar', 'in_the_forest', 'ExciteGame', 'Favor', 'Gyu-Tan-Game', 'Calc', 'cmtout', 'v10', 'copyme', 'drecon', 'Forgotten', 'hiddenhtml', 'History', 'dater', 'SHOCK !', 'Block', 'The history', 'Crossword', 'Poster', 'Life', 'RLO', 'JPG', 'The Public Document "F"', 'notepad?', 'Anomaly Directories are Serial', 'Letter from Galaxy', 'A_Priceless_Treasure', 'comma', 'TimeMachine', 'Leak Leak Leak!!!', 'SNSisDANGER2', 'Property', 'ccTLD', 'ExPrtct', 'Footprint', 'Friend', 'paper book', 'Excel.lent', 'Lookfor', 'Where', 'localasterisk', 'Listen', 'Name', 'WLAN', 'Unlock', 'Binary_Ultra-Introduction', 'sleepy', 'Analyze', 'dotnet_branch', 'mod', 'Arithmetic', 'Chase(2) Lots of branches', 'LINK', 'Photo', 'E.X.E', 'BlackBox', 'LOG', 'Macro', 'Fuzzy', 'Melancholy Holiday(1) Broken Head', 'Screen', 'Starting', 'processing', 'Macro-Power', 'HiddenFile', 'Unconn', 'PDF-JPGS', 'Indeed', 'Notes', 'RunRanRun', 'Chase(1) Power of Image', 'WakeUp', 'Legacy', 'Fraud(2) The sound from deep water', 'Melancholy Holiday(2) Find the Profile', 'Kaiser', 'RNA', 'The_Sword', 'Fraud(1) Whistle blowing', 'DO U KNOW BASIC?', 'SSS', 'DH', 'Prime', 'Matryoshka64', 'bach', 'ShellScript', 'RSALibrary', 'RSAES', 'STRIKE', 'Mujulla', 'Chase(3) maldocker']
for key, lists in data.items():
    for list in lists:
        text_file.write("------------------------------------------------" + '\r\n')
        for key2, value2 in list.items():
            if key2 in ('name'):
                text_file.write(str(key2) + ' : ' + str(value2) + '\r\n')
            # if key2 in ('hints'):
            #     for i in range(len(value2)):
            #         if i == 0:
            #             text_file.write('ヒント1】\r\n')
            #         if i == 1:
            #             text_file.write('ヒント2】\r\n')
            #         for hintkey, hintval in value2[i].items():
            #             if hintkey == 'cost':
            #                 text_file.write('減点:' + str(hintval) + '\r\n')
            #             if hintkey == 'hint':
            #                 text_file.write(hintval + '\r\n')
                            # soup = BeautifulSoup(hintval)
                            # image_tags = soup.findAll('img')
                            # for image in image_tags:
                            #     filename = os.path.basename(image['src'])
                            #     imgdata = browser.open('https:test3' + image['src']).read()
                            #     browser.back()
                            #     save = open('out/' + filename, 'wb')
                            #     save.write(imgdata)
                            #     save.close()

            if key2 in ('id'):
                solvelink = 'https://test4' + str(value2) + '/explanation'
                solveresponse = browser.open(solvelink)
                solvedata = json.loads(solveresponse.read()) 
                for key3, value3 in solvedata.items():
                    for key4, value4 in value3[0].items():
                        if key4 == 'explanation':
                            text_file.write('【解説】\r\n')
                            text_file.write(value4 )
                            text_file.write('\r\n')
                            soup2 = BeautifulSoup(value4)
                            image_tags = soup2.findAll('img')
                            for image in image_tags:
                                filename = os.path.basename(image['src'])
                                imgdata2 = browser.open('https:test5' + image['src']).read()
                                browser.back()
                                save = open('out/' + filename, 'wb')
                                save.write(imgdata2)
                                save.close()


# print(str(response2.read(), 'utf-8'))
# browser.find_link(text='Lookfor')
# req = browser.click_link(text='Lookfor', nr=0)
# browser.open(req)
#print(str(browser.response().read(), 'utf-8'))