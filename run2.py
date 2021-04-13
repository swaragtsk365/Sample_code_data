import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import kabuki
import numpy as np
import pickle
import hddm

dataSB = hddm.load_csv('Placebo_SB.csv')

m1SB = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m1SB.find_starting_values()
m1SB.sample(60000, burn=30000, thin=30,dbname='traces1SB.db', db='pickle')
#save_object(m,'Model1')
m1SB.save('Model1SB')

m2SB = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m2SB.find_starting_values()
m2SB.sample(60000, burn=30000, thin=30,dbname='traces2SB.db', db='pickle')
#save_object(m,'Model1')
m2SB.save('Model2SB')

m3SB = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m3SB.find_starting_values()
m3SB.sample(60000, burn=30000, thin=30,dbname='traces3SB.db', db='pickle')
#save_object(m,'Model1')
m3SB.save('Model3SB')

m4SB = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m4SB.find_starting_values()
m4SB.sample(60000, burn=30000, thin=30,dbname='traces4SB.db', db='pickle')
#save_object(m,'Model1')
m4SB.save('Model4SB')

m5SB = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m5SB.find_starting_values()
m5SB.sample(60000, burn=30000, thin=30,dbname='traces5SB.db', db='pickle')
#save_object(m,'Model1')
m5SB.save('Model5SB')
