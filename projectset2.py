measure_in_cm = float(input("Enter a measurement in centimeters: "))
def convert_cm_to_imperial(measure_in_cm):
  feet = 0.0328 * measure_in_cm
  inches1= 0.393701 * measure_in_cm
  inches = inches1 - int(feet) * 12
  return f"Someone {measure_in_cm} cm tall is {int(feet)}' {round(inches,1)}\" tall."
print(convert_cm_to_imperial(measure_in_cm))