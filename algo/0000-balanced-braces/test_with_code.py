# Balanced braces

# Given a string, return true or false

# "{}" => true
# "{()[{}[]]}" => true
# "{(})" => false
# "{()[}[]]}" => false
# "if(a==b) x = y;" => true
# "if(a==b x = y;" => false
# "if(x<10}(b++;}else{b+=10;}" => false


def solve(data):
    open_brackets = ['{','(','[']
    close_brackets = ['}',')',']']
    brackets = dict(zip(open_brackets,close_brackets))
    is_balanced = True
    bracket_in_data = []
    for i in data:
        print(i)
        if i in open_brackets:
            bracket_in_data.append(i)
        elif i in close_brackets:
            if brackets[bracket_in_data[-1]] == i:
                bracket_in_data.pop(-1)
            else:
                is_balanced = False
                break
        else:
            pass
    if len(bracket_in_data) != 0:
        is_balanced = False
    return is_balanced

def test_datas():
    inputs_ouputs = [
        ("""{}""" , True),
        ("{()[{}[]]}" , True),
        ("{(})" , False),
        ("{()[}[]]}" , False),
        ("if(a==b) x = y;" , True),
        ("if(a==b x = y;" , False),
        ("if(x<10}(b++;}else{b+=10;}" , False),
    ]
    print(inputs_ouputs)
    for inp, outp in inputs_ouputs:
        print('Input and Output are: ',inp,outp)
        assert solve(inp) == outp
        print('Input and Output are [Balanced]: ',inp,outp)