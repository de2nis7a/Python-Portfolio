# FILE: streaming_service_account.py
# CONCEPT: Object-Oriented Programming (OOP) - State Management
# DEMONSTRATES: Class initialization (__init__), managing internal state (movies_streamed), 
#               methods for state change (upgrade_membership), and conditional logic.

class StreamingAccount:
    def __init__(self):
        self.account_name = "Guest"
        self.membership_type = "Basic"
        self.stream_limit = 2
        self.movies_streamed = 0  # Initialize movies streamed

    def view_details(self):
        print(f"Account Name: {self.account_name}")
        print(f"Membership Type: {self.membership_type}")
        print(f"Stream Limit: {self.stream_limit}")
        print(f"Movies Streamed: {self.movies_streamed}")

    def upgrade_membership(self, name):
        self.account_name = name
        if self.membership_type == "Basic":
            self.membership_type = "Premium"
            self.stream_limit = 5
        else:
            print("You already have Premium membership.")

    def stream_movie(self):
        if self.movies_streamed < self.stream_limit:
            self.movies_streamed += 1
            print("Movie streamed successfully.")
        else:
            print("You have reached your streaming limit.")


def main():
    account = StreamingAccount()
    account.view_details()
    account.upgrade_membership("Alice")
    account.view_details()
    print("\n" + "="*30 + "\n")

    # Demonstrate streaming functionality
    for _ in range(3):
        account.stream_movie()
    account.view_details()

if __name__ == "__main__":
    main()
