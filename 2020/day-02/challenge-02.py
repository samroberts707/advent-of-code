def split(word): 
    return [char for char in word]  

with open ('input.txt', 'r') as _file:
    valid_passwords = 0
    for val in _file:
        chunk = val.split()

        # Get different parts of the chunk
        limits = chunk[0].split('-')
        letter_to_check = chunk[1].split(':')[:1]
        password = split(chunk[2])

        print 'Letter to check: ' + letter_to_check[0] + '; against: ' + password[int(limits[0]) - 1] + '-' + password[int(limits[1]) - 1]

        if password[int(limits[0]) - 1] == letter_to_check[0] and password[int(limits[1]) - 1] == letter_to_check[0]:
            print 'Password not valid'
        elif password[int(limits[0]) - 1] == letter_to_check[0]:
            valid_passwords = valid_passwords + 1
            print 'Password valid'
        elif password[int(limits[1]) - 1] == letter_to_check[0]:
            valid_passwords = valid_passwords + 1
            print 'Password valid'
        else:
            print 'Password not valid'

print 'Valid password: ' + str(valid_passwords)