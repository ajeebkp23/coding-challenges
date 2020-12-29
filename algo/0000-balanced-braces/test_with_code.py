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
    brackets = [
        ('{','}'),
        ('(',')'),
        ('[',']'),
    ]
    for bracket1, bracket2 in brackets:
        if data.count(bracket1) != data.count(bracket2):
            return False
    return True

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

    for inp, outp in inputs_ouputs:
        print('Input and Output are: ',inp,outp)
        assert solve(inp) == outp