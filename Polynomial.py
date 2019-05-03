import sys
import re

from PolynomialParser import PolynomialParser

class Polynomial:
	def __init__(self, string):
		self.monomials = [];
		parser = PolynomialParser(self, string);
		parser.parse();
	
	def power(self):
		res = 0;
		for monomial in self.monomials:
			if monomial.factor != 0 and monomial.power > res:
				res = monomial.power;
		return res;
		
	def reduce(self):
		i = 0;
		while (i < len(self.monomials)):
			ref = self.monomials[i];
			j = i + 1;
			while (j < len(self.monomials)):
				compare = self.monomials[j];
				if (ref.power == compare.power):
					ref.add(compare);
					self.monomials.remove(compare);
				else:
					j = j + 1;
			i = i + 1;

		

	def scalar(self, other, scalar): #p1 = p1 + scalar * p2
		for monomial in other.monomials:
			self.monomials.append(monomial.scalaredClone(scalar));

	def sub(self, other):
		self.scalar(other, -1);
	
	def add(self, other):
		self.scalar(other, 1);

	def isNull(self):
		for monomial in self.monomials:
			if (monomial.factor != 0):
				return False;
		return True;

	def __repr__(self):
		if (len(self.monomials) == 0 or self.isNull()):
			return "0";
		res = "";
		printed = False;
		for monomial in self.monomials:
			if (printed == False and monomial.factor != 0):
				res += repr(monomial);
				printed = True;
			else:
				if (monomial.factor > 0):
					res += " + " + repr(monomial);
				elif (monomial.factor < 0):
					res += " " + repr(monomial);
		return (res);
