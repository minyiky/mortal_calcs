from collections import namedtuple

# =============================================================================
# 
# BOW TYPES
# 
# =============================================================================

BowType = namedtuple('BowType', ['str_mult', 'rng_mult', 'rng_plus', 'dur_mult', 'name'])
types = {}

shortBow = BowType(0.7058598180676242, 7/12, 0, 1, "Short")
longBow  = BowType(1.55882352941176, 1.5, 7.5, 1.25, "Long")
# longBow  = BowType(2.20840383531, 1.5, 7.5, 1.25, "Long")
asymBow  = BowType(2.29408530442, 2, 7.5, 1.25, "Asymmetrical")
types[shortBow.name] = shortBow
types[longBow.name] = longBow
types[asymBow.name] = asymBow


# =============================================================================
# 
# BOW MECHANICS
# 
# =============================================================================

BowMechanic = namedtuple('BowMechanic', ['str_short_mult', 'str_long_mult', 'str_asym_mult',
                                         'rng_short_mult', 'rng_long_mult', 'rng_asym_mult',
                                         'dur_mult', 'name'])
mechanics = {}

decurveMechanic = BowMechanic(1, 1, 1, 1, 1, 1, 1, "Decurve") 
recurveMechanic = BowMechanic(
    1.41666666667, 1.18867924528, 1.12820512820512, 
    2.14375975579 , 1.277778, 1.208333,
    0.5, "Recurve") 
flatMechanic = BowMechanic(1.14705885063020, 1.09433964038911, 1.06410258173763, 1.357143, 1.138889, 1.104167, 0.75, "Flat")
mechanics[decurveMechanic.name] = decurveMechanic
mechanics[recurveMechanic.name] = recurveMechanic
mechanics[flatMechanic.name] = flatMechanic

Material = namedtuple('Material', ['belly_str', 'belly_rng', 'back_str', 'back_rng', 'dura', 'name', 'usage'])

materials = {}

# =============================================================================
# 
# A N I M A L   M A T E R I A L S
# 
# =============================================================================

crepite = Material(
    belly_str = 76.5, 
    belly_rng = 57.375, 
    back_str = 100.40625, 
    back_rng = 54, 
    dura = 140, 
    name = "Crepite", 
    usage = {
        'short': 70, 
        'long': 160, 
        'asym': 180, 
        }
)
materials[crepite.name] = crepite

denseCrepite = Material(
    belly_str = 79.9, 
    belly_rng = 61.335, 
    back_str = 106.866241, 
    back_rng  = 56.4, 
    dura      = 170, 
    name       = "Dense Crepite", 
    usage={ 
        'short': 106, 
        'long': 241, 
        'asym': 271, 
        }
)
materials[denseCrepite.name] = denseCrepite

molarium = Material( 
    belly_str = 73.1, 
    belly_rng = 53.535, 
    back_str = 94.116257, 
    back_rng  = 51.6, 
    dura      = 210, 
    name       = "Molarium", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[molarium.name] = molarium

emalj = Material( 
    belly_str = 68.051, 
    belly_rng = 48, 
    back_str = 85.064, 
    back_rng  = 47.973, 
    dura      = 210, 
    name       = "Emalj", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[emalj.name] = emalj

boneTissue = Material( 
    belly_str = 54.4, 
    # belly_str = 38.309342996, 
    belly_rng = 34.56, 
    back_str = 62.56, 
    # back_str = 44.156577704, 
    back_rng  = 38.4, 
    dura      = 145, 
    name       = "Bone Tissue", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0, 
        }
)
materials[boneTissue.name] = boneTissue

ironBone = Material( 
    belly_str = 64.6, 
    belly_rng = 44.46, 
    back_str = 79.135, 
    back_rng  = 45.6, 
    dura      = 230, 
    name       = "Iron Bone", 
    usage = 0, 
)
materials[ironBone.name] = ironBone

horn = Material( 
    belly_str = 64.6, 
    belly_rng = 44.46, 
    back_str = 79.135, 
    back_rng  = 45.6, 
    dura      = 150, 
    name       = "Horn", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[horn.name] = horn

compHorn = Material( 
    belly_str = 68, 
    belly_rng = 48, 
    back_str = 85, 
    back_rng  = 48, 
    dura      = 185, 
    name       = "Compact Horn", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[compHorn.name] = compHorn

greatHorn = Material( 
    belly_str = 71.4, 
    belly_rng = 51.66, 
    back_str = 91.035, 
    back_rng  = 50.4, 
    dura      = 225, 
    name       = "Great Horn", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[greatHorn.name] = greatHorn

# =============================================================================
# 
# W O O D S
# 
# =============================================================================

spongeWood = Material( 
    belly_str = 23.8, 
    belly_rng = 11.34, 
    back_str  = 22.015, 
    back_rng  = 16.8, 
    dura      = 55, 
    name      = "Spongewood", 
    usage={ 
        'short': 18, 
        'long': 18, 
        'asym': 18, 
        }
)
materials[spongeWood.name] = spongeWood

whiteWood = Material( 
    belly_str = 27.2, 
    # belly_str = 19.199387, 
    belly_rng = 13.44, 
    back_str  = 25.84, 
    # back_str  = 18.239418, 
    back_rng  = 19.2, 
    dura      = 75, 
    name      = "Whitewood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0, 
        }
)
materials[whiteWood.name] = whiteWood

dappleWood = Material( 
    belly_str = 35.7, 
    belly_rng = 19.215, 
    back_str  = 36.146248, 
    back_rng  = 25.2, 
    dura      = 150, 
    name      = "Dapplewood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[dappleWood.name] = dappleWood

blackWood = Material( 
    belly_str = 39.1, 
    belly_rng = 21.735, 
    back_str  = 40.56625, 
    back_rng  = 27.6, 
    dura      = 200, 
    name      = "Blackwood", 
    usage={ 
        'short': 50, 
        'long': 113, 
        'asym': 127, 
        }
)
materials[blackWood.name] = blackWood

greyWood = Material( 
    belly_str = 34, 
    # belly_str = 24.001246329, 
    belly_rng = 18,
    back_str  = 34, 
    # back_str  = 23.9437638871, 
    back_rng  = 24, 
    dura      = 125, 
    name      = "Greywood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0, 
        }
)
materials[greyWood.name] = greyWood

firmWood = Material( 
    belly_str = 30.6, 
    belly_rng = 15.66, 
    back_str  = 29.835, 
    back_rng  = 21.6, 
    dura      = 100, 
    name      = "Firmwood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[firmWood.name] = firmWood

brownWood = Material( 
    belly_str = 37.4, 
    belly_rng = 20.46, 
    back_str  = 38.335, 
    back_rng  = 26.4, 
    dura      = 175, 
    name      = "Brownwood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0, 
        }
)
materials[brownWood.name] = brownWood

ironWood = Material( 
    belly_str = 40.8, 
    belly_rng = 23.04, 
    back_str  = 42.84, 
    back_rng  = 28.8, 
    dura      = 225, 
    name      = "Ironwood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[ironWood.name] = ironWood

stoneWood = Material( 
    belly_str = 42.5, 
    belly_rng = 24.375, 
    back_str  = 45.1563, 
    back_rng  = 30, 
    dura      = 275, 
    name      = "Stonewood", 
    usage={ 
        'short': 0, 
        'long': 0, 
        'asym': 0,
        }
)
materials[stoneWood.name] = stoneWood


def calculate(bow_type, bow_mechanic, primary_mat, secondary_mat, percent):
    if bow_type.name == 'Short':
        bow_mechanic_str_mult = bow_mechanic.str_short_mult
        bow_mechanic_rng_mult = bow_mechanic.rng_short_mult
    elif bow_type.name == 'Long':
        bow_mechanic_str_mult = bow_mechanic.str_long_mult
        bow_mechanic_rng_mult = bow_mechanic.rng_long_mult
    else:
        bow_mechanic_str_mult = bow_mechanic.str_asym_mult
        bow_mechanic_rng_mult = bow_mechanic.rng_asym_mult

    bow_str = bow_type.str_mult \
              * bow_mechanic_str_mult \
              * ((primary_mat.back_str * percent) \
                 + (secondary_mat.belly_str * (1 - percent)))

    bow_rng = bow_type.rng_mult \
              * bow_mechanic_rng_mult \
              * ((primary_mat.back_rng * percent) \
                 + (secondary_mat.belly_rng * (1 - percent))) \
              + bow_type.rng_plus

    return bow_str, bow_rng

# %%

if __name__ == '__main__':
    bow_type = types['Long']
    bow_mechanic = mechanics['Decurve']
    primary_mat = materials['Emalj']
    secondary_mat = materials['Whitewood']
    percent = 0.05
    print(calculate(bow_type, bow_mechanic, primary_mat, secondary_mat, percent))
