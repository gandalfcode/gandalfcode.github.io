from gandalf.analysis.facade import *
import numpy as np
from scipy.stats import powerlaw


#Usual stuff that we saw before
sim=newsim(ndim=3,sim='sph')

#Here a few parameters that you might want to set
#Of course you can set other ones if you want
sim.SetParam('ic','python')
Ngas=?
sim.SetParam('Nhydro',Ngas) #or whatever you want
sim.SetParam('Nstar',1) #the star
sim.SetParam('gas_eos','isothermal')
sim.SetParam('temp0',?) #work out the right temperature
sim.SetParam('dimensionless',1)
sim.SetParam('hydro_forces',1)
sim.SetParam('sink_particles',1)
sim.SetParam('sink_radius',0.1)
sim.SetParam('nbody','lfkdk')
sim.SetParam('run_id',?)
sim.SetParam('tsnapfirst',?)
sim.SetParam('dt_snap',?)
sim.SetParam('tend',?)


sim.PreSetupForPython()

#Now we start doing the actual work
#Easier to work in cylindrical coordinates


#Use the np.random.uniform function for phi
#called like np.random.uniform(min,max,size)

#Use the powerlaw function from scipy for r
#called like follows:
#pw=powerlaw(exponent+1,loc=loc,scale=scale)
#random_numbers=pw.rvs(size)
#if you don't specify loc and scale the domain goes from 0 to 1
#loc shifts the domain and scale changes the extent
#beware: the parameter you pass is the exponent+1!

#Assume a gaussian for z (np.random.normal)
#called like np.random.normal(average,scale=scale,size=size)
#where scale is the standard deviation

#convert cylindrical/spherical coordinates to cartesian

#set the velocity


#import the arrays
#remember setting the masses of the particles as well!


#import the array for the star
#you need to set h as well - example below

hstar=np.ones(1)*0.1

sim.ImportArray(hstar,'h','star')

#Initial conditions have now been generated!
#Do what you want with them!
#Try doing a rendered plot perhaps


#Then you can run the simulation live
#Or also trying saving it to a snapshot file and running the file directly with the executable