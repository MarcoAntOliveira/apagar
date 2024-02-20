import os

def apagar_imagens(diretorio):
    # Verificar se o diretório existe
    if not os.path.exists(diretorio):
        print(f'O diretório {diretorio} não existe.')
        return

    # Listar todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtrar apenas os arquivos de imagem (você pode ajustar os formatos de imagem conforme necessário)
    imagens = [arquivo for arquivo in arquivos if arquivo.endswith('.jpg') or arquivo.endswith('.png')]

    # Verificar se há imagens no diretório
    if not imagens:
        print(f'Não foram encontradas imagens no diretório {diretorio}.')
        return

    # Confirmar com o usuário antes de excluir as imagens
    confirmacao = input(f'Tem certeza que deseja excluir {len(imagens)} imagens em {diretorio}? (sim/não): ')
    if confirmacao.lower() != 'sim':
        print('Operação cancelada.')
        return

    # Excluir cada imagem
    for imagem in imagens:
        caminho_imagem = os.path.join(diretorio, imagem)
        os.remove(caminho_imagem)
        print(f'{imagem} excluída com sucesso.')

diretorio = '/caminho/para/o/diretorio'  # Substitua pelo caminho do diretório onde suas imagens estão
apagar_imagens(diretorio)
