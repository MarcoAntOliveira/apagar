from path import Path

def deletar_arquivos_por_tipo(diretorio, tipo):
    for arquivo in diretorio.walkfiles(f'*{tipo}'):
        arquivo.remove()
        print(f"Arquivo '{arquivo}' excluído com sucesso.")

# Exemplo de uso:
ROOT_DIR = Path(__file__).parent  # Substitua pelo caminho do seu diretório
tipo_arquivo = [".aux",".fdb_latexmk",".fls",".log",".out",".synctex.gz"]

diretorios = ["conjunto", "curriculo","curso_latex", "Docker", "Inglês", "modelo_tcc", "python","servidor_django", "slide", "slide2", "solid", "test", "trab_1_micro", "trab_ingles", "trab_so"]
for directory in diretorios:
    diretorio_alvo = ROOT_DIR / directory 
    for arquivos in tipo_arquivo:
        deletar_arquivos_por_tipo(diretorio_alvo, arquivos)


