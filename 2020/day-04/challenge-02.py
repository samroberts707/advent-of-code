import re
valid_passports = 0
passports = []

def checkHeight(val):
    height_type = val[-2:]
    if height_type == 'cm':
        height_val = int(val[:-2])
        if 150 <= height_val <= 193:
            return True
        else: return False
    elif height_type == 'in':
        height_val = int(val[:-2])
        if 59 <= height_val <= 76:
            return True
        else: return False
    else: return False

def PassportValid(passport):
    passportValid = False
    # If all values are present
    if all(x in passport for x in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
        passportValid = True
        # Check Birth Year
        if passport['byr'] != range(1920, 2002):
            passportValid = False
        # Check issue year
        # if passport['iyr'] != range(2010, 2020):
        #     passportValid = False
        # Check expiry year
        # if passport['eyr'] != range(2020, 2030):
        #     passportValid = False
        # Check correct height
        # if checkHeight(passport['hgt']) == False:
        #     passportValid = False
        # Check valid hair colour
        # print re.match("^[A-Za-z0-9_-]*$", passport['hcl'][-6:])
        # if passport['hcl'][:1] != '#' and re.match("^[A-Za-z0-9_-]*$", passport['hcl'][-6:]):
        #     passportValid = False
        # Check eye colour is valid
        # print any(passport['ecl'] in x for x in ['amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth'])
        # if any(passport['ecl'] in x for x in ['amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth'] ) == False:
        #     passportValid = False
        # Check passport id is valid
        # if len(passport['pid']) != 9 and passport['pid'][:2] != 00:
        #     passportValid = False

    return passportValid

with open ('input.txt', 'r') as _file:
    passports = _file.read().split('\n\n')
    for passport in passports:
        passport = passport.replace('\n', ' ')
        passport = dict(item.split(':') for item in passport.split(' '))
        if PassportValid(passport):
            valid_passports = valid_passports + 1

print 'Valid Passports: ' + str(valid_passports)

