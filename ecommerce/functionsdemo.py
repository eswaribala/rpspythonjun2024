# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:17:09 2018

@author: Balasubramaniam
"""
from datetime import date;

holidayList = {
    '1/1/2018': 'New  year',
    '14/1/2018': 'Pongal',
    '26/1/2018': 'Republic Day'
}

account = {
    'accountNo': 23864585,
    'balance': 45000
}

import datetime;


def fundTransfer(fromAccountNo, toAccountNo, amount):
    currentTime = datetime.datetime.now().hour;
    print(currentTime)
    if (account['accountNo'] == fromAccountNo):
        if (account['balance'] > int(amount)):
            if (currentTime > 21):
                print("Fund Transfer will happen in next working day");
            else:
                print("Fund transfer initiated to Account No %d"
                      % (toAccountNo));


def check(data):
    status = False;
    for key in holidayList.keys():

        if (key == data):

            status = True;
            print(holidayList[key]);
            break;
        else:
            status = False;
    if (status is False):
        print("Working Day....");
