# FILE: procedural_streaming_account.py
# CONCEPT: Procedural State Management using Global Variables
# DEMONSTRATES: Managing application state (account details) using functions and the 'global' keyword 
# instead of an Object-Oriented approach (classes).

# Global Variables define the application's state
account_name = "Guest"
membership_type = "Basic"
stream_limit = 2
movies_streamed = 0 # Added to make state management complete

def view_details():
    """Displays current account details."""
    print(f"Account Name: {account_name}")
    print(f"Membership Type: {membership_type}")
    print(f"Stream Limit: {stream_limit}")
    print(f"Movies Streamed: {movies_streamed}")


def upgrade_membership(name):
    """Upgrades the membership and updates global state variables."""
    global account_name, membership_type, stream_limit
    
    account_name = name
    if membership_type == "Basic":
        membership_type = "Premium"
        stream_limit = 5
        print(f"Membership upgraded to {membership_type}.")
    else:
        print("You already have Premium membership.")

def stream_movie():
    """Increments movies streamed if below stream limit."""
    global movies_streamed, stream_limit
    if movies_streamed < stream_limit:
        movies_streamed += 1
        print("Movie streamed successfully.")
    else:
        print("You have reached your streaming limit.")

def main_test():
    global movies_streamed # Needed to reset state for a clean test run
    
    # Reset for test
    movies_streamed = 0 
    
    view_details()
    upgrade_membership("Alice")
    view_details()
    
    print("\n" + "="*30 + "\n")
    print("Testing streaming:")
    stream_movie()
    stream_movie()
    stream_movie()
    view_details()

if __name__ == "__main__":
    main_test()
