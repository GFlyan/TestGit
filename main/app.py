import ipeadatapy as ipea
import streamlit as st
import pandas as pd

df = ipea.sources()
df
bota = "bacen"
def organization(phrase: str):
    """
    Retorna um dataframe contendo as series do IPEA de acordo com a string parametrizada referente a um órgão procurado.

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encotrado".
    """
    series = ipea.metadata()
    series = series[series["MEASURE"].str.contains("\\$")]
    series = pd.concat([series[series["SOURCE ACRONYM"].str.lower().str.contains(phrase.lower())],
                        series[series["SOURCE"].str.lower().str.contains(phrase.lower())]])
    series = series.sort_values(by='CODE').drop_duplicates()
    return "Não Encontrado" if series.empty else series


teste = organization(bota)
teste