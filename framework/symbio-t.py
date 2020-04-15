#!/usr/bin/env python
# (C) 2015 The University of Chicago
#
# See COPYRIGHT in top-level directory.

from enum import Enum
	
class NetworkMicroservice:
	functions = ["network_do_work"]
	def __init__(self, num_providers):
		self.num_providers = num_providers
	
class MemoryMicroservice:
	functions = ["memory_do_work"]
	def __init__(self, num_providers):
		self.num_providers = num_providers

class ComputeMicroservice:
	functions = ["compute_do_work"]
	def __init__(self, num_providers):
		self.num_providers = num_providers

class StorageMicroservice:
	functions = ["storage_do_work"]
	def __init__(self, num_providers):
		self.num_providers = num_providers

class AccessPattern(Enum):
	Fixed = 1
	Dynamic = 2

class OperationTree:
	def __init__(self, microservice_function, first=None, second=None, third=None):
		self.microservice_function = microservice_function
		self.first = first
		self.second = second
		self.third = third

	def traverseTree(self, accessPattern=None, isFirstChild=True):
		requestStructure = ""
                if isFirstChild: 
			requestStructure += '{'
		else:
			requestStructure += ',{'
		
		requestStructure += '"val": ' + '"'+str(self.microservice_function) + '"'
		if accessPattern != None:
			requestStructure += ',' + '"accessPattern": ' + '"'+ str(accessPattern) + '"'

		if self.first != None or self.second != None or self.third != None:
			requestStructure += ',' + '"children": ['
			if self.first != None:
				requestStructure += self.first[0].traverseTree(self.first[1])
			if self.second != None:
				requestStructure += self.second[0].traverseTree(self.second[1], False)
			if self.third != None:
				requestStructure += self.third[0].traverseTree(self.third[1], False)
			requestStructure += ']'
		requestStructure += "}"
		return requestStructure
		


class OperationType:
	def __init__(self, name, tree):
		self.name = name
		self.opTree = tree

class Service:
	def __init__(self, name):
		self.microservices = list()
		self.name = name
		self.opTypes = set()
		self.legal_boilerplate = "/*\n  * (C) 2015 The University of Chicago\n  *\n  * See COPYRIGHT in top-level directory.\n*/\n"
	
	def addMicroservice(self, microservice):
		self.microservices.append(microservice)

	def addOperationType(self, op):
		self.opTypes.add(op)

	def generateClientHeader(self):
		filename = self.name + str("_client.h")
		f = open(filename, "w")
		f.write(self.legal_boilerplate)
		for op in self.opTypes:
			f.write("static char[] " + op.name + " = \"" + str(op.opTree.traverseTree()) + "\";")
		f.flush()
		f.close()
	


def main():
	a = OperationTree(NetworkMicroservice.functions[0])
	b = OperationTree(ComputeMicroservice.functions[0], (a, AccessPattern.Fixed), (a, AccessPattern.Dynamic))
	c = OperationTree(StorageMicroservice.functions[0], (b, AccessPattern.Dynamic))

	op1 = OperationType("op1", c)
	s = Service("dummy")
	s.addMicroservice(NetworkMicroservice(2))
	s.addMicroservice(ComputeMicroservice(1))
	s.addMicroservice(StorageMicroservice(1))
	s.addOperationType(op1)
	s.generateClientHeader()

main()

