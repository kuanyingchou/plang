# FSM Simulation
# r"a+1+"

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # QUIZ: You fill this out!
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        # Hint: recursion.
        print letter
        if (current, letter) in edges:
            current=edges[(current, letter)]
            return fsmsim(string[1:], current, edges, accepting)
        else:
            return False #fall off




print fsmsim("aaa111",1,edges,accepting)
# >>> True

print fsmsim("1",1,edges,accepting)
print fsmsim("a",1,edges,accepting)
print fsmsim("a1",1,edges,accepting)
