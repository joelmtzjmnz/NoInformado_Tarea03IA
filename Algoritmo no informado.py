import time

class Vertice:
    def __init__(self, v, p):
        self.valor = v
        self.peso = p
        self.visitado = False
        self.padre = None
        self.vecinos = []

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)


class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, val, pes):
        if val not in self.vertices:
            self.vertices[val] = Vertice(val, pes)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)
            
    def dfs(self, r, PL, PA, camino):
        if r in self.vertices:
            PA += self.vertices[r].peso
            if PA >= PL:
                return 0
            self.vertices[r].visitado = True
            #print("\nR= "+str(r))
            for nodo in self.vertices[r].vecinos:
                #print("\nnodo= "+str(nodo))
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = r
                    camino.append(self.vertices[nodo].valor) 
                    print("("+str(nodo)+", "+str(r)+", p="+str(PA)+")")
                    self.dfs(nodo, PL, PA, camino)
                    

    
            
def main():
    inicio = time.time()
    print("Numero de nodos: ")
    NumNodos = float(input())
    print("Peso límite: ")
    pesoLimite = float(input())

    g = Grafica()
    for k in range(0,int(NumNodos)):
        print("Valor["+str(k+1)+"]: ")
        VN = input()
        VN = float(VN)
        print("Peso["+str(k+1)+"]: ")
        PN = input()
        PN = float(PN)
        g.agregarVertice(VN,PN)
        if k == 0:
            NodoInicial=VN
    
    aux =0 
    for X in g.vertices:
        if aux == 0:
            A= g.vertices[X].valor
            aux=1
        else:
            B= g.vertices[X].valor
            g.agregarArista(A,B)
            A = B
        

    print("("+str(NodoInicial)+", NULL, P=0)")
    pesoAcumulado = 0.0
    camino = [NodoInicial]
    g.dfs(NodoInicial, pesoLimite, float(pesoAcumulado), camino)
    print("\nCamino: "+str(camino))


    fin = time.time()
    print("\n\nTiempo de ejecución: "+ str(fin-inicio)+ " s")

main()