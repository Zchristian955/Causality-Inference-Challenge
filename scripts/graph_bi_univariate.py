import matplotlib.pyplot as plt
import seaborn as sns


## Pie
plt.figure(figsize=(16,8))
df.diagnosis.value_counts().plot.pie(autopct="%.1f%%")
plt.title("col", fontsize = 20)
plt.legend(['Modality1','Modality2'])


##  Histogram
fig, ax = plt.subplots(1,5, figsize=(15, 8))
sns.set_style('darkgrid')
sns.histplot(df['col1'],color='yellow',kde=True,ax=ax[0])
ax[0].set_title("col1")
sns.histplot(df['col2'],ax=ax[1],kde=True)
ax[1].set_title("col2")
sns.histplot(df['col3'],color='red',kde=True,ax=ax[2])
ax[2].set_title("col3")



##biplot1 histogramm
plt.figure(figsize=(15, 8))
M = plt.hist(df_clean[df_clean.diagnosis == 'M'].area_mean, bins=30, label='Malignant', alpha=0.5, color='#b967ff')
B = plt.hist(df_clean[df_clean.diagnosis == 'B'].area_mean, bins=30, label='Benign', alpha=0.6, color='#ff6f69')
plt.legend()
plt.xlabel('Mean Area Values', fontsize=13)
plt.ylabel('Frequency', fontsize=13)
plt.title('Histogram of Frequency of Mean Area of Tumors', fontsize=16)
plt.show()

# Calculating the maximum mean area of malignant and benign tumors

print('The Maximum Mean Area for Malignant Tumor is',M[0].max())
print('The Maximum Mean Area for Benign Tumor is',B[0].max())



##biplot  and distributio per columns
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data4_m, split=True, inner="quart")
plt.xticks(rotation=90)



##boxplot
plt.figure(figsize=(10,10))
sns.boxplot(x="features",y="value", hue="diagnosis", data=data4_m)
plt.xticks(rotation=90)



## Sweat biplot using points
sns.set(style="whitegrid", palette="muted")
data_dia=y
data=df_clean
data_n_2= (data-data.mean())/(data.std())
data=pd.concat([y, data_n_2.iloc[:,0:10]], axis=1)
data=pd.melt(data, id_vars="diagnosis", var_name="features", value_name='value')
plt.figure(figsize=(10,10))
#tic=time.time()
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=90)



###biplot 
sns.set(style="whitegrid", palette="muted")
plt.figure(figsize=(10,10))
#tic=time.time()
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data4_m)
plt.xticks(rotation=90)




##Cumulative Distribution function

count, bins_count = np.histogram(df_clean[df_clean.diagnosis == 'M'].area_mean, bins=10)
  
pdf = count / sum(count)

cdf = np.cumsum(pdf)
  

plt.figure(figsize=(10, 6))
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
plt.legend()
plt.title("PDF & CDF of Malignant Tumor Area Mean", fontsize=16)
plt.xlabel(xlabel='Area Mean(Malignant Tumor)', fontsize=13)
plt.ylabel(ylabel='Probability', fontsize=13)

plt.show()



###Pairplot
sns.pairplot(data3_m, hue='diagnosis', markers=['o', 's'], corner=True, palette='plasma')
plt.show()

