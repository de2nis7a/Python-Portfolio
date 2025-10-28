# FILE: discord_chat_simulation.py
# CONCEPT: Object-Oriented Programming (OOP) - Inheritance and Messaging Logic
# DEMONSTRATES: Inheritance for user tiers (NitroUser), complex method logic (pinning_messages), 
#               and composition (Message class holding a User instance).

class User:
    
    types = ["unverified", "verified", "nitro"]
    
    def __init__(self, user_id, user_type):
        self._id = user_id
        if user_type in self.types:
            self._type = user_type
        else:
            self._type = "unverified"
        
        self.messages_received = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7']
        
    @property
    def user_type(self):
        return self._type
    
    @user_type.setter
    def type(self, user_type):
        if user_type in self.types:
            self._type = user_type
    
    @property
    def user_id(self):
        return self._id
    
    def __str__(self):
        desc = ""
        if self._type == "unverified":
            desc = "can't send messages, the message limit does not apply and can't pin messages"
        elif self._type == "verified":
            desc = "can send messages, the message limit is max 100 characters and can't pin messages"
        elif self._type == "nitro":
            desc = "can send messages, the message limit is unlimited and can pin messages"
            
        return (f"The user {self._id} have an {self._type} account in which {desc}")
    
    def see_received_mess(self):
        output = f"Received messages for {self._id}:"
        for message in self.messages_received:
            output += f"\n - {message} "
        return output

class NitroUser(User):
    
    def __init__(self, user_id, user_type):
        # Force user_type to 'nitro' if initialized as NitroUser class
        super().__init__(user_id, 'nitro') 
    
    def pinning_messages(self, message_index_1_based):
        index = message_index_1_based - 1 # Convert to 0-based
        if 0 <= index < len(self.messages_received):
            message_for_pin = self.messages_received.pop(index)
            self.messages_received.insert(0, message_for_pin)
            print(f"Message {message_index_1_based} pinned successfully.")
        else:
            print("Invalid message index.")
    
class Message:
    
    def __init__(self, user):
        self.user = user
        
    def view_message(self, message):
        if message in self.user.messages_received:
            return f"\n Message {message} for {self.user._id}: 'Wanted to say hi!' \n"
        
    def receive_message(self, new_message_text="mX"):
        # Simulates receiving a new message
        self.user.messages_received.append(new_message_text)
        
    def send_message(self, text, to_user_id):
        # Check permission based on user type
        if self.user._type == "verified" or self.user._type == "nitro":
            self.text = text
            self.send_to = to_user_id
            return (f"\n The message: '{self.text}' is sending from {self.user._id} to {self.send_to}")
        else:
            return "Not allowed. User must be verified or nitro to send messages."
        
def test_discord():
    user1 = User("u1_Alice", "verified")
    user2 = NitroUser("u2_Bob", "nitro")
    print(user1)
    
    print("\n--- NITRO USER PINNING ---")
    print(user2.see_received_mess())
    user2.pinning_messages(3) # Pin message m3
    print(user2.see_received_mess())
    user2.pinning_messages(7) # Pin message m7 (now at index 6)
    print(user2.see_received_mess())
    
    print("\n--- MESSAGE CLASS TEST ---")
    m_sender = Message(user2) # Nitro user is the sender
    print(m_sender.send_message("Hello from Nitro", "u1_Alice"))
    
    m_unverified = Message(User("u3_Guest", "unverified"))
    print(m_unverified.send_message("Trying to send...", "u1_Alice"))
    
if __name__ == "__main__":
    test_discord()
