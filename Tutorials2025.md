# MAD-X WORKSHOP JUAS 2025
**N. Fuster-Marti­nez, D. Gamba, S. Kostoglou** 

# **Tutorial 1: My first accelerator, a FODO cell**
<div style="font-size: 16px;">
The main goals of this tutorial are:
    
- to ensure that we all have a working enviroment,
    
- get familiar with the MAD-X pythonic approach,
    
- work on the optics of the simplest configuration we can design to get a net focusing effect of the beam in both transverse planes, a FODO cell.

  
<p>
<div style="display: flex; align-items: center;">

    
<div style="flex: 1; padding: 5px; margin-left: -0px;">
    
**FODO cell specifications:**<p>
- $L_{cell}$ = 100 m. <p>
- Two quadrupoles, one focusing (FQ) and another one defocusing (DQ).<p>
- $L_{q}$ = 1 m long.<p>
- The start of the sequence it is placed at the start of the first quadrupole.<p>
- f = 200 m (k x $L_{q}$ = 1/f).<p>

- Equal length drift spaces.<p>
 
</div>

<div style="flex: 1;">
    <img src="/Figures/Tutorial1_FODO.png" style="max-width: 90%;">
</div>

    
<div style="font-size: 16px;">
    
# **Questions:**
    
1. Run the provided FODO lattice in a MAD-X process.

2. Define a proton beam with a total energy, $E_{tot}$, of 450 GeV. Activate the sequence and compute the periodic linear optics functions with the Twiss command in MAD-X. Then, plot the $\beta$-functions. If you find a maximum $\beta$-function around 455 m, you succeeded!

3. Using the $\beta$-function plot obtained, can you estimate the phase advance of the cell? How does this value compare to the tune computed by MAD-X?
   
    $\mu (s)=\int_0^s \frac{1}{\beta (s)} ds$
    
4. Try to run the Twiss command with $E_{tot}$ = 0.7 GeV. What is the MAD-X error message?

5. Try to run the Twiss command with a focal length of 20 m. What is the MAD-X error message? Can you find a non-periodic solution for this lattice with initial $\beta_{x,y}$ = 1 m?

**SOLUTIONS**    
    
6. Coming back to the periodic solution found in question 2. Reduce the focusing strength of the quadrupoles by half. What is its effect on $\beta_{max}$, $\beta_{min}$, and $\Delta \mu$?

7. Compute the maximum beam size, $\sigma_{x,y}$, before and after reducing the strength of the quadrupoles for two beams, one of $E_{tot}$ = 450 GeV and the other of $E_{tot}$ = 7000 GeV. Assume a normalized horizontal and vertical emittance, $\epsilon_n^{x,y}$, of 3 mrad mm and use the following relation:

    $\sigma_{x,y}=\sqrt{\frac{\beta_{x,y}\epsilon_n^{x,y}}{\gamma}}$
    
    where $\gamma$ stands for the relativistic factor.

8. Using the nominal k, compute the required quadrupole magnetic field gradient and magnetic field at the poles using the following relations:
    
    $k[m^{-2}]=\frac{G[T/m]*0.3}{p[GeV/c]}$
    
    $B_{pole}[T]=G[T/m]*r_{in}[m] $
    
   Perform the calculation for two proton beams of 450 and 7000 GeV total energy, with a quadrupole inner aperture radius of 23 mm.
    
**SOLUTIONS**
    
# **Tutorial 2: Building a circular machine**
<div style="font-size: 16px;">
The main goals of this tutorial are:
    
- to install dipole magnets in the FODO cell designed in Tutorial 1 to build a circular machine,

- study the impact of the dipoles into the linear optics functions, 

- use the MAD-X matching module to define the required strength of the quadrupole for getting a desired tune of the machine, which is a crucial parameter in the design of a circular machine for getting the desired beam quality and stability. 

<p>
<div style="display: flex; align-items: center;">

<div style="flex: 1; padding: 5px; margin-left: -0px;">
    
**Added specifications:**<p>
- 4 sector dipoles of 15 m long, <p>
- assuming a drift space between the magnets as illustrated.<p>
 
</div>

<div style="flex: 1;">
    <img src="/Figures/Tutorial3_FODO.png" style="max-width: 90%;">
</div>

<div style="font-size: 16px;">
    
# **Questions:**
    
1. Install the dipoles in the sequence in the Tutorial2.madx file and run the complete file.
    
2. Compute the required bending angle for the dipoles considering a ring with 736 dipoles with equal bending angles (HINT: $2\pi=N\theta$). 
    
3. Define a proton beam with a total energy, $E_{tot}$, of 7000 GeV. Activate the sequence and change the dipole bending angle to the one computed in question 1. Then, compute the periodic linear optics functions with the twiss command in MAD-X. Do the dipoles (weak focusing) affect the maximum of the $\beta$-functions? And the dispersion?

4. From the phase advance of the FODO cell compute the horizontal and vertical tunes of the machine.
    
**SOLUTIONS**    
    
5. Using the MAD-X match block on a single FODO cell, match the tunes of the machine to 46.0 in both planes. Don't forget to power the dipoles!

        match, sequence = ??;
        global, q1 = ??;
        global, q2 = ??;
        vary, name = ??, step = 0.00001;
        vary, name = ??, step = 0.00001;
        lmdif, calls = 50, tolerance = 1e-6;
        endmatch;
           
6. If we change the beam energy to a total beam energy of 2 GeV, which are the new tunes of the machine? Why?

7. Using the chromaticity computed with MAD-X, compute the tunes for particles with $\Delta p/p = 10^{-3}$ using the following equation:

     $\Delta Q = dq \times \frac{\Delta p}{p}$

<p>
<div style="display: flex; align-items: center;">

<div style="flex: 1; padding: 5px; margin-left: -0px;">

- Chromaticity concept in a quadrupole magnet.<p>
- Orange and blue lines correspond to off-momentum particles and the green line represents the on-momentum particle. <p>
- An spread in the focusing effect of the quadrupole is observed due to the energy spread of the beam. 

</div>

<div style="flex: 1;">
    <img src="/Figures/Tutorial4_chroma.jpg" style="max-width: 100%;">
</div>
    
    
# **Tutorial 3: Natural chromaticity and correction**
<div style="font-size: 16px;">

The main objectives of this tutorial are:

- to analyze the effect of the natural chromaticity of a FODO cell on the particle beam dynamics,
    
- to assess the impact of a chromaticity correction scheme, utilizing two sextupoles, also on the particle beam dynamics through particle tracking studies."
    
**Two lattices will be used:**
    
- **Tutorial3-1.madx**: thin lens version of the lattice designed in Tutorial 2 for a 7 TeV total energy proton beam. 

    <div style="flex: 1;">
    <img src="/Figures/Tutorial3_FODO.png" style="max-width: 50%;">
    </div>
    
- **Tutorial3-2.madx**: thin lens version of a new lattice in which sextupoles have been added and matched for chromaticity correction.

<div style="display: flex; align-items: center;">
<div style="flex: 1; padding: 5px; margin-left: -0px;">
</div>

<div style="flex: 1;">
    <img src="/Figures/Tutorial5_chroma_correction.jpg" style="max-width: 90%;">
</div>
    
<p align="center">
<img src="/Figures/Tutorial5_FODO.png" width="90%"/>
</p>

<div style="font-size: 16px;">
    
# **Questions:**
    
**As starting point we use the lattice of tutorial3-1.madx.**    
    
1. Track two particles: one with initial coordinates x, y, px, py = (1 mm, 1 mm, 0, 0) and another with initial coordinates x, y, px, py = (100 mm, 100 mm, 0, 0) for 100 turns. Plot the horizontal and vertical phase spaces, x-px and y-py, respectively. How do the particles move in phase space turn after turn? Do you observe the tunes? Is there any noticeable difference between the two particles? It may be helpful to examine only the first 4 turns for a clearer picture.

        track, dump, file = name, deltap = ??;
        start, x = ??, px = ?? , y = ??, py = ??;
        start, x = ??, px = ?? , y = ??, py = ??;
        run, turns = 100;
        endtrack;
        
**Note**: You can access the tracking data table, for example, as follows:

        particle1=madx.table['track.obs0001.p0001'].dframe()
        particle2=madx.table['track.obs0001.p0002'].dframe()
    
2. Now, repeat the tracking exercise, but for two off-momentum particles by adding a $\Delta p/p = 10^{-2}$ to the initial particle conditions. How does the phase space look now? Is the tune still the same?
    
**Now we move to the tutorial3-2.madx lattice.** 
    
3. Use the second lattice and track the same two particles: one with initial coordinates x, y, px, py = (1 mm, 1 mm, 0, 0) and the other with x, y, px, py = (100 mm, 100 mm, 0, 0), both having $\Delta p/p = 0.01$, for 100 turns. Plot the horizontal and vertical phase spaces, x-px and y-py, respectively. Did you manage to recover the original tune for the off-momentum particle from question 1? Do you observe the tunes? What is happening?

4. Finally, move the tunes to (0.23, 0.23) and repeat the tracking exercise. Are the particles stable?
