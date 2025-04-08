class patients:
    def __init__(self, name, age, date, medical_history):
        self.name = name
        self.age = age
        self.date = date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Date: {self.date}, Medical History: {self.medical_history}")

# Example usage:
# Create a patient record
patient1 = patients("Macbeth Smith", 50, "2020-05-11", "Insomnia")
# Print the patient's details
patient1.print_details()  