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

def histogram(lst,bin_):
    dct, mn, mx, lim = {}, min(lst), max(lst), None
    if mn%bin_==0: lim=mn
    for i in lst:
        key = (i//bin_ + 1 if i%bin_!=0 or i==lim else i//bin_)*bin_
        if key in dct:
            dct[key]+=1
        else:
            dct[key] =1
    return dct

def histogram_dct(lst, bin, name=None):
    dct = histogram(lst, bin)
    if name: create_plot(dct, bin, name)
    return dct
