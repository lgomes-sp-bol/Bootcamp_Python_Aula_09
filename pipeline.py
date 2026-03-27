from etl import calcular_kpi_total_vendas_consolidado

pasta: str = "Data"
formato_de_saida: list[str] = ["csv", "json", "parquet"]


calcular_kpi_total_vendas_consolidado(pasta, formato_de_saida)
