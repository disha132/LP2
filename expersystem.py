# Simple Medical Expert System

print("=== Hospital Expert System ===")
print("Answer with yes or no\n")

fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
headache = input("Do you have headache? ").lower()
stomach = input("Do you have stomach pain? ").lower()

print("\n--- Diagnosis Result ---")

if fever == "yes" and cough == "yes":
    print("You may have Flu or Viral Infection.")
    print("Suggestion: Drink fluids and consult a doctor.")

elif fever == "yes" and headache == "yes":
    print("You may have Migraine or Fever Infection.")
    print("Suggestion: Take rest and proper medication.")

elif stomach == "yes":
    print("You may have Gastric or Digestive Problem.")
    print("Suggestion: Avoid oily food and stay hydrated.")

else:
    print("Symptoms are unclear.")
    print("Please consult a medical professional.")
