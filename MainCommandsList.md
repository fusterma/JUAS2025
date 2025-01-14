# Main commands list

**N. Fuster-Marti­nez, D. Gamba, S. Kostoglou** 

## MAD-X commands

**Lattice elements definition:**
        
    mb : sbend, angle = ??, l = ??; 
    mq : quadrupole, k1 = ??, l = ??;
    ms : sextupole, k2 = ??, l = ??;

**Sequence definition:**

    sequencename : sequence, refer = centre, l = ??;
    element1: elementType1, at = ??;
    element1: elementType1, at = ??;
    ...
    endsequence;

**Sequence activation:**

    use, sequence = sequencename;

**Call an external file:**

    call, file = name;

**Beam definition:**

    beam, particle = proton, energy = 7000;

**Twiss action:**

    select, flag = twiss, column = name, keyword, s, betx, bety;
    
	twiss, sequence = name, centre, file = filename.txt, table = name;
    
    twiss, sequence = name, betx = ??, alfx = ??, bety = ??, alfy = ??, centre, file =filename.txt, table = name;
    
    plot, haxis = s, vaxis = betx, color = 100, file = name;
   
**Matching action:**

	match, sequence = ??;
	global, q1 = ??;
	global, q2 = ??;
	vary, name = ??, step = 0.00001;
	vary, name = ??, step = 0.00001;
	lmdif, calls = 50, tolerance = 1e-6;
	endmatch;

	
	match, sequence = ??;
	constraint, range = #e, betx = ??;
	constraint, range = #e, alfx = ??;
	vary, name = ??, step = 0.00001;
	vary, name = ??, step = 0.00001;
	lmdif, calls = 50, tolerance = 1e-6;
	endmatch;


**Tracking action:**

	track, dump, file = name, deltap = ??;
	start, x = ??, px = ?? , y = ??, py = ??;
	start, x = ??, px = ?? , y = ??, py = ??;
	run, turns = 100;
    endtrack;   

        
## Cpymad library functions

**First, we need to load the cpymad library:**
	
	from cpymad.madx import Madx
	
**Next, we need to instantiate the MAD-X process:**
 	
	madx = Madx()
  	
**Main functions to communicate with the MAD-X process:**

	madx.call('filename')
	
	
	madx.input('MAD-X commands')
	
	
	madx.table.twiss.dframe()
 
## Python plot commands

**First, we need to load the matplotlib library:**
    
    from matplotlib.pyplot as plt 

**To change the size of the plot window:**

	plt.rcParams['figure.dpi'] = 100

**Plot command:**

	plt.plot(x,y,'ob',label='Example')

**Adding labels:**

	plt.xlabel('s[m]')
	plt.ylabel('[m]')
	
**Adding a legend:**

	plt.legend(loc='best')     
