import ast
valid_passports = 0
passports = []

def PassportValid(passport):
    passportValid = False
    if all(x in passport for x in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
        passportValid = True
    return passportValid

with open ('input.txt', 'r') as _file:
    passports = _file.read().split('\n\n')
    for passport in passports:
        passport = passport.replace('\n', ' ')
        passport = dict(item.split(':') for item in passport.split(' '))
        if PassportValid(passport):
            valid_passports = valid_passports + 1

print 'Valid Passports: ' + str(valid_passports)

