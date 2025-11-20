# from _ import _ statement was used to be able to use type hinting
# --- Type hinting ---
from typing import List, Dict, Tuple, Any, Optional


# A patient record
PatientRecord = List[Any]
PatientsList = List[PatientRecord]

# A doctor record
DoctorRecord = List[str]
DoctorsList = List[DoctorRecord]

# Map of symptoms
SymptomMap = Dict[str, Tuple[str, int]]


# --- Input data ---
registration_of_patients: PatientsList = [
    ["Nathan Drake", 20, "male", ("fever",)],
    ["Ellie Williams", 42, "female", ("fracture",)],
    ["Arthur Morgan", 35, "male", ("depression",)],
    ["Lara Croft", 63, "female", ("diabetes",)]
]


doctors_staff: DoctorsList = [
    ["Peter Pan", "General practice"],
    ["Hermione Granger", "Traumatology"],
    ["Geralt of Rivia", "Endocrinology"],
    ["Taylor Swift", "Psychology"]
]


symptom_speciality: SymptomMap = {
    # A dictionary with keys (illnesses) and values (a tuple with a speciality
    # and an urgency value)
    # The Urgency scale goes from 2, which is the lowest value, to 5 (highest value)
    # Urgency scale -> (Highest = 5, Lowest = 2)
    "fever": ("General practice", 2),
    "fracture": ("Traumatology", 4),
    "diabetes": ("Endocrinology", 3),
    "depression": ("Psychology", 3),
    "chest pain": ("Cardiology", 5),
}


# Secondary functions' definition
# --- Definition of auxiliary functions ---
def speciality_by_symptoms(patient: PatientRecord) -> Optional[str]:
    """

    1. Finds the needed speciality to treat a certain symptom.
    Returns the appropriate value to its key.
    """
    name, age, gender, symptoms = patient
    for symptom in symptoms:
        if symptom in symptom_speciality:
            return symptom_speciality[symptom][0]
    return None


def doctors_by_speciality(doctors_staff: DoctorsList, speciality: str) -> Optional[str]:
    """

    2. Finds the name of a doctor belonging to a specific speciality.
    Returns the name of the doctor if the coincidence is found.
    """
    for doctor in doctors_staff:
        doctors_name, doctors_speciality = doctor
        if doctors_speciality == speciality:
            return doctors_name


# Main function
def main_function(registration_of_patients: PatientsList, doctors_staff: DoctorsList) -> List[str]:
    """
    Main function
    3. Iterates through each patient, determines the required speciality, finds a suitable doctor, and indicates the urgency.
    Returns the assignment for each patient, which is a list of strings.
    """
    result: List[str] = []
    for patient in registration_of_patients:
        name, age, gender, symptoms = patient
        symptom = symptoms[0]
        needed_speciality_from_map, priority = symptom_speciality[symptom]
        needed_speciality = speciality_by_symptoms(patient)
        chosen_doctor = doctors_by_speciality(doctors_staff, needed_speciality)
      
        message = f"Patient's name: {name}, Assigned doctor: {chosen_doctor}, Medical area: {needed_speciality}, Urgency: {priority}"
        result.append(message)
    return result


for line in main_function(registration_of_patients, doctors_staff):
    print(line)
