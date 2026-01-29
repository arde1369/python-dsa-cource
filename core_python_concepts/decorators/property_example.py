class Temperature:
    def __init__(self, celsius):
        # Internal attribute is prefixed with an underscore. NEED TO ENSURE IT IS PREFIXED WITH _ OTHERWISE IT WILL RECURSIVELY CALL THE SETTER METHOD.
        self._celsius = celsius

    # The 'getter' method, accessed like an attribute
    @property
    def celsius(self):
        print("Getting temperature...")
        return self._celsius

    # The 'setter' method, used when the attribute is assigned a value
    @celsius.setter
    def celsius(self, value):
        if value < -273.15: # Absolute zero in Celsius
            raise ValueError("Temperature below absolute zero is not possible.")
        print("Setting temperature...")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    

# Create an object
t = Temperature(25)

# Access the property (calls the getter)
print(f"Current Celsius temp: {t.celsius}") 
# Output:
# Getting Celsius value...
# Current Celsius temp: 25

# Set the property (calls the setter with validation)
t.celsius = 30
print(f"New Celsius temp: {t.celsius}")
# Output:
# Setting Celsius value...
# Getting Celsius value...
# New Celsius temp: 30

# Access the read-only fahrenheit property
print(f"Fahrenheit equivalent: {t.fahrenheit}")
# Output:
# Getting Celsius value...
# Fahrenheit equivalent: 86.0