import requests
from datetime import datetime as dt

APP_ID = "5fb75669"
APP_KEYS = "75930c2625d193f71f88ad5dd6613a3a"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEYS,
    "Content-Type": "application/json"
}

data = {
    "query": "running",
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 160,
    "age": 41
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me, what exercise did you do today? ")

response = requests.post(url=url, json=data, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
exercise = result['exercises'][0]['user_input']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

print(exercise, duration, calories)
USERNAME = "Jim McKeown"
PROJECTNAME = "My Workouts App"
SHEETNAME = "My Workouts App"

sheety_url = "https://api.sheety.co/55b89bfbfd63b45f11e9bd1c7f988e16/myWorkoutsApp/workouts"
today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

sheety_data = {
    "workouts": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 232i043"
    # }

response_sheet = requests.post(url=sheety_url, headers = sheety_headers, json=sheety_data)
response_sheet.raise_for_status()
print(response_sheet.text)

