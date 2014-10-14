gandalf
=======

GANDALF (Graphical Astrophysics code for N-body Dynamics And Lagrangian Fluids)



GANDALF is a new hybrid SPH and N-body code for combined star formation, planet formation and star cluster studies.  GANDALF is written in C++ to perform the main hydrodynamic and gravitational computations.  GANDALF also includes a Python library to allow interactive simulations and visualisation.   Initial conditions can also be generated inside Python allowing simple control of setting up, running a simulation, analysing and visualising it from a single Python script.  GANDALF uses hybrid parallelisation of OpenMP and MPI and is currently available as a beta-release.

The code is open-source and can be downloaded anonimously. Users are encouraged to use a github account so bug reports and other suggestions can be made on the github code pages, or to e-mail the authors so we can e-mail notifications and bug-fixes.


Download
---------------------

You can download the code by typing in a terminal:

 ```
 git clone https://github.com/gandalfcode/gandalf.git
 cd gandalf
 ```
 
If you wish to know more in detail what git is and what you can do with it, the [github help page](https://help.github.com/articles/set-up-git) has all the references needed.

Userguide
------------
The folder docs contains a latex file with the userguide.  The userguide contains a section about the requirements for installation and how to compile the code. You need at the very least a c++ compiler to compile the main code.

Contact
---------
David Hubber [david.hubber@googlemail.com](mailto:david.hubber@googlemail.com)

Giovanni Rosotti [rosotti@usm.lmu.de](mailto:rosotti@usm.lmu.de)
