import pandas as pd

weather_df = pd.DataFrame(X)
weather_df = weather_df.sort(['humidity', 'temprature'], ascending=False)
weather_df

