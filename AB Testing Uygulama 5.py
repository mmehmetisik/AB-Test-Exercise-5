
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu,pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


######################################################
# AB Testing (İki Örneklem Oran Testi)
######################################################
# Bu test iki oran arasında karşılaştırma yapmak için kullanılır.
# Elimizde daha önce ortalama vardı. Şimdi ise oranlar var. Bu oranlar arasında istatistiki olarak anlamlı fark olup
# olmadığını anlamaya çalışacağız.

# Bu testin varsayımı örnek sayısının 30 dan büyük olması varsayımı vardır. Ama genelde örnek sayısı 30 dan büyüktür.

# H0: p1 = p2  Yeni web tasarımın Dönüşüm Oranı ile Eski web Tasarımın Dönüşüm Oranı Arasında İstatistiki Olarak Anlamlı Farklılık Yoktur.

# H1: p1 != p2 Yeni web tasarımın Dönüşüm Oranı ile Eski web Tasarımın Dönüşüm Oranı Arasında İstatistiki Olarak Anlamlı Farklılık Vardır.


basari_sayisi = np.array([300, 250])
gozlem_sayilari = np.array([1000, 1100])

proportions_ztest(count=basari_sayisi, nobs=gozlem_sayilari)

# p-value değeri 0.05 den küçük olduğu için H0 hipotezi reddedilir.
# İki oran arasında istatistiki olarak anlamlı bir farklılık vardır.

basari_sayisi / gozlem_sayilari
