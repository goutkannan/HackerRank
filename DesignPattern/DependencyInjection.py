
in_sudo_mode = True

def always_authenticated(val):
    print("this is ",val)

def always_authorized(u,a):
    print(u,a)

def login():
    print("login.....")

class Command:

    def __init__(self, authenticate=None, authorize=None):
        self.authenticate = authenticate or self._not_authenticated
        self.authorize = authorize or self._not_autorized

    def execute(self, user, action):
        self.authenticate(user)
        self.authorize(user, action)
        return action()

if in_sudo_mode:
    command = Command(always_authenticated, always_authorized)
else:
    print("Not sudo")
    #command = Command(config.authenticate, config.authorize)
command.execute("Goutham",login)
