# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:34:18 2021

@author: Michael
"""

import requests
import json
from collections import namedtuple


def determine_eqs(data_5, data_95):
    str_m = (-float(data_95['str']) + float(data_5['str'])) / 90
    rng_m = (-float(data_95['range']) + float(data_5['range'])) / 90
    str_c = data_5['str'] - 95*str_m
    rng_c = data_5['range'] - 95*rng_m
    return str_m, str_c, rng_m, rng_c


BowMatEq = namedtuple('BowMatEq', ['str_m', 'str_c', 'rng_m', 'rng_c', 'dura'])

# bowMechanics = ('decurve', 'recurve', 'flat')
# bowTypes = ('short', 'long', 'asym')
bowMechanics = ['flat',]
bowTypes = ('long', 'asym')
bowMats = (
    'denseCrepite',
    'crepite',
    'molarium',
    'greatHorn',
    'compHorn',
    'horn',
    'ironBone',
    'boneTissue',
    'spongeWood',
    'whiteWood',
    'firmWood',
    'greyWood',
    'dappleWood',
    'brownWood',
    'blackWood',
    'ironWood',
    'stoneWood'
)

bowData = {}

for Mechanic in bowMechanics:
    for Type in bowTypes:
        for leftMat in bowMats:
            for rightMat in bowMats:
                userdata = {
                    "bellyMat"    : rightMat,
                 	"backMat"     : leftMat,
                 	"sliderPerc"  : "5",
                 	"bowType"     : Type,
                 	"bowMechanic" : Mechanic   
                }
                resp = requests.post('https://www.mortalonlinemap.info/emulator/calc.php', params=userdata)
                data_5 = resp.json()
                userdata = {
                    "bellyMat"    : rightMat,
                 	"backMat"     : leftMat,
                 	"sliderPerc"  : "95",
                 	"bowType"     : Type,
                 	"bowMechanic" : Mechanic    
                }
                resp = requests.post('https://www.mortalonlinemap.info/emulator/calc.php', params=userdata)
                data_95 = resp.json()
                bowData[f"{Mechanic}_{Type}_{leftMat}_{rightMat}"] = BowMatEq(*determine_eqs(data_5, data_95), data_5['dura'])
            print(f'{Mechanic}, {Type}, {leftMat}')
            userdata = {
                "bellyMat"    : leftMat,
             	"backMat"     : leftMat,
             	"sliderPerc"  : "100",
             	"bowType"     : Type,
             	"bowMechanic" : Mechanic   
            }
            resp = requests.post('https://www.mortalonlinemap.info/emulator/calc.php', params=userdata)
            data = resp.json()
            bowData[f"{Mechanic}_{Type}_{leftMat}_{leftMat}"] = BowMatEq(*determine_eqs(data, data), data['dura'])

with open('bow_data.json', 'w') as fp:
    json.dump(bowData, fp)
