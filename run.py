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

#--------------------------

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

#---------------

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

m30G = hddm.HDDM(dataOG,include= 'z', depends_on={'z': 'AD'})
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

#------------------------------------------

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




