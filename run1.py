import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import kabuki
import numpy as np
import pickle
import hddm

dataSG = hddm.load_csv('Placebo_SG.csv')

m1SG = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m1SG.find_starting_values()
m1SG.sample(60000, burn=30000, thin=30,dbname='traces1SG.db', db='pickle')
#save_object(m,'Model1')
m1SG.save('Model1SG')

m2SG = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m2SG.find_starting_values()
m2SG.sample(60000, burn=30000, thin=30,dbname='traces2SG.db', db='pickle')
#save_object(m,'Model1')
m2SG.save('Model2SG')

m3SG = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m3SG.find_starting_values()
m3SG.sample(60000, burn=30000, thin=30,dbname='traces3SG.db', db='pickle')
#save_object(m,'Model1')
m3SG.save('Model3SG')

m4SG = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m4SG.find_starting_values()
m4SG.sample(60000, burn=30000, thin=30,dbname='traces4SG.db', db='pickle')
#save_object(m,'Model1')
m4SG.save('Model4SG')

m5SG = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m5SG.find_starting_values()
m5SG.sample(60000, burn=30000, thin=30,dbname='traces5SG.db', db='pickle')
#save_object(m,'Model1')
m5SG.save('Model5SG')
