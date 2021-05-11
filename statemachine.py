class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, q_state, handler, end_state=0):
        q_state = q_state.upper()
        self.handlers[q_state] = handler
        if end_state == 1:
            self.endStates.append(q_state)

    def set_start(self, q_state):
        self.startState = q_state.upper()

    def run(self, input): #, Iter):
        global handler
        try:
            #handler = self.handlers[self.start_transitions]
            handler = self.handlers[self.startState]
            print('---------- run {} ----------'.format(input))
        except:
            print("call set_start() before run()")
        if not self.endStates:
            print("one state must be an end_state")
        self.current_state = self.startState
        index = 0
        while index < len(input):
            keyEntry = input[index]
            #(newState, x) = handler(keyEntry)
            newState, x = handler(keyEntry)
            index += 1
			#if fsm has entered end state
            if newState.upper() in self.endStates:
                print("entered end state")
                break
            else:
                self.current_state = newState.upper()
                if newState.upper() in self.handlers.keys():
                    handler = self.handlers[newState.upper()]
                else:
                    break
        print("-------------------------------")
