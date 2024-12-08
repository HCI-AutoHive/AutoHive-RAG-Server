import pandas as pd

df = pd.read_excel("app/data/HCI_data.xlsx", engine="openpyxl")

df.to_csv("app/data/HCI_data.csv", index=False, encoding='utf-8-sig')
