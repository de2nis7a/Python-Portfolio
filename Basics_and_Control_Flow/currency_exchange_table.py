# FILE: currency_exchange_table.py
# CONCEPT: Control Flow and Output Formatting
# DEMONSTRATES: Using a 'for' loop to generate a table of values and using advanced f-string formatting 
#               to align columns (`<` for left-align, `.2f` for precision).

def exchange_table():
    # Assuming exchange rate of 1 Euro = 1.17 USD
    exchange_rate = 1.17
    print("EUR | USD")
    print("--- | ---")
    for i in range(21):
        usd_value = i * exchange_rate
        # f"{i:<2}" left-aligns the integer, "{:.2f}" ensures two decimal places for the float
        print(f"{i:<2} {usd_value:>.2f}" )
