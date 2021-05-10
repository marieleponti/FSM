class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state == 1:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo, Iter):
        global handler
        try:
            handler = self.handlers[self.startState]
        except:
            print("call set_start() before run()")
        if not self.endStates:
            print("one state must be an end_state")
        self.currState = self.startState
        index = 0
        while True:
            cargo_sub = cargo[index + 1]
            index = index + 2
            (newState, x) = handler(cargo_sub)
            if newState.upper() in self.endStates:
                print("end_state reached", newState)
                print("Test case complete.")
                break
            else:
                self.currState = newState.upper()
                if newState.upper() in self.handlers.keys():
                    handler = self.handlers[newState.upper()]
                else:
                    print("Test case complete.")
                    break
