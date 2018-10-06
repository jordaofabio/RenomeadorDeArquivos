import shutil
import os
import re
from unicodedata import normalize

def preparaCaminho(caminho):
    caminho = caminho.replace("\\", "//")
    if caminho[len(caminho)-1] != "/":
        caminho = caminho + "//"
    return caminho

_fonte = input('Informe a pasta de origem:')
_fonte = preparaCaminho(_fonte)

_destino = input('Informe a pasta de destino:')
_destino = preparaCaminho(_destino)

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def preparaNomeArquivo(a):
    _arquivo = a.replace(" ","-").replace(".","-").lower()
    i=0
    nomeArquivo = _arquivo[:-4]
    extensaoArquivo = "." + _arquivo[len(nomeArquivo)+1:]
    novoArquivo = remover_acentos(nomeArquivo + extensaoArquivo).strip()
    return novoArquivo

def gera_pastas(root):
    for pasta in os.listdir(root):
        novoRoot = root+pasta+'\\'
        novoDestino = remover_acentos(novoRoot.replace(_fonte, "")).lower()
        novoDestino = _destino+novoDestino.replace(" ","-")

        if os.path.isdir(novoRoot):
            print(novoRoot)
            if not os.path.exists(novoDestino):
                os.makedirs(novoDestino)
            copia_arquivos(novoRoot, novoDestino)
            gera_pastas(novoRoot)

def copia_arquivos(orig, dest):
    for _, _, arquivo in os.walk(orig):
        arquivo = arquivo
    i=0
    for a in range(0, len(arquivo)):
        a = str(arquivo[i])
        caminho = orig.strip()+a
        if os.path.isfile(caminho) and not os.path.exists(dest.strip()+preparaNomeArquivo(a)):
            shutil.copy(caminho, dest.strip()+preparaNomeArquivo(a))
        print(caminho, dest.strip()+preparaNomeArquivo(a))
        i+=1

gera_pastas(_fonte)
copia_arquivos(_fonte, _destino)



