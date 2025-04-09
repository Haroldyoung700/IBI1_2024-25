weight = float(input("Enter the weight of the child in kg: "))
strength = float(input("Enter the strength of the paracetamol in mg/5ml (120 or 250): "))


def calculate_paracetamol(weight, strength):
    # Check if the weight is within the allowed range
    if not (10 <= weight <= 100):
        raise ValueError("Weight must be between 10 and 100 kg.")
    # Check if the strength is valid
    if strength not in [120, 250]:
        raise ValueError("Strength must be either 120 mg/5ml or 250 mg/5ml.")
    # Calculate the required volume in ml
    dose_mg = 15 * weight
    volume_ml = (dose_mg / strength) * 5
    return volume_ml
# Attempt to calculate the dosage under certain circumstances
print("The drug required:", calculate_paracetamol(weight, strength), "ml")

#example usage
# weight = 20
# strength = 120
# print("The drug required:", calculate_paracetamol(weight, strength), "ml")    
# weight = 50
# strength = 250
# print("The drug required:", calculate_paracetamol(weight, strength), "ml")