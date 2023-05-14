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
    A()
    B()
    C()
    c = getchar()
    if c != '$':
        end()

def A():
    c = getchar()
    if c == 'b':
        A____()
    else:
        end()

def A____():
    c = getchar()
    if c in first['A_']:
        A_()
    elif c is None:
        return
    else:
        end()

def A_():
    C()
    c = getchar()
    if c == 'b':
        A__()
    else:
        end()

def A__():
    c = getchar()
    if c in follow['A_']:
        return
    elif c == 'b':
        A___()
    elif c is None:
        return
    else:
        end()


def A___():
    c = getchar()
    if c in first['A_']:
        A_()
    elif c is None:
        return
    else:
        end()

def C():
    c = getchar()
    if c == 'b':
        c = getchar()
        if c == 'b':
            C_()
        else:
            return
    else:
        end()

def C_():
    c = getchar()
    if c in follow['B']:
        return
    elif c == 'a':
        A()
    else:
        end()


def B():
    c = getchar()
    if c == 'b':
        c = getchar()
        if c != 'b':
            end()
    else:
        end()

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

start("bcbb")
