import matplotlib.pyplot as plt

def create_plot(dct, bin_, name):
    y = dct.values()
    x = dct.keys()
    plt.figure(figsize=(12, 6))
    plt.bar(x, y,color='crimson',align='center')
    plt.xticks(list(x),[str(int(i)) if int(i)==float(i)
                        else str(i) for i in x])
    plt.ylabel('frequency')
    plt.xlabel(f'{name} values')
    plt.title(f'{name} histogram (bin={bin_})')
    plt.savefig(f'{name} histogram bin={bin_}.png')
    plt.show()

def histogram(lst, bin, plot=False):
    lst = sorted(lst)
    lower = (lst[0]//bin + 1)*bin
    dct = {lower:0}
    for i in range(len(lst)):
        if lst[i]<=lower:
            dct[lower]+=1
        else:
            while lst[i]>lower: lower=lower+bin
            dct[lower] =1
    if plot: create_plot(dct, bin ,plot)
    return dct


def smart_histogram(lst,bin_):
    dct, mn, mx, lim = {}, min(lst), max(lst), None
    if mn%bin_==0: lim=mn
    for i in lst:
        key = (i//bin_ + 1 if i%bin_!=0 or i==lim else i//bin_)*bin_
        if key in dct:
            dct[key]+=1
        else:
            dct[key] =1
    return dct


def fanction(option=True):
    if option:
        return lambda df, y: df/y
    else:
        return lambda x, y: x**y

def histogram_creator(lst, bin, name=None):
    dct = smart_histogram(lst, bin)
    if name: create_plot(dct, bin, name)
    return dct






# from hdbscan import HDBSCAN
# print(HDBSCAN(min_cluster_size=3, metric='euclidean').fit(data).labels_)
# from random import randint
# from time import time as t
# import numpy as np
#
# for j in range(1,8):
#     lst= np.random.normal(5, 3, 10**j)
#     t1 = t()
#     a = histogram(lst,2.5)
#     t2 = t()
#     b = smart_histogram(lst,2.5)
#     t3 = t()
#     print(b)
#     print('round j=',j,'O(nlogn) runtime: ',round(t2-t1,2),'O(n) runtime:', round(t3-t2,2))
