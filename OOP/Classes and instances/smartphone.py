class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app_name, memory):
        if self.memory - memory <= 0:
            return f"Not enough memory to install {app_name}"

        if not self.is_on:
            return f"Turn on your phone to install {app_name}"

        else:
            self.apps.append(app_name)
            self.memory -= memory
            return f"Installing {app_name}"

    def status(self):
         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"