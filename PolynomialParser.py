import re

from Monomial import Monomial

def to_int(x):
    try:
        return int(x);
    except ValueError:
        ret = float(x);
        return (int(float(x)));

def is_integer(s):
    try:
        int(s);
        return True;
    except ValueError:
        try:
            ret = float(s);
            if (ret - int(ret) == 0):
                return True;
            else:
                return False;
        except ValueError:
		    return False;

def is_number(s):
    try:
        float(s);
        return True;
    except ValueError:
        return False;

class PolynomialParser:
    def __init__(self, polynomial, string):
        self.polynomial = polynomial;
        self.string = string;
        self.first = True;
        self.init_current();

    def init_current(self):
            self.sign = 1;  # + == 1 or - == -1
            self.factor = 1;
            self.power = 0;
            self.parsed_sign = False; #parsed the sign
            self.await_mul = False; #await a multiplication sign (*)
            self.await_X = False; # await X
            self.await_power = False; # await a ^
            self.await_power_value = False; # await an integer as as power
            self.parsed_factor = False; # parsed the factor as a value

    def parse(self):
        split = re.split('(?!\.)(\W+)', self.string)
        split = [x.strip(' ') for x in split]
        split = filter(None, split)
        self.init_current();
        for index, symbol in enumerate(split):
            if (is_number(symbol)):
                if (self.parsed_factor == True and self.await_power_value == False):
                    raise Exception("polynomial syntax error around:",  symbol);
                elif (self.parsed_factor == False):
                    if (not self.parsed_sign and not self.first):
                        raise Exception("polynomial syntax error around:",  symbol);
                    self.factor = float(symbol);
                    self.parsed_factor = True;
                    self.parsed_sign = True;
                    self.await_mult = True;
                elif (self.await_power_value == True):
                    if (is_integer(symbol)):
                        if (to_int(symbol) < 0):
                            raise Exception("please only give positive polynomial power: ", symbol);
                        else:
                            self.power = to_int(symbol);
                            self.flush();
                    else:
                        raise Exception("please only give integer polynomial power: ", symbol);
            elif (symbol == "*"):
                if (self.parsed_factor == False or
                        self.await_power == True or self.await_power_value == True
                             or self.await_mult == False):
                    raise Exception("polynomial syntax error around:",  symbol);
                self.await_X = True;
            elif symbol == "X":
                if (not self.await_X and self.parsed_factor):
                    raise Exception("polynomial syntax error around:",  symbol);
                if (not self.parsed_sign and not self.first):
                    raise Exception("polynomial syntax error around:",  symbol);
                self.power = 1;
                self.await_power = True;
                self.parsed_factor = True;
                self.await_X = False;
            elif symbol == "^":
                if (not self.await_power):
                    raise Exception("polynomial syntax error around:",  symbol);
                self.await_power_value = True;
                self.await_power_power = False;
            elif (symbol == "-" or symbol == "+"):
                if (self.parsed_factor):
                    self.flush();
                if (symbol == "-"):
                    self.sign *= -1;
                self.parsed_sign = True;
            else:
                raise Exception("polynomial lexical error: ", symbol);
            self.first = False;
        if (self.parsed_factor and not self.await_power_value and not self.await_X):
            self.flush();
        elif (self.parsed_sign or self.await_power_value or self.await_X):
            raise Exception("polynomial syntax error on last token", " (" + split[index] + ")");

    def flush(self):
        self.polynomial.monomials.append(Monomial(self.factor * self.sign, self.power));
        self.init_current();

    def __repr__(self):
        return "ouai";
