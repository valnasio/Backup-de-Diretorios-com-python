import os
import shutil
from datetime import datetime
from log import setup_logger

PASTA_ORIGEM = r'C:\Users\user\Documents\Origem'
PASTA_DESTINO = r'C:\Users\user\Documents\Destino'


def validar_pasta(caminho: str) -> bool:
    return os.path.exists(caminho)


def criar_pasta(caminho: str) -> None:
    os.makedirs(caminho, exist_ok=True)
    print(f'[INFO] pasta criada: {caminho}\n')


def copiar_arquivo(origem: str, destino: str) -> bool:
    try:
        shutil.copy2(origem, destino)
        print(f'[INFO] Arquivo copiado: {origem}\n')
        return True
    except Exception as e:
        print(f'[ERRO] Falha ao copiar {origem}: {e}\n')
        return False


def exibir_resumo(copiados: int, ignorados: int, timestamp: str) -> None:
    print(f'\n[INFO] Resumo do Backup - {timestamp}\n')
    print(f'Arquivos copiados: {copiados}')
    print(f'Arquivos ignorados: {ignorados}\n')


def realizar_backup(pasta_origem: str, pasta_destino: str) -> None:
    try:
        if not validar_pasta(pasta_origem):
            print(f'[ERRO] A pasta de origem "{pasta_origem}" não existe.\n')
            return

        if not validar_pasta(pasta_destino):
            criar_pasta(pasta_destino)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivos_copiados = 0
        arquivos_ignorados = 0

        for item in os.listdir(pasta_origem):
            origem = os.path.join(pasta_origem, item)
            destino = os.path.join(pasta_destino, item)

            if os.path.isfile(origem):
                if copiar_arquivo(origem, destino):
                    arquivos_copiados += 1
                else:
                    arquivos_ignorados += 1
            else:
                print(f'[INFO] Ignorando {item} (não é arquivo)\n')
                arquivos_ignorados += 1

        exibir_resumo(arquivos_copiados, arquivos_ignorados, timestamp)

    except Exception as e:
        print(f'[ERRO] Ocorreu um erro durante o backup: {e}\n')
        raise


if __name__ == '__main__':
    logger = setup_logger()

    try:
        print('\n[INÍCIO] Iniciando o processo de backup...\n')
        realizar_backup(PASTA_ORIGEM, PASTA_DESTINO)

    except Exception:
        logger.error(
            'Ocorreu um erro durante a execução do script.',
            exc_info=True
        )
