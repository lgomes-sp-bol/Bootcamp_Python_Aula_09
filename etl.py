import pandas as pd
import os
import glob
from utils_log import log_decorator

@log_decorator
def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))   
    df_lista = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_lista, ignore_index=True)
    return df_total 

@log_decorator    
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_total_vendas = df.copy()
    df_total_vendas["Total"] = df["Quantidade"] * df["Venda"]
    return df_total_vendas

@log_decorator
def salvar_parquet_por_data(df: pd.DataFrame, path_saida: str):
    os.makedirs(path_saida, exist_ok=True)

    # Agrupa por data
    df["Data"] = pd.to_datetime(df["Data"])
    for data, df_dia in df.groupby(df["Data"].dt.date):
        data_str = pd.to_datetime(data).strftime("%Y%m%d")

        nome_arquivo = f"{path_saida}_{data_str}.parquet"

        df_dia.to_parquet(
            nome_arquivo,
            engine="pyarrow",
            index=False
        )

        print(f"Arquivo: {nome_arquivo} salvo com sucesso!")      
    return 

@log_decorator
def carregar_dados(df: pd.DataFrame, caminho: str, tipo_arq: list[str]) -> None:
    
    for tipo in tipo_arq:
        if tipo == "csv":
            df.to_csv(caminho + "." + tipo, index=False)
            print(f"Arquivo: {caminho + "." + tipo} salvo com sucesso!")      
        elif tipo == "json":
            df.to_json(caminho + "." + tipo, orient="records")   
            print(f"Arquivo: {caminho + "." + tipo} salvo com sucesso!")      
        elif tipo == "parquet":
            salvar_parquet_por_data(df, caminho)

    return None

@log_decorator
def calcular_kpi_total_vendas_consolidado(pasta: str, formato_saida: list[str]) -> None:
    dta_frame = extrair_dados_e_consolidar(pasta)
    dta_frame_calculado = calcular_kpi_total_vendas(dta_frame)
    carregar_dados(dta_frame_calculado, os.path.join(pasta, "total_vendas"), formato_saida) 
    
    return None

    

