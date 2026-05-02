#temperature conversion

def convert_cel_to_far(celsius):
    fahrenheit_float = float(celsius) * (9 / 5) + 32
    return f"{fahrenheit_float:.2f}F"

def convert_far_to_cel(fahrenheit):
    celsius_float = float(fahrenheit - 32) * (5 / 9)
    return f"{celsius_float:.2f}C"

temps = [22, 0, 100, 38.8, 42.6]
# for temp in temps:
#     print(f"{temp}C is {convert_cel_to_far(temp)}")
    
# for temp in temps:
#     print(f"{temp}F is {convert_far_to_cel(temp)}")

#Combined function taking both C anf F values
def temperature_converter(temp) -> str:
    #trim the last char with temp[:-1] and convet to float
    temperature_value = float(temp[:-1])
    #terneray operator with or
    selector = temp[len(temp)-1] == "C" or "F"
  
    if selector is True :
        convert_temp = convert_cel_to_far(temperature_value)
    else:
        convert_temp = convert_far_to_cel(temperature_value)
        
    return f"{temp} conversion: {convert_temp}"

temperatures = {
    0     : "C", 
    20    : "F",  
    37.2  : "C", 
    40    : "F", 
    72    : "F",
    100   : "C"
}

for temperature in temperatures:
    #Access key 'temperature' float to get the value: temperatures[temperature]
    convert_from_tempreature = f"{temperature}{temperatures[temperature]}"
    print(temperature_converter(convert_from_tempreature))