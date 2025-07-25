arquivo1 = input("Insira o caminho do arquivo 1: ") #/content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 1/prova_anon12.css || /content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 2/prova_anon16.css || /content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 3/prova_anon6.css
arquivo2 = input("Insira o caminho do arquivo 2: ") #/content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 1/prova_anon3.css || /content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 2/prova_anon19.css  || /content/drive/MyDrive/Python/projeto_pega_cola/suspeitos 3/prova_anon8.css

with open(arquivo1, 'r') as f1, open(arquivo2, 'r') as f2:
    linhas1 = f1.readlines()
    linhas2 = f2.readlines()

def limpa_linhas(linhas):
    linhas_limpas = []
    for linha in linhas:
        l = linha.strip().lower()
        if l != "":
            linhas_limpas.append(l)
    return linhas_limpas

linhas1 = limpa_linhas(linhas1)
linhas2 = limpa_linhas(linhas2)

linhas_iguais = 0
for linha in linhas1:
    if linha in linhas2:
        linhas_iguais += 1

total_linhas = max(len(linhas1), len(linhas2))
percentual_iguais = (linhas_iguais / total_linhas) * 100 if total_linhas > 0 else 0

print(f"Os arquivos têm {percentual_iguais:.2f}% de linhas idênticas.")

if percentual_iguais > 80:
    print("Alta suspeita de cola.")
elif percentual_iguais > 50:
    print("Suspeita de cola.")
else:
    print("Baixa suspeita de cola.")
