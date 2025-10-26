# FILE: weather_activity_recommender.py
# CONCEPT: Multi-Branch Conditional Logic
# DEMONSTRATES: Using multiple 'elif' statements to suggest activities based on temperature ranges.

def what_to_do_today():
    """Suggests an activity based on the temperature."""
    temperature = float(input("Today's temperature is:"))
    if temperature > 25:
        print("You should swim in the sea")
    elif 10 < temperature:
        print("You should go shopping in Gunwharf Quays")
    else:
        print("You should watch a film at home")
