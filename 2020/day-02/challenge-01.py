with open ('input.txt', 'r') as _file:
    valid_passwords = 0
    for val in _file:
        chunk = val.split()

        # Get different parts of the chunk
        limits = chunk[0].split('-')
        letter_to_check = chunk[1].split(':')[:1]
        password = chunk[2]
        letter_count = 0
        for i in password:
            if i == letter_to_check[0]:
                letter_count = letter_count + 1

        print 'Letter to check: ' + letter_to_check[0] + '; against password: ' + password +  '; Total letter_count: ' + str(letter_count) + '; Limits: ' + limits[0] + '-' + limits[1]
        if int(limits[0]) <= letter_count <= int(limits[1]):
            valid_passwords = valid_passwords + 1

print 'Valid password: ' + str(valid_passwords)