# FILE: smartphone_app_manager.py
# CONCEPT: Object-Oriented Programming (OOP) - List Manipulation and State Tracking
# DEMONSTRATES: Managing complex object state (list of apps), updating list elements based 
#               on index, and tracking previous state (ant_index).

class Smartphone:
    def __init__(self, colour, memory , apps):
        self.colour = colour
        self.memory = memory
        self.apps = apps
        self.ant_index = 0 # Index of the currently "active" app (initially "Phone")
    
    def installed_apps(self):
        text = "Installed apps: \n"
        for i in self.apps:
            text = text + f"- {i}" + '\n'
        return text
    
    def install_app(self, app):
        self.install = app
        self.apps.append(app)
        return f"Installing {self.install} app ..."
    
    def switching_app(self, app):
        index = self.apps.index(app)
        
        # 1. Deactivate previous app (remove "(current)")
        if self.ant_index < len(self.apps):
            word = self.apps[self.ant_index].split()
            self.apps[self.ant_index] = word[0]

        # 2. Activate new app
        self.apps[index] = f"{app} (current)"
        
        # 3. Update the tracked index
        self.ant_index = index
            
    
    def __str__(self):
        return f"A {self.colour} smartphone with {self.memory} GB of memory \n"
        
def test_smartphone():
    smartphone = Smartphone("black", 128, ["Phone (current)", "Messages" , "Camera"])
    print(smartphone)
    print(smartphone.installed_apps())
    print(smartphone.install_app("Spotify"))
    print(smartphone.installed_apps())
    smartphone.switching_app("Camera")
    print(smartphone.installed_apps())
    smartphone.switching_app("Messages")
    print(smartphone.installed_apps())

if __name__ == "__main__":
    test_smartphone()
