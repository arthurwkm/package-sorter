#check if all mesuraments are physically possible
def validate_measurements(width, height, length, mass):
    
    return width > 0 and height > 0 and length > 0 and mass > 0

#find which category the package belongs to
def get_package_category(width, height, length, mass):
    
    if not validate_measurements(width, height, length, mass):
        return "Incorrect input, try again"
    
    volume = width * height * length
    
    if volume >= 1000000 and mass >= 20:
        return "REJECTED"   
    if volume >= 1000000 or mass >= 20:
        return "SPECIAL"
    
    return "STANDARD"

#check if there are only 4 inputs
def parse_input(input_str):
    
    try:
        values = input_str.split()
        if len(values) != 4:
            return None
        return [float(x) for x in values]
    except ValueError:
        return None

def main():
    #first checks if input is valid, then calculates the category
    print("Input width, height, length (in cm) and mass (in kg) of the package separating them with a space")
    
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            break
            
        measurements = parse_input(user_input)
        if measurements is None:
            print("Invalid input format. Please enter 4 numbers separated by spaces")
            continue
            
        width, height, length, mass = measurements
        result = get_package_category(width, height, length, mass)
        
        if result == "Incorrect input, try again":
            print(result)
            continue
            
        print(result)
        break

if __name__ == "__main__":
    main()
