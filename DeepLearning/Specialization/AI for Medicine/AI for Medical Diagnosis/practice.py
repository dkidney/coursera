import numpy as np
import pandas as pd
from keras import backend as K
import tensorflow as tf

sensitivity = 0.9
specificity = 0.8
prevalence = 0.2

ppv = sensitivity * prevalence / (sensitivity * prevalence + (1-specificity) * (1-prevalence))
print(ppv)

accuracy = sensitivity * prevalence + specificity * (1-prevalence)
print(accuracy)

p1 = np.array([.3,.7,.3,.7,.9,.7,.3,.7,.3])
g = np.array([0.,1.,0.,1.,1.,1.,0.,1.,0.])
1 - (2*np.dot(p1, g)) / (np.dot(p1, p1) + np.dot(g, g))

p2 = np.array([.5, .7, .5, .7, .9, .7, .5, .7, .5])
1 - (2*np.dot(p2, g)) / (np.dot(p2, p2) + np.dot(g, g))

p3 = g
1 - (2*np.dot(p3, g)) / (np.dot(p3, p3) + np.dot(g, g))

p4 = 1 - g
1 - (2*np.dot(p4, g)) / (np.dot(p4, p4) + np.dot(g, g))



df = pd.DataFrame([[1., 2.], [1, 2]])
df
df.dtypes
df[0]
df[0].dtype
df[0].dtype == float
df[1]

isinstance(df[0], float)
isinstance(df[0].dtype, float)
