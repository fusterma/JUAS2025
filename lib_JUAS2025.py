#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches
import matplotlib.animation
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def plotLatticeSeries(ax,series, height=1., v_offset=0., color='g',alpha=0.5,lw=3):
    aux=series
    ax.add_patch(
    patches.Rectangle(
        (aux.s-aux.l, v_offset-height/2.),   # (x,y)
        aux.l,          # width
        height,          # height
        color=color, alpha=alpha,lw=lw
    )
    )
    return;


def plot_layout(myDF):

    myTwiss=myDF
    fig = plt.figure(figsize=(13,8))
    ax1=plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=1)
    plt.plot(myTwiss['s'],0*myTwiss['s'],'k')

    DF=myTwiss[(myTwiss['keyword']=='quadrupole')]
    for i in range(len(DF)):
        aux=DF.iloc[i]
        plotLatticeSeries(plt.gca(),aux, height=aux.k1l, v_offset=aux.k1l/2, color='r')
    
    DF=myTwiss[(myTwiss['keyword']=='multipole')]
    for i in range(len(DF)):
        aux=DF.iloc[i]
        plotLatticeSeries(plt.gca(),aux, height=aux.k1l, v_offset=aux.k1l/2, color='r')


    DF=myTwiss[(myTwiss['keyword']=='multipole')]
    for i in range(len(DF)):
        aux=DF.iloc[i]
        plotLatticeSeries(plt.gca(),aux, height=aux.k2l, v_offset=aux.k2l/2, color='y')

    
    color = 'red'
    ax1.set_ylabel('1/f=K1L [m$^{-1}$]', color=color,fontsize=20)
    ax1.tick_params(axis='y',labelsize=20,labelcolor=color)
    ax1.tick_params(axis='x',labelsize=20)
    ax1.set_ylim(-np.max(abs(myDF.k1l)),np.max(abs(myDF.k1l)))
    
    ax2 = ax1.twinx()

    color = 'blue'
    ax2.set_ylabel('$\\theta$[rad]', color=color,fontsize=20)
    ax2.tick_params(axis='y', labelsize=20,labelcolor=color)


    DF=myTwiss[(myTwiss['keyword']=='sbend')]
    for i in range(len(DF)):
        aux=DF.iloc[i]
        plotLatticeSeries(plt.gca(),aux, height=aux.angle, v_offset=aux.angle/2, color='b')
        
    DF=myTwiss[(myTwiss['keyword']=='multipole')]
    for i in range(len(DF)):
        aux=DF.iloc[i]
        plotLatticeSeries(plt.gca(),aux, height=aux.k0l, v_offset=aux.k0l/2, color='b')
  
    ax2.set_ylim(-np.max(abs(myDF.k0l)),np.max(abs(myDF.k0l)))

    axbeta=plt.subplot2grid((3,3), (1,0), colspan=3, rowspan=2,sharex=ax1)

    plt.plot(myTwiss['s'],myTwiss['betx'],'b', label='$\\beta_x$')
    plt.plot(myTwiss['s'],myTwiss['bety'],'r', label='$\\beta_y$')
    plt.legend(loc='best',fontsize=20)
    plt.ylabel('[m]',fontsize=20)
    plt.xlabel('s [m]',fontsize=20)
    axbeta.tick_params(axis='both', labelsize=20)
    plt.grid()

    ax3 = plt.gca().twinx() 
    plt.plot(myTwiss['s'],myTwiss['dx'],'green', label='$D_x$', lw=2)
    ax3.set_ylabel('$D_x$ [m]', color='green',fontsize=20)
    ax3.tick_params(axis='y', labelsize=20,labelcolor='green')
    ax3.tick_params(axis='x', labelsize=20)
    ax3.set_ylim(0, 6);

    return

def animation_plot(particle1): 
    
    import matplotlib.animation
    from matplotlib.animation import FuncAnimation

    points=[(particle1.iloc[0].x,particle1.iloc[0].px),(particle1.iloc[1].x,particle1.iloc[1].px),(particle1.iloc[2].x,particle1.iloc[2].px),(particle1.iloc[3].x,particle1.iloc[3].px),(particle1.iloc[4].x,particle1.iloc[4].px),(particle1.iloc[5].x,particle1.iloc[5].px),(particle1.iloc[6].x,particle1.iloc[6].px)]

    x_data=particle1.x[0:7]
    y_data=particle1.px[0:7]

    # Configuración de la figura
    fig, ax = plt.subplots()
    ax.set_xlim(min(x_data)*2, max(x_data)*2)  # Límites del eje x
    ax.set_ylim(min(y_data)*2, max(y_data)*2)  # Límites del eje y
    ax.set_xlabel("x [m]")
    ax.set_ylabel("px")
    ax.legend(loc="upper left")  # Posición inicial de la leyenda

    # Adding phase space ellipse on the plot
    # Twiss parameters
    beta = 170     # Beta de Twiss
    alpha = -2.4   # Alpha de Twiss
    gamma = (1 + alpha**2) / beta  # Relación entre los parámetros de Twiss
    epsilon = 0.001**2/beta+alpha**2*0.001**2/beta  # Emittance (constante de área de la elipse)

    # Points of the ellipse
    theta = np.linspace(0, 2 * np.pi, 500)  # Ángulo paramétrico
    xa = np.sqrt(epsilon * beta) * np.cos(theta)  # Coordenadas x
    xpa = -np.sqrt(epsilon / beta) * (alpha * np.cos(theta) + np.sin(theta))  # Coordenadas x'

    # Configuración de la gráfica
    ax.plot(xa, xpa, label="Elipse en el espacio de fase", color="blue")

    colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta']
    shapes = ['o', '^', 's', 'P', 'D', '*', 'h']  # Circle, triangle, square, etc.

    # Initialize plot elements
    point, = ax.plot([], [], 'ro', markersize=10, label="Current Point")  # Current point
    trail = []  # Store the trail of points as individual plots

    # Initialization function
    def init():
        point.set_data([], [])
        return point,

    # Update function for each frame
    def update(frame):
        # Update the current point
        x, y = points[frame]
        point.set_data([x], [y])
        point.set_color(colors[frame % len(colors)])  # Change color dynamically
        point.set_marker(shapes[frame % len(shapes)])  # Change shape dynamically

        # Add the current point to the trail
        trail_point, = ax.plot(x, y, marker=shapes[frame % len(shapes)], color=colors[frame % len(colors)], markersize=8)
        trail.append(trail_point)

        # Actualizar la leyenda con información dinámica
        ax.legend(
            labels=[
                f"Phase space ellipse" ,  # Información dinámica del punto actual
                f"Turn number {frame} "  # Información del número de puntos trazados
            ],
            loc="upper left"
        )

        return [point] + trail  # Return all elements to re-render

    # Create the animation
    frames = len(points)
    ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=500)

    return ani