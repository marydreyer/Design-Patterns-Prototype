
from Syrax import Syrax
from Vhagar import Vhagar
from Balerion import Balerion
import datetime

print('Iniciando criação de um dragão padrão Balerion: ', datetime.datetime.now().time())
balerion = Balerion (70, "Preto", 8000, "Macho", "50000 ºC ")
print('Finalizando Balerion: ', datetime.datetime.now().time())
print('Caracteristicas:\n' + '\n'.join("%s: %s" % item for item in vars(balerion).items()))

print('Instanciando cópias em: ', datetime.datetime.now().time())
for i in range(1,5):
    balerion = Balerion (70, "Preto", 8000, "Macho", "50000 ºC ")
    print(f'Finalizado Balerion {i} em: ', datetime.datetime.now().time(),f'\nBalerion {i}:\n', balerion.getInformacoes())
print('Finalizado instanciamento de cópias em:', datetime.datetime.now().time())

print('-------------------------------------------------------------')

print('Instanciando clone de dragão padrão Balerion: ', datetime.datetime.now().time())
balerion_template = Balerion(70, "Preto", 8000, "Macho", "50000 ºC ")
for i in range(1,5):
    balerion_clone = balerion_template.clone()
    print(f'Finalizando clone Balerion {i} at: ', balerion_clone.getInformacoes(), datetime.datetime.now().time())
print('Finalizado instanciamento dos clones em: ', datetime.datetime.now().time())

print('-------------------------------------------------------------')

print('Instanciando 9 Cópias - Femêa: ', datetime.datetime.now().time())
balerion_template = Balerion(70, "Preto", 8000, "Femêa", "50000 ºC ")
vhagar_template = Vhagar(50, "Vermelho", 5000, "Femêa", "5000 hs")
syrax_template = Syrax(15, "Amarelo", 5000, "Femêa", "Extremamente Agil")
for i in range(1,3):
    balerion_clone = balerion_template.clone()
    vhagar_clone = vhagar_template.clone()
    syrax_clone = syrax_template.clone()
    print(f'Finalizada criação de um trio de dragões clone {i} em: ', datetime.datetime.now().time(),f'\nBelarion {i}:\n', balerion_template.getInformacoes(),f'\nVhagar {i}:\n', vhagar_template.getInformacoes(),f'\nSyrax {i}:\n', syrax_template.getInformacoes(),'\n')
print('Finalizada instanciamento da população em: ', datetime.datetime.now().time())

print('-------------------------------------------------------------')

print('Instanciando 9 Cópias - Macho: ', datetime.datetime.now().time())
balerion_template = Balerion(70, "Preto", 8000, "Macho", "50000 ºC ")
vhagar_template = Vhagar(50, "Vermelho", 5000, "Macho", "5000 hs")
syrax_template = Syrax(15, "Amarelo", 5000, "Macho", "Extremamente Agil")
for i in range(1,3):
    balerion_clone = balerion_template.clone()
    vhagar_clone = vhagar_template.clone()
    syrax_clone = syrax_template.clone()
    print(f'Finalizada criação de um trio de dragões clone {i} em: ', datetime.datetime.now().time(),f'\nBelarion {i}:\n', balerion_template.getInformacoes(),f'\nVhagar {i}:\n', vhagar_template.getInformacoes(),f'\nSyrax {i}:\n', syrax_template.getInformacoes(),'\n')
print('Finalizada instanciamento da população em: ', datetime.datetime.now().time())