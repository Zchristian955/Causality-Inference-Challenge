import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("../data/data.csv")
df.describe()

#Univariate
plt.figure(figsize=(16,8))
df.diagnosis.value_counts().plot.pie(autopct="%.1f%%")
plt.title("Diagnosis Ratio", fontsize = 20)
plt.legend(['Benign','Malignant'])


#split by modality of the variable
df=df[df['column']=='modality']
df.describe()



#Normalise data
df= (df-df.mean())/(df.std())
df.head()




#Correlation (heatmap)
f,ax=plt.subplots(figsize=(14,14))
sns.heatmap(df.corr(),annot=True, linewidths=5, fmt='.1f', ax=ax)


#heatmap for high coreelation above 0.5
plt.figure(figsize=(16,8))
sns.heatmap(df_clean[high_corr_columns].corr(), annot=True, cmap="coolwarm")
