def validateKW(kw):

    if kw is None or len(kw) != 15:
        return False

    kw = kw.upper()
    letter_values = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
        'W', 'Y', 'Z'
    ]

    def get_letter_value(letter):
        for j in range(len(letter_values)):
            if letter == letter_values[j]:
                return j
        return -1

     if kw[4] != '/' or kw[13] != '/':
        return False

    for i in range(2):
        if get_letter_value(kw[i]) < 10:
            return False

    if get_letter_value(kw[2]) < 0 or get_letter_value(kw[2]) > 9:
        return False

    if get_letter_value(kw[3]) < 10:
        return False

    for i in range(5, 13):
        if get_letter_value(kw[i]) < 0 or get_letter_value(kw[i]) > 9:
            return False

    sum = (1 * get_letter_value(kw[0]) +
           3 * get_letter_value(kw[1]) +
           7 * get_letter_value(kw[2]) +
           1 * get_letter_value(kw[3]) +
           3 * get_letter_value(kw[5]) +
           7 * get_letter_value(kw[6]) +
           1 * get_letter_value(kw[7]) +
           3 * get_letter_value(kw[8]) +
           7 * get_letter_value(kw[9]) +
           1 * get_letter_value(kw[10]) +
           3 * get_letter_value(kw[11]) +
           7 * get_letter_value(kw[12])) % 10

    if kw[14] != str(sum):
        return False

    return True


def validateKWDivided(court, id, check_digit):
    return validateKW(court + '/' + id + '/' + check_digit)
    
    
def generate_land_register_numbers(court):
    check_digits = [str(x) for x in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']

    for i in range(10000000):
        id = str(i).zfill(8)
        for check_digit in check_digits:
            kw = court + '/' + id + '/' + check_digit
            if validateKW(kw):
                print(kw)
       
generate_land_register_numbers('WL1A')

