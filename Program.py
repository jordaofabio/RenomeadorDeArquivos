import shutil
import os
import re
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

_fonte = "C:\Projetos\Restrita_v2\ARQUIVOS EM PDF_2018_ÁREA RESTRITA\\"
_destino = "C:\\Projetos\\Restrita_v2\\pdfs-formatados\\"

def gera_pastas(root):
    for pasta in os.listdir(root):
        novoRoot = root+pasta+'\\'
        novoDestino = remover_acentos(novoRoot.replace(_fonte, "")).lower()
        novoDestino = _destino+novoDestino

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
    for a in range(1, len(arquivo)):
        a = str(arquivo[i])
        novoArquivo = remover_acentos(a.strip())
        caminho = orig.strip()+a
        if os.path.isfile(caminho) and not os.path.exists(dest.strip()+novoArquivo.replace(" ","")):
            shutil.copy(caminho, dest.strip()+novoArquivo.replace(" ",""))
        print(caminho)
        i+=1

gera_pastas(_fonte)


