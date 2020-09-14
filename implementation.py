import histogram_dct as hd
import pandas as pd

# load data
data = pd.read_excel('Example\distributions.xlsx')

# uniform distribution:
hd.histogram_dct(data['unf'], bin=12.5, name='uniform distribution')

# normal distribution:
hd.histogram_dct(data['nrm'], bin=4, name='normal distribution')

# exp distribution:
hd.histogram_dct(data['exp'], bin=5, name='exp distribution')

# mix distribution:
hd.histogram_dct(data['mix'], bin=5, name='mixed distribution')


# use the output dictionary (find the maximum key):
max_key, max_vlu, dct = None, 0, hd.histogram_dct(data['nrm'], bin=5)
for key, value in dct.items():
    if max_vlu < value:
        max_vlu =value
        max_key =key
print(f'maximum key: {max_key}\nmaximum value: {max_vlu}'
      f'\nprecent: {round(max_vlu/sum(dct.values())*100,2)}%')

