# FILE: rainfall_chart_generator.py
# CONCEPT: File I/O, String Splitting, and Data Visualization
# DEMONSTRATES: Reading structured data from a file, splitting it by word, and using string multiplication (`*`) 
#               to generate a basic bar chart visualization.

def rainfall_chart():
    # NOTE: Assumes 'rainfall.txt' contains lines like 'CityName 15'
    try:
        with open("rainfall.txt", "r") as input_file:
            lines = input_file.readlines()
            for line in lines:
                # split() without arguments splits by any whitespace
                city, rainfall = line.split()
                rainfall = int(rainfall)
                # Prints the city name followed by the appropriate number of stars
                print(f"{city:<15} {'*' * rainfall}")
                
    except FileNotFoundError:
        print("Error: rainfall.txt not found.")
    except ValueError:
        print("Error: rainfall.txt contains incorrect data format.")
