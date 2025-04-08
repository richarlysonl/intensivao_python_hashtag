# pip install pyautogui
import pyautogui
import time
# pyautogui.press() aperta uma tecla
# pyautogui.write digita algo
# pyautogui.click clica em uma posição
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#digitar o site
site ="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

# passo 2: fazer login
# preencher email
pyautogui.click(x=645,y=485)
pyautogui.write("pythonimpressionador@gmail.com")
# preencher senha
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")
# logar
pyautogui.press("tab")
pyautogui.press("enter")
# botao logar


# esperar 3 segundos
time.sleep(3)
# passo 3 importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# passo 4 cadastrar 1 produto
for coluna in tabela.columns
for linha in tabela.index: # para cada linha na minha tabela
    pyautogui.click(x=613,y=328)
    codigo=tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")# passar para o proximo campo
    marca=tabela.loc[linha,"marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")# passar para o proximo campo
    tipo=tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")# passar para o proximo campo
    categoria=str(tabela.loc[linha,"categoria"])                          # string = texto -> srt()
    pyautogui.write(categoria)
    pyautogui.press("tab")# passar para o proximo campo
    preco_unitario=tabela.loc[linha,"preco_unitario"]
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")# passar para o proximo campo
    custo=tabela.loc[linha,"custo"]
    pyautogui.write(custo)
    pyautogui.press("tab")# passar para o proximo campo
    obs=tabela.loc[linha,"obs"]
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")# passou para o botao enviar 
    pyautogui.press("enter")
    pyautogui.scroll(10000)
#passo 5 repetir para todos os produtos
# nan -> not a number