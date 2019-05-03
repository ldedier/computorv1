# coding: utf-8
import sys

from Polynomial import Polynomial

class Equation:
	def __init__(self, string):
		self.string = string;
		split = string.rstrip().split("=");
		if (len(split) != 2):
			raise Exception("the equation must have one left hand side and one right hand side");
		else:
			self.lhs = Polynomial(split[0]);
			self.rhs = Polynomial(split[1]);

	def isolate(self):
		
		print self;

		self.lhs.sub(self.rhs);
		self.rhs.monomials = [];

		print self;

		self.lhs.reduce();
#		self.lhs.sort();
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

	def resolveEquation(self):
		self.equation.isolate();
		if (self.equation.power > 2):
			raise Exception("\nThis equation is not solvable because its power is equal to ", str(self.equation.power));
		self.populateEquationValues();
		print ("\nthis equation\'s degree is %d" % self.equation.power);
		if (self.equation.power == 2):
			self.delta = (self.b * self.b) - (4 * self.a * self.c);
			print ("\ndelta: 𝚫 = %d\n" % self.delta);
			if (self.delta > 0):
				print ("𝚫 is strictly positive, so it has 2 real solutions");
				self.solutions.append(str((- self.b - self.delta ** 0.5) / (2 * self.a)));
				self.solutions.append(str((- self.b + self.delta ** 0.5) / (2 * self.a)));
			elif (self.delta < 0):
				print ("𝚫 is strictly negative, so it has 2 conjugated complex solutions");
				self.solutions.append(str((- self.b / (2 * self.a))) + " + i * " + str(abs((((-self.delta) ** 0.5) / (2 * self.a)))));
				self.solutions.append(str((- self.b / (2 * self.a))) + " - i * " + str(abs((((-self.delta) ** 0.5) / (2 * self.a)))));
			elif (self.delta == 0):
				print ("𝚫 is zero, so it has a single real solution:");
				self.solutions.append(str(-self.b / (2 * self.a)));
		elif self.equation.power == 1:
			self.solutions.append(str(-self.c / (self.b)));
		else: #self.equation.power = 0
			if (self.c == 0):
				print("the entirety of ℝ is solution of this equation !")
			else:
				print("this equation has no solutions !");
			return ;
		print ("\nthis equation's %d solution%s:\n\n%s" % (len(self.solutions), "s" if len(self.solutions)>1 else "" , "\n".join(self.solutions)));

if len(sys.argv) == 2:
	try:
		computor = Computor(sys.argv[1]);
		computor.resolveEquation();
	except Exception as exception:
		sys.exit("".join(exception.args));
else:
	sys.exit("usage: python %s \" *equation* \"" % sys.argv[0]);
