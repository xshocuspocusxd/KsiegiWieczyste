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
    
    
def generate_land_register_numbers(court, filename):
    check_digits = [str(x) for x in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']

    with open(filename, 'w') as f:
        for i in range(10000000):
            id = str(i).zfill(8)
            for check_digit in check_digits:
                kw = court + '/' + id + '/' + check_digit
                if validateKW(kw):
                    print(kw)
                    f.write(kw + '\n')


courts = ["WL1A", "SU1A", "OL1Y", "PT1B", "KA1B", "LU1B", "RA2G", "KO1B", "BI1B", "BB1B", "BI1P", "ZA1B", "OL1B", "TR1O", "JG1B",
"EL1B", "TO1B", "OP1B", "TR1B", "LD1B", "KS1B", "KI1B", "BY1B", "KA1Y", "SL1B", "LU1C", "TO1C", "PO1H", "SL1C", "KA1C", "SZ1C", "KR1C", "PL1C", "BB1C",
"PO2T", "KR1K", "CZ1C", "SL1Z", "KA1D", "TR1D", "RZ1D", "KR2Y", "KO1D", "EL1D", "SW1D", "EL1E", "OL1E", "SI1G", "GD1G", "GD1Y", "OL1G", "GL1G", "LE1G",
"OP1G", "PO1G", "SZ1O", "TO1G", "NS1G", "GW1G", "PL1G", "PO1Y", "LM1G", "WA1G", "PO1S", "RA1G", "TO1U", "SZ1G", "SZ1Y", "ZG2K", "BI2P", "ZA1H", "EL1I",
"BY1I", "ZA1J", "KZ1J", "PR1J", "KS1J", "GL1J", "LE1J", "KA1J", "JG1J", "KI1J", "KZ1A", "JG1K", "SZ1K", "GD1R", "KA1K", "KI1I", "OP1K", "KZ1E", "OL1K",
"KR2E", "KI1L", "OP1U", "CZ2C", "SW1K", "TB1K", "KO1L", "KN1K", "KN1N", "KI1K", "KO1K", "PO1K", "GD1E", "RA1K", "KR1P", "ZA1K", "LU1K", "KS1K", "ZG1K",
"KZ1R", "KR2K", "LD1K", "GD1I", "WA1L", "LE1L", "KS1E", "PO1L", "RZ1E", "SL1L", "OL1L", "NS1L", "WL1L", "RA1L", "PR1L", "JG1L", "LU1A", "LE1U", "CZ1L",
"LU1I", "JG1S", "RZ1A", "SR1L", "LD1Y", "SZ1L", "LM1L", "SI2S", "LD1O", "LD1M", "LU1U", "GD1M", "SL1M", "KR1M", "TB1M", "PO2A", "GW1M", "KA1M", "WR1M",
"SI1M", "PL1M", "BY1M", "EL2O", "OL1M", "NS2L", "NS1M", "KA1L", "CZ1M", "KR1Y", "SZ1M", "BY1N", "OL1N", "KR2I", "TB1N", "SW2K", "ZG1N", "EL1N", "GD2M",
"WA1N", "NS1S", "NS1T", "PO1N", "OP1N", "PO1O", "OL1C", "OP1L", "WR1E", "KR1O", "OL1O", "WR1O", "KI1T", "PT1O", "LU1O", "OP1O", "OS1O", "KI1O", "EL1O",
"OS1M", "KZ1W", "KZ1O", "KR1E", "WA1O", "LD1P", "SR2W", "WA1I", "PO1I", "KI1P", "RA2Z", "PT1P", "OL1P", "KZ1P", "PL1P", "PL1L", "SR2L", "SZ2S", "PO1P",
"PO2P", "KR1H", "OP1P", "WA1P", "OS1P", "PR1P", "PR1R", "RA1P", "KA1P", "GD2W", "LU1P", "OS1U", "SZ2T", "GL1R", "RA1R", "PT1R", "WL1R", "LU1R", "LD1R",
"PO1R", "RZ1R", "GL1S", "GL1Y", "LU1Y", "WL1Y", "RZ1Z", "KI1S", "KS1S", "SU1N", "BY2T", "SI1S", "KA1I", "BI3P", "PR2R", "SR1S", "PL1E", "KR2P", "KI1R",
"KR3I", "LD1H", "KO1E", "KR1S", "GW1S", "KN1S", "SL1S", "PL1O", "SI1P", "BI1S", "GD1S", "KA1S", "TB1S", "KI1H", "SZ1T", "GD1A", "KI1A", "GW1K", "OP1S",
"WR1T", "RZ1S", "KR1B", "ZG2S", "GW1U", "SU1S", "PO1A", "KO1I", "SZ1S", "OL1S", "GD2I", "BY1U", "RA1S", "PO1M", "WR1S", "PO1D", "SW1S", "KO2B", "ZG1S",
"BY1S", "SZ1W", "TB1T", "GL1T", "TR1T", "GD1T", "ZA1T", "PT1T", "TO1T", "PO1T", "WR1W", "BY1T", "TR2T", "KN1T", "KA1T", "RZ2Z", "KS2E", "KR1W", "SW1W",
"KO1W", "WA3M", "WA1M", "WA2M", "WA4M", "WA5M", "WA6M", "TO1W", "PO1B", "GD1W", "OL2G", "SI1W", "KR1I", "SR1W", "WL1W", "LU1W", "KI1W", "GL1W", "PO1E",
"WA1W", "WR1L", "WR1K", "PO1F", "ZG1W", "PO2H", "LM1W", "OS1W", "GL1Z", "NS1Z", "LM1Z", "ZA1Z", "CZ1Z", "SW1Z", "SR1Z", "LD1G", "JG1Z", "ZG1E", "LE1Z",
"PO1Z", "RA1Z", "ZG1G", "ZG1R", "BY1Z", "GL1X", "PL2M", "PL1Z", "BB1Z"]

for court in courts:
    generate_land_register_numbers(court, court + '.txt')