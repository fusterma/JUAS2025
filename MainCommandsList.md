# Main commands list

**N. Fuster-Marti­nez, G. Sterbini, D. Gamba, S. Kostoglou, J. Olivares** 

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

	twiss, sequence = name, centre, file = filename.txt, table = name;
        twiss, sequence = name, betx = ??, alfx = ??, bety = ??, alfy = ??, centre, file = filename.txt, table = name;
        select, flag = twiss, column = name, keyword, s, betx, bety;
        plot, haxis = s, vaxis = betx, color = 100, file = name;
   
**Matching action:**


	match, sequence = ??;
	global, q1 = ??;
	global, q2 = ??;
	vary, name = ??, step = 0.00001;
	vary, name = ??, step = 0.00001;
	lmdif, call = 50, tolerance = 1e-6;
	endmatch;

	
	match, sequence = ??;
	constraint, range = #e, betx = ??;
	constraint, range = #e, alfx = ??;
	vary, name = ??, step = 0.00001;
	vary, name = ??, step = 0.00001;
	lmdif, call = 50, tolerance = 1e-6;
	endmatch;


** Tracking action:**


	track, dump, file = name, deltap = ??;
	start, x = ??, px = ?? , y = ??, py = ??;
	start, x = ??, px = ?? , y = ??, py = ??;
	run, turns = 100;

        
## Cpymad library functions

**First, we need to load the cpymad library:**
	
	from cpymad.madx import Madx
	
**Next, we need to instantiate the MAD-X process:**
 	
	madx = Madx()
  	
**Main functions to communicate with the MAD-X process:**

	madx.call('filename')
	
	
	madx.input('MAD-X commands')
	
	
	madx.table.twiss.dframe()
    	madx.table.twiss.dframe()

 
## Python plot commands

**To change the size of the plot window:**

	plt.rcParams['figure.dpi'] = 100

**Plot command:**

	plt.plot(x,y,'ob',label='Example')

**Adding labels:**

	plt.xlabel('s[m]')
	plt.ylabel('[m]')
	
**Adding a legend:**

	plt.legend(loc='best')     
