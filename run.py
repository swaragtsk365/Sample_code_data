import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import kabuki
import numpy as np
import pickle
import hddm

dataSG = hddm.load_csv('Placebo_SG.csv')

m = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces1SG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model1SG')

m = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces2SG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model2SG')

m = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces3SG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model3SG')

m = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces4SG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model4SG')

m = hddm.HDDM(dataSG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces5SG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model5SG')

#--------------------------

dataSB = hddm.load_csv('Placebo_SB.csv')

m = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces1SB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model1SB')

m = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces2SB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model2SB')

m = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces3SB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model3SB')

m = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces4SB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model4SB')

m = hddm.HDDM(dataSB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces5SB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model5SB')

#---------------

dataOG = hddm.load_csv('Placebo_OG.csv')

m = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces1OG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model1OG')

m = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces2OG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model2OG')

m = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces3OG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model3OG')

m = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces4OG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model4OG')

m = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces5OG.db', db='pickle')
#save_object(m,'Model1')
m.save('Model5OG')

#------------------------------------------

dataOB = hddm.load_csv('Placebo_OB.csv')

m = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces1OB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model1OB')

m = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces2OB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model2OB')

m = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces3OB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model3OB')

m = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces4OB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model4OB')

m = hddm.HDDM(dataOB,include= 'z', depends_on={'z': 'AD'})
m.find_starting_values()
m.sample(60000, burn=30000, thin=30,dbname='traces5OB.db', db='pickle')
#save_object(m,'Model1')
m.save('Model5OB')




