from Syrax import Syrax
from Vhagar import Vhagar
from Balerion import Balerion


Dragao1 = Syrax()
Dragao1.cadastrar(15, "Amarelo", 5000, "Femêa", "Extremamente Agil")
print('Syrax:\n', Dragao1.getInformacoes(),'\n')

Dragao2 = Vhagar()
Dragao2.cadastrar(50, "Preto", 5000, "Femêa", "5000 hs")
print('Vhagar:\n', Dragao2.getInformacoes(),'\n')

Dragao3 = Balerion()
Dragao3.cadastrar(70, "Preto", 8000, "Macho", "50000 ºC ")
print('Balerion:\n', Dragao3.getInformacoes(),'\n')