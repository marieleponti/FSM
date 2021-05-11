import time
import random
from statemachine import StateMachine

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def q0_transitions(input):
    print("start")
    print("current state: q0\tinput: {}".format(input))
    if input == "1":
        newState = "q1"
    elif input == "#":
        newState = "q0"
    elif input in alphabet:
        newState = "q7"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q1_transitions(input):
    print("current state: q1\tinput: {}".format(input))
    if input == "4":
        newState = "q2"
    elif input == "#":
        newState = "q0"
    elif input in alphabet:       
        newState = "q8"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q2_transitions(input):
    print("current state: q2\tinput: {}".format(input))
    if input == "7":
        newState = "q3"
    elif input == "#":
        newState = "q0"
    elif input in alphabet: 
        newState = "q9"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q3_transitions(input):
    print("current state: q3\tinput: {}".format(input))
    if input == "2":
        newState = "q4"
    elif input == "#":
        newState = "q0"
    elif input in alphabet:  
        newState = "q10"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q4_transitions(input):
    print("current state: q4\tinput: {}".format(input))
    if input == "5":
        newState = "q5"
    elif input == "#":
        newState = "q0"
    elif input in alphabet:   
        newState = "q11"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q5_transitions(input):
    print("current state: q5\tinput: {}".format(input))
    if input == "8":
        print("UNLOCKED")
        time.sleep(2)
        newState = "q12"
    elif input == "#":
        newState = "q0"
    elif input in alphabet:  
        print("INCORRECT COMBINATION.")
        newState = "q0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

# def q6_transitions():
#     print("current state: q6")
#     print("UNLOCKED")
#     time.sleep(2)
#     newState = "q12"
#     return newState, '#'

def q7_transitions(input):
    print("current state: q7\tinput: {}".format(input))
    if input in alphabet: 
        newState = "q8"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q8_transitions(input):
    print("current state: q8\tinput: {}".format(input))
    if input in alphabet: 
        newState = "q9"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q9_transitions(input):
    print("current state: q9\tinput: {}".format(input))
    if input in alphabet: 
        newState = "q10"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q10_transitions(input):
    print("current state: q10\tinput: {}".format(input))
    if input in alphabet: 
        newState = "q11"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q11_transitions(input):
    print("current state: q11\tinput: {}".format(input))
    if input in alphabet: 
        print("INCORRECT COMBINATION.")
        newState = "q0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def q12_transitions(input):
    print("current state: final state\tinput: {}".format(input))
    

if __name__ == "__main__":
    m = StateMachine()
    m.add_state("q0", q0_transitions)
    m.add_state("q1", q1_transitions)
    m.add_state("q2", q2_transitions)
    m.add_state("q3", q3_transitions)
    m.add_state("q4", q4_transitions)
    m.add_state("q5", q5_transitions)
    #m.add_state("q6", q6_transitions) #, end_state=1)
    m.add_state("q7", q7_transitions)
    m.add_state("q8", q8_transitions)
    m.add_state("q9", q9_transitions)
    m.add_state("q10", q10_transitions)
    m.add_state("q11", q11_transitions)
    m.add_state("q12", q12_transitions, end_state = 1)
    m.set_start("q0")

    #Test case 1
    m.run("010010") 
    m.run("147259") # no
    m.run("147259174258")

  	#Test case 2
    m.run("147258")

    #Random test case
    randTest = ""
    for i in range(random.choice([10])):
        randTest += str(random.choice([0, 1]))
    m.run(randTest, "random")

    