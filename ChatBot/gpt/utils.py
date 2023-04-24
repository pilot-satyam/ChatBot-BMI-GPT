import openai

# Replace with your OpenAI API key
openai.api_key = "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"

def calculate_bmi(height, weight):
    """
    Calculates the Body Mass Index (BMI) given the height (in cm) and weight (in kg) of a person.
    """
    return round((weight / (height / 100)**2), 1)

def get_recommendations(bmi):
    """
    Calls OpenAI's GPT-3 API to generate personalized diet, exercise, and medical test recommendations
    based on the given BMI.
    """
    # Call ChatGPT to get diet recommendations
    try:
        prompt = f"What are some diet recommendations for a {bmi:.1f} BMI?"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Parse the response and extract the diet recommendations
        diet_recommendations = response.choices[0].text.strip()
    except:
        # If the ChatGPT API fails, use default recommendations
        if bmi < 18.5:
            diet_recommendations = "Eat more protein and calories to gain weight."
        elif bmi >= 18.5 and bmi < 25:
            diet_recommendations = "Eat a balanced diet with plenty of fruits, vegetables, and whole grains."
        elif bmi >= 25 and bmi < 30:
            diet_recommendations = "Eat a low-calorie diet and exercise regularly to lose weight."
        else:
            diet_recommendations = "Eat a low-calorie diet and exercise regularly to lose weight. Consider consulting a doctor or nutritionist for personalized recommendations."

    try:
        # Call ChatGPT to get exercise recommendations
        prompt = f"What are some exercise recommendations for a {bmi:.1f} BMI?"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Parse the response and extract the exercise recommendations
        exercise_recommendations = response.choices[0].text.strip()
    except:
        # If the ChatGPT API fails, use default recommendations
        if bmi < 18.5:
            exercise_recommendations = "Do strength training exercises and lift heavy weights to build muscle."
        elif bmi >= 25 and bmi < 30:
            exercise_recommendations = "Aim for 60 minutes of moderate exercise (such as brisk walking or cycling) most days of the week."
        else:
            exercise_recommendations = "Aim for 60-90 minutes of moderate exercise (such as brisk walking or cycling) most days of the week. Consider consulting a doctor or personal trainer to create a personalized exercise plan."
    
    # Add test recommendations based on BMI
    if bmi < 18.5:
        test_recommendations = "Consider getting a blood test to check for nutritional deficiencies."
    elif bmi >= 18.5 and bmi < 25:
        test_recommendations = "None"
    else:
        test_recommendations = "Blood tests for diabetes, cholesterol, and liver function; Electrocardiogram; Stress test"

    return bmi, diet_recommendations, exercise_recommendations, test_recommendations
