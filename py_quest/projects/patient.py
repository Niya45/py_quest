def symptm(*symptoms, **patient_info):
    print("Known symptoms:")
    for symptom in symptoms:
        print(f"- {symptom}")
    print()
    
    print("Patient info: ")
    for key, value in patient_info.items():
        print(f"{key} : {value}")
    
symptm("cough", "rashes", "blood clot", "fever",
       name="tony",
       age="45",
       sex="M",
       medical_history="cancer",
       allergy="bullet trains")