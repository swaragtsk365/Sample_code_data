import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import kabuki
import numpy as np
import pickle
import hddm

dataOB = hddm.load_csv('Placebo_OB.csv')

m1OB = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m1OB.find_starting_values()
m1OB.sample(60000, burn=30000, thin=30,dbname='traces1OB.db', db='pickle')
#save_object(m,'Model1')
m1OB.save('Model1OB')

m2OB = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m2OB.find_starting_values()
m2OB.sample(60000, burn=30000, thin=30,dbname='traces2OB.db', db='pickle')
#save_object(m,'Model1')
m2OB.save('Model2OB')

m3OB = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m3OB.find_starting_values()
m3OB.sample(60000, burn=30000, thin=30,dbname='traces3OB.db', db='pickle')
#save_object(m,'Model1')
m3OB.save('Model3OB')

m4OB = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m4OB.find_starting_values()
m4OB.sample(60000, burn=30000, thin=30,dbname='traces4OB.db', db='pickle')
#save_object(m,'Model1')
m4OB.save('Model4OB')

m5OB = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m5OB.find_starting_values()
m5OB.sample(60000, burn=30000, thin=30,dbname='traces5OB.db', db='pickle')
#save_object(m,'Model1')
m5OB.save('Model5OB')
