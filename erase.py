import os
from path import Path
ROOT_DIR = Path(__name__).parent

def deletar_arquivos_por_tipo(diretorio, tipo):
    # Percorre todos os arquivos no diretório
    for raiz, pastas, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            # Verifica se o arquivo tem o tipo especificado
            if arquivo.endswith(tipo):
                # Constrói o caminho completo do arquivo
                caminho_arquivo = os.path.join(raiz, arquivo)
                print(caminho_arquivo)
                # Exclui o arquivo
                os.remove(caminho_arquivo)
                print(f"Arquivo '{caminho_arquivo}' excluído com sucesso.")

# Exemplo de uso:
diretorio_alvo = ROOT_DIR  # Substitua pelo caminho do seu diretório
tipo_arquivo = [".aux",".fdb_latexmk",".fls",".log",".out",".synctex.gz",] # Substitua pelo tipo de arquivo que você deseja excluir, por exemplo, '.txt'
diretorios = ["conjunto", "curriculo","curso_latex", "Docker", "Inglês", "modelo_tcc", "python","servidor_django", "slide", "slide2", "solid", "test", "trab_1_micro", "trab_ingles", "trab_so"]
"""for directory in diretorios:
    diretorio_alvo = ROOT_DIR / directory 
    for arquivos in tipo_arquivo:
        deletar_arquivos_por_tipo(diretorio_alvo, arquivos)
"""
for arquivos in tipo_arquivo:
        print(arquivos)
        deletar_arquivos_por_tipo(diretorio_alvo, arquivos)