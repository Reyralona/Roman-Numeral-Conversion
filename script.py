ROMAN_N = {
    "I" : 1,
    "IV": 4,
    "V" : 5,
    "IX": 9,
    "X" : 10,
    "XL": 40,
    "L" : 50,
    "XC": 90,
    "C" : 100,
    "CD": 400,
    "D" : 500,
    "CM": 900,
    "M" : 1000
}

def in_dict(num):
    for key, value in ROMAN_N.items():
        if num == value:
            return key
        elif num == key:
            return value
            
def int_to_roman(num):
    if num < 1:
        raise ValueError("Has to be > 1")
        
    in_dict(num)
    
    values_before = []
    roman_numeral = []
    
    while num != 0:
        for key, value in ROMAN_N.items():
            if value <= num:
                values_before.append(value)
        roman_numeral.append(in_dict(max(values_before)))
        num = num - max(values_before)
        values_before.clear()
        
    return "".join(roman_numeral)
    
def roman_to_int(num):
    num = list(num)
    
    result = []
    for char in num:
        result.append(in_dict(char))
        
    return sum(result)
    
while True:
    inp = eval(input("integer to roman >> "))
    print(int_to_roman(inp))
    inp2 = str(input("roman to integer >> "))
    print(roman_to_int(inp2))
