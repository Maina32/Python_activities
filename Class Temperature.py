class Temperature:
    def convert_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")

    def convert_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")


temp = Temperature()

# Convert Celsius to Fahrenheit
temp.convert_to_fahrenheit(35)

# Convert Fahrenheit to Celsius
temp.convert_to_celsius(95.0)