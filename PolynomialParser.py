import re

from Monomial import Monomial

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
		self.init_current();

	def init_current(self):
		self.sign = 1;
		self.factor = 1 ;
		self.power = 0;
		self.await_power = False;
		self.parsed_factor = False;

	def parse(self):
		split = self.string.rstrip().split(" ");
		split = filter(None, split)
		self.init_current();
		for index, symbol in enumerate(split):
			m = re.search("^X\^([0-9]+)$", symbol);
			if (is_number(symbol)):
				if (self.parsed_factor == True or self.await_power == True):
					raise Exception("polynomial syntax error around:",  symbol);
				self.factor = float(symbol);
				self.parsed_factor = True;
			elif (symbol == "*"):
				if (self.parsed_factor == False or self.await_power == True):
					raise Exception("polynomial syntax error around:",  symbol);
				self.await_power = True;
			elif m or symbol == "X":
				if (symbol == "X"):
					self.power = 1;
				else:
					self.power = int(m.group(1));
				self.flush();
			elif (symbol == "-" or symbol == "+"):
				if (self.parsed_factor):
					self.flush();
				if (symbol == "-"):
					self.sign *= -1;
			elif (re.match("^X\^-[0-9]+$", symbol)):
				raise Exception("please only give positive polynomial power: ", symbol);
			else:
				raise Exception("polynomial lexical error: ", symbol);
		if (self.parsed_factor):
			self.flush();

	def flush(self):
		self.polynomial.monomials.append(Monomial(self.factor * self.sign, self.power));
		self.init_current();

	def __repr__(self):
		return "ouai";
