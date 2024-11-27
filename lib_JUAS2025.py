#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches

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
  
    ax2.set_ylim(-np.max(abs(myDF.angle)),np.max(abs(myDF.angle)))

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
