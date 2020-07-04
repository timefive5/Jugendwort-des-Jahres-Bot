import requests
import time
import re
bold_start = '\033[1m'
bold_end   = '\033[0m'

alter10bis15 = '3067519627'
alter16bis20 = '3067519628'
alter21bis30 = '3067519629'
alter30undmehr = '3067519630'
AbstimmungsUrl = 'https://www.surveymonkey.com/r/7JZRVLJ?embedded=1'
Wort = 'Hurensohn'

i = 0

while i < 10:
    print('warte 5 Sekunden')
    time.sleep(5)
    print('beziehe Daten vom Server')
    r = requests.get(AbstimmungsUrl)
    survey_data = re.search(r'survey_data" value="(.*?)" />', r.text).group(1)
    daten1 = {
        '463803414': alter10bis15,
        '463803684': Wort,
        '483089934[]': '3189794655',
        'is_previous': 'false',
        'disable_survey_buttons_on_submit': '',
        'survey_data': survey_data
    }
    print('warte 5 Sekunden')
    time.sleep(5)
    print('stimme ab mit Alter 10 bis 15')
    r1 = requests.post(AbstimmungsUrl, data = daten1)
    print(bold_start, 'Abgestimmt mit Alter 10 bis 15!', bold_end)
    print('warte 5 Sekunden')
    time.sleep(5)
    print('beziehe Daten vom Server')
    r = requests.get(AbstimmungsUrl)
    survey_data = re.search(r'survey_data" value="(.*?)" />', r.text).group(1)
    daten2 = {
        '463803414': alter16bis20,
        '463803684': Wort,
        '483089934[]': '3189794655',
        'is_previous': 'false',
        'disable_survey_buttons_on_submit': '',
        'survey_data': survey_data
    }
    print('warte 5 Sekunden')
    time.sleep(5)
    print('stimme ab mit Alter 16 bis 20')
    r1 = requests.post(AbstimmungsUrl, data = daten2)
    print(bold_start, 'Abgestimmt mit Alter 16 bis 20!', bold_end)
    print('warte 5 Sekunden')
    time.sleep(5)
    print('beziehe Daten vom Server')
    r = requests.get(AbstimmungsUrl)
    survey_data = re.search(r'survey_data" value="(.*?)" />', r.text).group(1)
    daten3 = {
        '463803414': alter21bis30,
        '463803684': Wort,
        '483089934[]': '3189794655',
        'is_previous': 'false',
        'disable_survey_buttons_on_submit': '',
        'survey_data': survey_data
    }
    print('warte 5 Sekunden')
    time.sleep(5)
    print('stimme ab mit Alter 21 bis 30')
    r1 = requests.post(AbstimmungsUrl, data = daten3)
    print(bold_start, 'Abgestimmt mit Alter 21 bis 30!', bold_end)
    print('warte 5 Sekunden')
    time.sleep(5)
    print('beziehe Daten vom Server')
    r = requests.get(AbstimmungsUrl)
    survey_data = re.search(r'survey_data" value="(.*?)" />', r.text).group(1)
    daten4 = {
        '463803414': alter30undmehr,
        '463803684': Wort,
        '483089934[]': '3189794655',
        'is_previous': 'false',
        'disable_survey_buttons_on_submit': '',
        'survey_data': survey_data
    }
    print('warte 5 Sekunden')
    time.sleep(5)
    print('stimme ab mit Alter 30+')
    r1 = requests.post(AbstimmungsUrl, data = daten4)
    print(bold_start, 'Abgestimmt mit Alter 30+!', bold_end)