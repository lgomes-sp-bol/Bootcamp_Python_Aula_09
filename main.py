from loguru import logger

logger.add("app.log", rotation="1 MB", level="CRITICAL")
logger.info("Iniciando o programa")

def somar_numeros(a, b):
    logger.info(f"Calculando a soma de {a} e {b}")
    
    try:
        soma = a + b

    except TypeError as e:
        logger.critical(f"Erro ao somar números: {e}")
        raise

    return soma


if __name__ == "__main__":
    resultado = somar_numeros(5, 3)
    logger.info(f"Resultado: {resultado}")
