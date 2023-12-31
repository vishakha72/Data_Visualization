

from google.colab import drive
drive.mount('/content/drive')

!ls "/content/drive/MyDrive/colab"

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/drive/MyDrive/colab/voterfile .csv")


from sklearn import preprocessing
string_to_int= preprocessing.LabelEncoder()
df=df.apply(string_to_int.fit_transform)
df

df.shape

df.size

df.dtypes

df.describe()

sns.lineplot(x="age" , y = "party", data = df)

sns.distplot(df['party'],kde = False)

"""According to above graph we can observe that there is more chances of party Democratic to win the elections as from past few years we can observe the data."""

Count = sns.relplot(x="party", y = 'age', col= 'income' , row= 'education', kind="line", hue="party", style="party", data =df)

sns.countplot(x='party',data = df)

x = sns.boxplot(x = "party",y = "income",data = df ,whis = np.inf)

"""Most of the parties are lying at other quarter. only 4th party is working as outlier so there is negligible chance of party 4 to win the elections."""

plt.figure(figsize=(10,6))

sns.pairplot(x_vars = ['age','party','income','education'], y_vars = ['age','party','income','education'], data = df)

plt.title("Pairplot", fontsize = 20)
