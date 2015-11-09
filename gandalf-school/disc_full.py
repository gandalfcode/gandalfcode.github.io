from gandalf.analysis.facade import *
import numpy as np
from scipy.stats import powerlaw



#Usual stuff that we saw before
sim=newsim(ndim=3,sim='sph')

sim.SetParam('ic','python')
Ngas=1000
sim.SetParam('Nhydro',Ngas) #or whatever you want
sim.SetParam('Nstar',1) #the star
sim.SetParam('gas_eos','isothermal')
sim.SetParam('temp0','0.0025') #work out the right temperature
sim.SetParam('dimensionless',1)
sim.SetParam('hydro_forces',1)
sim.SetParam('sink_particles',1)
sim.SetParam('sink_radius',0.1)
sim.SetParam('nbody','lfkdk')
sim.SetParam('run_id','DISC1')
sim.SetParam('tsnapfirst',0.0)
sim.SetParam('dt_snap',6.28/20.)
sim.SetParam('tend',6.28*10)


sim.PreSetupForPython()

#Now we start doing the actual work

phi = np.random.uniform(0,2*np.pi,Ngas)

#generation of r coordinate
mr=powerlaw(0.5,loc=0.1,scale=10)
r=mr.rvs(size=Ngas)

#z coordinate, using first theta
theta=np.zeros(Ngas)
for i in range(Ngas):
    theta[i]=np.random.normal(0,scale=0.05*r[i]**0.5,size=1)
z=theta*r

#convert cylindrical/spherical coordinates to cartesian
x=np.sin(phi)*r
y=np.cos(phi)*r

vphi=1./np.sqrt(r)#/np.sqrt(2.)
vx=-np.cos(phi)*vphi
vy=np.sin(phi)*vphi
#vz=np.zeros_like(vx)

#import the arrays
sim.ImportArray(x,'x')
sim.ImportArray(y,'y')
sim.ImportArray(z,'z')
sim.ImportArray(vx,'vx')
sim.ImportArray(vy,'vy')
sim.ImportArray(np.ones_like(x)*0.0000001,'m')

#import the array for the star
xstar=np.zeros(1)
ystar=np.zeros(1)
zstar=np.zeros(1)
mstar=np.ones(1)
hstar=np.ones(1)*0.1
sim.ImportArray(xstar,'x','star')
sim.ImportArray(ystar,'y','star')
sim.ImportArray(zstar,'z','star')
sim.ImportArray(mstar,'m','star')
sim.ImportArray(hstar,'h','star')

#Initial conditions have now been generated!
#Do what you want with them!
#Try doing a rendered plot perhaps (can you do it straight away?!)
setupsim()
render('x','y','rho',lognorm=True)
window()
plot('x','y')
block()

run()
block()
#render('x','y','rho',lognorm=True)
#addplot('x','vx',type='star')
#Then you can run the simulation live
#Or also trying saving it to a snapshot file and running the file directly with the executable
