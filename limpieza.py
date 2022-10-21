import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

final = pd.read_csv('./final.csv')
final.info()
final.drop(columns=['Luminosity'], inplace=True)
final = final.dropna()

final.head()
print(final)
final.to_csv("final_df.csv")

final.info()