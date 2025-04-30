import ipeadatapy as ipea
import streamlit as st
import pandas as pd

# "* TODOS OS TEMAS"
# themes = ipea.themes()
# themes

def searchTheme(phrase: str):
    phrase = phrase.lower()
    getThemeID = ipea.themes()
    getThemeID['NAME'] = getThemeID['NAME'].str.lower()
    getThemeID = getThemeID[getThemeID['NAME'].str.contains(phrase)]

    try:
        final = pd.DataFrame()
        for id in getThemeID['ID']:
            theme = ipea.metadata(theme_id=id)
            final = pd.concat([final, theme], ignore_index=True)

        allSeries = final.sort_values(by='CODE')
    except:
        return str("Não Encontrado")
    else:
        return allSeries

"* PESQUISA POR TEMAS"
testDataFrame = searchTheme("demografia")
testDataFrame




