import pandas as pd
from pathlib import Path


def lerArquivos(caminho: Path) -> list:
    arquivos = list(caminho.glob("*.csv"))
    dataframes = [] # criando lista para armazenar os dataframes

    for arquivo in arquivos: # para cada arquivo foi criada uma variavel para percorrer a lista de arquivos
        df = pd.read_csv(arquivo)
        dataframes.append(df) # adicionando os dataframes a lista

    return dataframes

def extrairCidade(endereco: str) -> str:
    # Verifica se o endereço é uma string
    if not isinstance(endereco, str):
        return None
    partes = endereco.split(",") # quebra as strings sempre que houverem virgulas
    if len(partes) >= 2:
        return partes[1].strip() # remove os espaços em branco antes e depois do primeiro elemento
    return None

def extrairEstado(endereco: str) -> str:
    # Verifica se o endereço é uma string
    if not isinstance(endereco, str):
        return None
    partes = endereco.split(",") 
    if len(partes) >= 3:
        subpartes = partes[2].split(" ")
        if len(subpartes) > 1:
            return subpartes[1].strip()
    return None

def tratarDados(df: pd.DataFrame) -> pd.DataFrame:
    # convertendo os tipos de dados das colunas para os corretos
    df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors='coerce') # errors='coerce' transforma valores que não podem ser convertidos em null
    df["Price Each"] = pd.to_numeric(df["Price Each"], errors='coerce')
    df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%y %H:%M", errors="coerce"
    ).dt.normalize()
    # especificando o formato da data e removendo a hora

    # calculo da receita total
    df["Total Price"] = df["Quantity Ordered"] * df["Price Each"]

    # extrair cidade e estado atraves do endereco da compra
    df["City"] = df["Purchase Address"].apply(extrairCidade)
    df["State"] = df["Purchase Address"].apply(extrairEstado)

    df.dropna(subset=["Order Date"], inplace=True) # removendo linhas com valores nulos 
    
    df["Order Date BR"] = df["Order Date"].dt.strftime("%d/%m/%Y")  
    return df

def salvarDataFrame(df: pd.DataFrame, caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True) # cria o diretorio pai se for necessário
    df.to_csv(caminho, index=False)


def main():
    caminho_data = Path("../etl-vendas/data")
    arquivos_csv = lerArquivos(caminho_data)

    if len(arquivos_csv) == 0: # se o tamanho da lista for igual a 0 (nulo), exibir mensagem
        print("nenhum arquivo encontrado")
        return
    
    df_unificado = pd.concat(arquivos_csv, ignore_index=True)

    df_tratado = tratarDados(df_unificado)

    print(df_tratado.head())
    print(df_tratado.info())

    salvarDataFrame(df_tratado, Path("../etl-vendas/data/vendas_unificadas2.csv"))

if __name__ == "__main__":
    main()