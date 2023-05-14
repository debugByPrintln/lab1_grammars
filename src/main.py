first = {
   'S': {'b'},
   'A': {'b'},
   'A____': {'b', 'c', 'ε'},
   'A_': {'b', 'c'},
   'A__': {'b', 'c', 'ε'},
   'A___': {'b', 'c', 'ε'},
   'C': {'b', 'c'},
   'C_': {'a', 'b'},
   'B': {'b'}
}

follow = {
   'S': {'$'},
   'A': {'b', 'c'},
   'A____': {'b', 'c'},
   'A_': {'b', 'c'},
   'A__': {'b', 'c'},
   'A___': {'b', 'c'},
   'C': {'b', 'c'},
   'C_': {'b', 'c'},
   'B': {'$', 'b', 'c'}
}

def S():
    pass

def A():
    pass

def A____():
    pass

def A_():
    pass

def A__():
    pass

def A___():
    pass

def C():
    pass

def C_():
    pass

def B():
    pass

def end():
    print("Слово не подходит под грамматику вида:\nS → ACB\nA → bA’’’’\nA’’’’ → A’ | Ɛ\nA’ → CbA’’\nA’’ → A’ | bA’’’ | Ɛ\nA’’’ → A’ | Ɛ\nC → bbC’  |  c\nC’ → aA | B\nB → bb")
    raise Exception()

def getchar():
    global pointer
    global str1
    c = str1[pointer]
    pointer += 1
    return c

def start(st):
    global pointer
    pointer = 0
    global str1
    str1 = st
    S()
    print("Слово подходит под грамматику вида:\nS → ACB\nA → bA’’’’\nA’’’’ → A’ | Ɛ\nA’ → CbA’’\nA’’ → A’ | bA’’’ | Ɛ\nA’’’ → A’ | Ɛ\nC → bbC’  |  c\nC’ → aA | B\nB → bb")
