# MAD-X WORKSHOP JUAS 2025
**N. Fuster-Marti­nez, D. Gamba, S. Kostoglou** 

# **Tutorial 1: My first accelerator, a FODO cell**
<div style="font-size: 16px;">
The main goal of this tutorial is to ensure that we all have a working enviroment, get familiar with the MAD-X pythonic approach and work on the optics of the simplest configuration we can design to get a net focusing effect of the beam in both transverse planes, a FODO cell.
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
    
1. Run in a MAD-X process the provided FODO lattice.

2. Define a proton beam with a total energy, $E_{tot}$, of 450 GeV. Activate the sequence and compute the periodic linear optics functions with the twiss MAD-X command. Then, plot the $\beta$-functions. If you found a maximum $\beta$-function around 455 m you succeeded!

3. Using the $\beta$-function plot obtained, can you estimate the phase advance of the cell? How does this value compare to the tune computed by MAD-X.
   
    $\psi (s)=\int_0^s \frac{1}{\beta (s)} ds$
    
4. Try to run the twiss command with $E_{tot}$ = 0.7 GeV. What is the MAD-X error message?

5. Try to run the twiss command with a focal length to 20 m. What is the MAD-X error message? Can you find a non-periodic solution for this lattice?

6. Coming back to the periodic solution found in question 2. Reduce by half the focusing strength of the quadrupoles, what is the effect of it on the $\beta_{max}$, $\beta_{min}$ and $\Delta \mu$? 

7. Compute the maximum beam size, $\sigma_{x,y}$, before and after reducing the strength of the quadrupoles. Assume a normalized horizontal and vertical emittance, $\epsilon_n^{x,y}$, of 3 mrad mm for two beams, one of $E_{tot}$ = 450 GeV and the other of $E_{tot}$ = 7000 TeV using the following relation::

    $\sigma_{x,y}=\sqrt{\frac{\beta_{x,y}\epsilon_n^{x,y}}{\gamma}}$
    
    where $\gamma$ stands for the relativistic factor.

8. Compute the corresponding quadrupole's magnetic field gradient and magnetic field at the poles using the following relation:
    
    $k[m^{-2}]=\frac{G[T/m]*0.3}{p[GeV/c]}$
    
    $B_{pole}[T]=G[T/m]*r_{in}[m] $
    
    Do the calculation for both 450 and 7000 GeV proton beams and a quadrupole inner aperture radius of 20 mm.
    
# **Tutorial 2: Building a circular machine**
<div style="font-size: 16px;">
The main goal of this tutorial is to install dipole magnets in the FODO cell designed in Tutorial 1 to build a circular machine as well as to study the impact of the dipoles into the linear optics functions. In addition, the MAD-X matching module will be used to define the required strength of the quadrupole for getting a desired tune of the machine. The tune is a crucial parameter in the design of a circular machine for getting the desired beam quality and stability. 
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
    
1. Compute the required bending angle for the dipoles, consider a ring with 736 dipoles with equal bending angles and change the corresponding value in the given lattice (HINT: $2\pi=N\theta$) in order to power the dipole magnets.
    
2. Define a proton beam with a total energy, $E_{tot}$, of 7000 GeV. Activate the sequence and change the dipole bending angle to the one computed in question 1. Then, compute the periodic linear optics functions with the twiss MAD-X command. Do the dipoles (weak focusing) affect the maximum of the $\beta$-functions? And the dispersion?

3. From the phase advance of the FODO cell compute the horizontal and vertical tunes of the machine.
    
4. Using the MAD-X match block on a single FODO cell, match the tunes of the machine to 46.0 in both planes.

        match, sequence = ??;
        global, q1 = ??;
        global, q2 = ??;
        vary, name = ??, step = 0.00001;
        vary, name = ??, step = 0.00001;
        lmdif, call = 50, tolerance = 1e-6;
        endmatch;
           
5. If we change the beam energy to a total beam energy of 2 GeV, which are the new tunes of the machine? Why?

6. Using the chromaticity computed with MAD-X, compute the tunes for particles with $\Delta p/p = 10^{-3}$ using the following equation:

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

The main goal of this tutorial is to study the impact of the natural chromaticity of a FODO cell on the particles' beam dynamics by means of particle tracking studies. 
    
In order to do this tutorial, we will use as starting point, the thin lens version of the lattice designed in Tutorial 2 for a 7 TeV total energy proton beam

The thin lens lattice is mandatory in order to use the track MAD-X module. The makethin command should be used for this purpose. Additionally, after running the makethin command, it will be necessary to perform a rematch of the lattice to ensure that the horizontal and vertical tunes of the FODO cell remain at 0.25.
    
<div style="flex: 1;">
    <img src="/Figures/Tutorial3_FODO.png" style="max-width: 40%;">
</div>
    
Then, we will use a second lattice in which 2 sextupoles have been installed in order to correct the natural chromaticity of the FODO cell to study the impact of them on the particles' beam dynamics.
    
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
    
1. Track two particles, one with initial coordinates x, y, px, py = (1 mm, 1 mm, 0, 0) and another one with initial coordinates x, y, px, py = (100 mm, 100 mm, 0, 0) in 100 turns. Plot the horizontal and vertical phase space, x-px and y-py respectively. How do the particles move in the phase space turn after turn? Do you see the tunes? Do you see any difference between the two particles? It may help to look only at the first 4 turns to get a clear picture.

        track, dump, file = name, deltap = ??;
        start, x = ??, px = ?? , y = ??, py = ??;
        start, x = ??, px = ?? , y = ??, py = ??;
        run, turns = 100;
        endtrack;
        
**Note**: you can access the tracking data table, for example, as:

        particle1=madx.table['track.obs0001.p0001'].dframe()
        particle2=madx.table['track.obs0001.p0002'].dframe()
    
2. Repeat the tracking exercise but now for two of-momentum particles by adding a $\Delta p/p = 10^{-2}$ to the initial particles' conditions. How does the phase space look now? Is the tune still the same?
    
**Now we move to use tutorial3-2.madx lattice.** 
    
3. Now use the second lattice and track two particles, one with initial coordinates x, y, px, py = (1 mm, 1 mm, 0, 0) and another one with initial coordinates x, y, px, py = (100 mm, 100 mm, 0, 0) and both with $\Delta p/p = 0.01$ for 100 turns. Plot the horizontal and vertical phase space, x-px and y-py respectively. Did you manage to recover the original tune for the off-momentum particle from Tutorial 4? Do you see the tunes? What is going on?

4. Move the tunes to (0.23, 0.23) and repeat the tracking exercise. Are the particles stable?
