import sys

from Polynomial import Polynomial

class Equation:
	def __init__(self, string):
		self.string = string;
		split = string.rstrip().split("=");
		if (len(split) != 2):
			raise Exception("the equation must have a left hand side and a right hand side");
		else:
			self.lhs = Polynomial(split[0]);
			self.rhs = Polynomial(split[1]);

	def isolate(self):
		
		print self;

		self.lhs.sub(self.rhs);
		self.rhs.monomials = [];
		
		print self;
		
#		self.lhs.sort();

		print self;
		
		self.lhs.reduce();
		self.power = self.lhs.power();
		print self;

	def __repr__(self):
		return repr(self.lhs) + " = " + repr(self.rhs);

class Computor:
	def __init__(self, string):	
			self.equation = Equation(string);
			self.solutions = [];
	
	def populateEquationValues(self):
		self.a = 0;
		self.b = 0;
		self.c = 0;
		for monomial in self.equation.lhs.monomials:
			if (monomial.power == 0):
				self.c = monomial.factor;
			elif (monomial.power == 1):
				self.b = monomial.factor;
			elif (monomial.power == 2):
				self.a = monomial.factor;
		self.delta = (self.b * self.b) - (4 * self.a * self.c);

	def resolveEquation(self):
		self.equation.isolate();
		if (self.equation.power > 2):
			raise Exception("This equation is not solvable: power = ", str(self.equation.power));
		self.populateEquationValues();
		if (self.delta > 0):
			self.solutions.append((-self.b - sqrt(self.delta)) / (2 * self.a));
			self.solutions.append((-self.b + sqrt(self.delta)) / (2 * self.a));
		elif (self.delta == 0):
			self.solutions.append(-self.b / (2 * self.a));

if len(sys.argv) == 2:
	try:
		computor = Computor(sys.argv[1]);
		computor.resolveEquation();
	except Exception as exception:
		sys.exit("".join(exception.args));
else:
	sys.exit("usage: python %s \" *equation* \"" % sys.argv[0]);
