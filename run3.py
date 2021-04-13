import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import kabuki
import numpy as np
import pickle
import hddm

dataOG = hddm.load_csv('Placebo_OG.csv')

m1OG = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m1OG.find_starting_values()
m1OG.sample(60000, burn=30000, thin=30,dbname='traces1OG.db', db='pickle')
#save_object(m,'Model1')
m1OG.save('Model1OG')

m2OG = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m2OG.find_starting_values()
m2OG.sample(60000, burn=30000, thin=30,dbname='traces2OG.db', db='pickle')
#save_object(m,'Model1')
m2OG.save('Model2OG')

m3OG = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m3OG.find_starting_values()
m3OG.sample(60000, burn=30000, thin=30,dbname='traces3OG.db', db='pickle')
#save_object(m,'Model1')
m3OG.save('Model3OG')

m4OG = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m4OG.find_starting_values()
m4OG.sample(60000, burn=30000, thin=30,dbname='traces4OG.db', db='pickle')
#save_object(m,'Model1')
m4OG.save('Model4OG')

m5OG = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m5OG.find_starting_values()
m5OG.sample(60000, burn=30000, thin=30,dbname='traces5OG.db', db='pickle')
#save_object(m,'Model1')
m5OG.save('Model5OG')
