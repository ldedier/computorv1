#class Monomial:
#	def __init__(self, factor, power):
#		self.factor = factor;
#		self.power = power;
#
#	def __repr__(self):
#		return ("" if self.factor >= 0 else "- ") + str(abs(self.factor)) +\
#		" * X^" + str(self.power);

def ft_abs(a):
	if a < 0:
		return (-a);
	return (a);

class Monomial:
	def __init__(self, factor, power):
		self.factor = factor;
		self.power = power;

	def scalaredClone(self, scalar):
		return Monomial(self.factor * scalar, self.power);

	def add(self, other):
		if (self.power == other.power):
			self.factor += other.factor;

	def equals(self, other):
		#print "call to equals for ", self, "AND", other
		return (self.factor == other.factor and self.power == other.power);
	
	def __repr__(self):
		res = "";
		if (self.factor < 0):
			res += "- ";
		if (ft_abs(self.factor) == 1 and self.power != 0):
			res += "";
		elif (self.factor == int(self.factor)):
			res += str(ft_abs(int(self.factor)));
		else:
			res += str(ft_abs(self.factor));
		if (self.power == 0):
			return (res + "");
		else:
			if (ft_abs(self.factor) != 1):
				res += " * ";
			if (self.power == 1):
				res += "X";
			else:
				res += "X^" + str(self.power);
			return (res+ "");
