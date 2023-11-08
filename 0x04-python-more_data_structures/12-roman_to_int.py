def roman_to_int(roman_string):
 mapping_char  = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        
    min_number = None
    total = 0
    for letter in roman_string:
        returned_value = mapping_char[letter]
        print(returned_value)
        if min_number and returned_value > min_number:
            total -= min_number*2
        else:
            min_number = returned_value
        total += returned_value
                
    return total
