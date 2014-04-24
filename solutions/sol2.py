import pandas as pd

weather_df = pd.DataFrame(X)
weather_df = weather_df.sort(['humidity', 'temprature'], ascending=False)
weather_df

webdata_df.kmeans_labels.value_counts().plot(kind='barh')

from IPython.display import Image
i = Image(filename='data/clustering_kmeans.png')
i

from IPython.display import Image
i = Image(filename='data/clustering_dbscan.png')
i