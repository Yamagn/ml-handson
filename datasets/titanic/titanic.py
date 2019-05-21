import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier

# トレーニングデータをロード
train_df = pd.read_csv("train.csv", header=0)

train_df["Gender"]
