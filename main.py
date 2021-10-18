from classe import Escritor
from classe import Caneta
from classe import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
#print(escritor.nome)
caneta = Caneta('Bic')
#print(caneta.marca)
maquina = MaquinaDeEscrever()
#print(maquina)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
