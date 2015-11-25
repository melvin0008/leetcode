#!/bin/python
import sys

n = map(int,raw_input().strip().split(' '))
data = sys.stdin.readlines()

# for line in data :
#    print(line.split(''))

class Vertex(object):
	def __init__(self,key):
		self.key=key
		self.connected_nodes={}

	def __str__(self):
		return str(self.key) + ' adjacent: ' + str([x for x in self.connected_nodes])

	def getConnections(self):
		return self.connected_nodes.keys()

	def addNeighbour(self,neighbour,weight):
		self.connected_nodes[neighbour]=weight

	def getWeight(self,vertex2):
		return self.connected_nodes[vertex2]


class Graph(object):
	def __init__(self):
		self.vertices_list={}
		self.numVertices=0

	def __iter__(self):
		return iter(self.vertices_list.values())

	def addVertex(self,key):
		self.vertices_list[key]=Vertex(key)
		self.numVertices+=1

	def addVertices(self,vertices):
		for vertex in vertices:
			self.addVertex(vertex)

	def getVertex(self,vertex):
		if vertex in self.vertices_list:
			return self.vertices_list[vertex]
		else:
			return None

	def numberVertices(self):
		return self.numVertices

	def hasVertex(self,vertex):
		return vertex in self.vertices_list

	def getVertices(self):
		return self.vertices_list.keys()

	def addEdge(self,vertex1,vertex2,weight=0):
		if vertex1 not in self.vertices_list:
			self.addVertex(vertex1)
		if vertex2 not in self.vertices_list:
			self.addVertex(vertex2)
		self.vertices_list[vertex1].addNeighbour(vertex2,weight)

	def addEdges(self,edgesList):
		for edge in edgesList:
			try:
				self.addEdge(edge[0],edge[1],edge[2])
			except IndexError:
				self.addEdge(edge[0],edge[1],0)

	def getEdges(self):
		edgeList=[]
		for vertex1,vertex2 in self.vertices_list.items():
			print vertex1, vertex2.getConnections()

	def getNeighbours(self,vertex):
		if vertex in self.vertices_list:
			return self.vertices_list[vertex].getConnections()
		else:
			raise Exception("Vertex doesnt exist")




g=Graph()
# n = map(int,raw_input().strip().split(' '))
flag=0

linecol=0
a=[]
for line in data:
	a.append(map(int,line.strip().split(' ')))

for x in xrange(n[1]+n[1]+1):
	if(not flag):
		for y in xrange(n[0]):
			g.addEdge(str(linecol),str(linecol+1),a[x][y])
			linecol+=1
		flag=1
	else:
		for y in xrange(n[0]+1):
			g.addEdge(str(linecol-n[0]),str(linecol+1),a[x][y])
			linecol+=1
		linecol=linecol-n[0]
		flag=0


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}
  nodes = set(graph.getVertices())
  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] > visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.getNeighbours(min_node):
      weight = current_weight + graph.getVertex(min_node).getWeight(edge)
      if edge not in visited or weight > visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return max(visited.iteritems(), key=lambda x:x[1])[1]

print dijsktra(g,"0")

