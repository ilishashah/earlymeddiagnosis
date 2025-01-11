from flask import Flask, render_template, request

app = Flask(__name__)

# Function to diagnose conditions based on the symptoms
def diagnose(cough, sorethroat, chestpain, breath, wheezing,
             stomachPain, nausea, vomiting, diarrhea, bloating,
             jointPain, muscleWeakness, stiffness, swelling,
             headache, dizziness, confusion,
             rash, itching, redness,
             f1, f2):
    diagnosis = ""

    # Respiratory Conditions
    if cough and sorethroat and f1 and breath:
        diagnosis += "Possible Condition: COVID-19 or Viral Pneumonia\n"
        diagnosis += "Treatment: Seek medical testing, rest, hydration, and isolation.\n"
    elif cough and sorethroat and f1 and wheezing:
        diagnosis += "Possible Condition: Bronchitis\n"
        diagnosis += "Treatment: Rest, fluids, consider cough medicine. See a doctor if symptoms worsen.\n"
    elif chestpain and breath and dizziness:
        diagnosis += "Possible Condition: Heart Condition (e.g., Angina or Heart Attack)\n"
        diagnosis += "Treatment: Seek immediate medical attention.\n"
    elif cough and breath and wheezing:
        diagnosis += "Possible Condition: Asthma\n"
        diagnosis += "Treatment: Use inhalers, avoid triggers, consult with a doctor.\n"

    # Gastrointestinal Conditions
    if stomachPain and nausea and vomiting and diarrhea:
        diagnosis += "Possible Condition: Gastroenteritis (Stomach Flu)\n"
        diagnosis += "Treatment: Stay hydrated, rest, avoid solid foods until symptoms improve.\n"
    elif stomachPain and bloating and f2:
        diagnosis += "Possible Condition: Irritable Bowel Syndrome (IBS)\n"
        diagnosis += "Treatment: Manage stress, eat a balanced diet, avoid trigger foods.\n"
    elif stomachPain and bloating and nausea:
        diagnosis += "Possible Condition: Gastritis or Peptic Ulcer Disease\n"
        diagnosis += "Treatment: Avoid spicy foods, alcohol, and caffeine. See a gastroenterologist.\n"

    # Musculoskeletal Conditions
    elif jointPain and stiffness and f2:
        diagnosis += "Possible Condition: Arthritis (Osteoarthritis or Rheumatoid Arthritis)\n"
        diagnosis += "Treatment: Regular exercise, weight management, and anti-inflammatory medications.\n"
    elif muscleWeakness and jointPain and f2:
        diagnosis += "Possible Condition: Fibromyalgia\n"
        diagnosis += "Treatment: Exercise, stress management, consult a physician for pain management.\n"
    elif jointPain and swelling and redness:
        diagnosis += "Possible Condition: Gout\n"
        diagnosis += "Treatment: Avoid purine-rich foods, take prescribed medications for pain relief.\n"
    elif swelling and f2:
        diagnosis += "Possible Condition: Edema or Fluid Retention\n"
        diagnosis += "Treatment: Reduce salt intake, elevate legs, consult a doctor if swelling persists.\n"

    # Neurological Conditions
    elif headache and dizziness and confusion:
        diagnosis += "Possible Condition: Migraine or Mild Concussion\n"
        diagnosis += "Treatment: Rest in a dark room, and consult a doctor if symptoms worsen.\n"
    elif dizziness and nausea and vomiting:
        diagnosis += "Possible Condition: Vertigo or Inner Ear Disorder (e.g., Benign Paroxysmal Positional Vertigo)\n"
        diagnosis += "Treatment: Avoid sudden movements, rest, consult an ENT specialist.\n"
    elif confusion and f2:
        diagnosis += "Possible Condition: Alzheimer's Disease or Dementia\n"
        diagnosis += "Treatment: See a neurologist for further evaluation.\n"

    # Skin-Related Conditions
    elif rash and itching and redness:
        diagnosis += "Possible Condition: Allergic Reaction or Dermatitis\n"
        diagnosis += "Treatment: Use moisturizers or creams, avoid known allergens, consult a dermatologist if it worsens.\n"
    elif f1 and rash and jointPain:
        diagnosis += "Possible Condition: Dengue Fever or Viral Infection\n"
        diagnosis += "Treatment: See a doctor immediately, avoid anti-inflammatory drugs.\n"
    elif rash and f1 and f2:
        diagnosis += "Possible Condition: Chickenpox or Measles\n"
        diagnosis += "Treatment: Rest, hydration, and consult a doctor if symptoms worsen.\n"

    # General Conditions
    elif f2 and f1 and muscleWeakness:
        diagnosis += "Possible Condition: Mononucleosis (Mono) or Chronic Fatigue Syndrome\n"
        diagnosis += "Treatment: Rest, hydration, and stress management.\n"
    elif f1 and f2 and jointPain:
        diagnosis += "Possible Condition: Lupus or Rheumatoid Arthritis\n"
        diagnosis += "Treatment: Consult a rheumatologist for proper diagnosis and treatment.\n"

    else:
        diagnosis += "Diagnosis: Unable to diagnose based on provided symptoms.\n"
        diagnosis += "Recommendation: Consult a healthcare professional for further evaluation.\n"

    return diagnosis


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/symptoms', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data (convert checkboxes to booleans)
        cough = 'cough' in request.form
        sorethroat = 'sorethroat' in request.form
        chestpain = 'chestpain' in request.form
        breath = 'breath' in request.form
        wheezing = 'wheezing' in request.form
        stomachPain = 'stomachPain' in request.form
        nausea = 'nausea' in request.form
        vomiting = 'vomiting' in request.form
        diarrhea = 'diarrhea' in request.form
        bloating = 'bloating' in request.form
        jointPain = 'jointPain' in request.form
        muscleWeakness = 'muscleWeakness' in request.form
        stiffness = 'stiffness' in request.form
        swelling = 'swelling' in request.form
        headache = 'headache' in request.form
        dizziness = 'dizziness' in request.form
        confusion = 'confusion' in request.form
        rash = 'rash' in request.form
        itching = 'itching' in request.form
        redness = 'redness' in request.form
        f1 = 'f1' in request.form
        f2 = 'f2' in request.form

        # Call the diagnose function and generate diagnosis
        diagnosis = diagnose(cough, sorethroat, chestpain, breath, wheezing,
                              stomachPain, nausea, vomiting, diarrhea, bloating,
                              jointPain, muscleWeakness, stiffness, swelling,
                              headache, dizziness, confusion,
                              rash, itching, redness,
                              f1, f2)

        return render_template('result.html', diagnosis=diagnosis)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
