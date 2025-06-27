#!/usr/bin/env python
# Wenchang Yang (wenchang@princeton.edu)
# Wed Oct  5 11:09:59 EDT 2022

# Plot the -6% Solar experiments (4-member ensemble, CM2.1)

if __name__ == '__main__':
    import sys

import sys
if '/tigress/wenchang/wython/' not in sys.path:
    sys.path.append('/tigress/wenchang/wython/')

import sys, os.path, os, glob, datetime
import xarray as xr, numpy as np, pandas as pd, matplotlib.pyplot as plt
#more imports
from misc.modelout import get_modelout_data, update_modelout_data
import xfilter
nwindow, dimlp = 9, 'year'
#lowpass = lambda x: x.filter.lowpass(1/nwindow, dim=dimlp, padtype='odd')
lowpass = lambda x: x.rolling(year=nwindow, center=False, min_periods=1).mean()
import geoxarray

#start from here
model = 'CM2.1p1'
daname = 't_surf'
func = lambda x: x.load().geo.fldmean()
funcname = 'glbmean'

labels = []
das = []
dass = {}

label = 'CTL1860'
expname = 'CTL1860_tigercpu_intelmpi_18_80PE'
da = update_modelout_data(daname=daname, model=model, expname=expname, func=func, funcname=funcname)
labels.append(label)
das.append(da)
dass[label] = da
da_ctl = da
 
label = '-6% Solar'
expname = 'CTL1860_m6pctSolar_tigercpu_intelmpi_18_80PE'
da = update_modelout_data(daname=daname, model=model, expname=expname, func=func, funcname=funcname)
labels.append(label)
das.append(da)
dass[label] = da
 
label = '-6% Solar from1001'
expname = 'CTL1860_m6pctSolar_from1001_tigercpu_intelmpi_18_80PE'
da = update_modelout_data(daname=daname, model=model, expname=expname, func=func, funcname=funcname)
labels.append(label)
das.append(da)
dass[label] = da
 
label = '-6% Solar from2001'
expname = 'CTL1860_m6pctSolar_from2001_tigercpu_intelmpi_18_80PE'
da = update_modelout_data(daname=daname, model=model, expname=expname, func=func, funcname=funcname)
labels.append(label)
das.append(da)
dass[label] = da
 
label = '-6% Solar from3001'
expname = 'CTL1860_m6pctSolar_from3001_tigercpu_intelmpi_18_80PE'
da = update_modelout_data(daname=daname, model=model, expname=expname, func=func, funcname=funcname)
labels.append(label)
das.append(da)
dass[label] = da

 
def wyplot(da, flip=False, reset_year=False, yearspan_ctl=None, lowpass_on=True, **kws):
    if yearspan_ctl is None: yearspan_ctl=slice(101,200)
    year_start = yearspan_ctl.start
    year_end = yearspan_ctl.stop
    timespan_ctl = slice(f'{year_start:04d}', f'{year_end:04d}')
    label = kws['label']
    ax = kws.pop('ax', plt.gca())
    da = da.groupby('time.year').mean('time') - da_ctl.groupby('time.year').mean('time').sel(year=yearspan_ctl).mean('year') #anom
    if flip: 
        #anomaly of the control run not zero for some experiments
        if 'from1001' in label or '-1%toP25xCO2' in label:
            da_offset = da_ctl.sel(time=slice('1001', '1100')).mean('time') - da_ctl.sel(time=timespan_ctl).mean('time')
        elif 'from2001' in label:
            da_offset = da_ctl.sel(time=slice('2001', '2100')).mean('time') - da_ctl.sel(time=timespan_ctl).mean('time')
        elif 'from3001' in label:
            da_offset = da_ctl.sel(time=slice('3001', '3100')).mean('time') - da_ctl.sel(time=timespan_ctl).mean('time')
        else:
            da_offset = 0
        da = da_offset*2 - da
    if reset_year:
        years = range(int(reset_year), da.year.size+int(reset_year))
        da = da.assign_coords(year=years)
    if da.year.size >= nwindow and lowpass_on: da = da.pipe(lowpass)
    #da = da.assign_coords(year=da.year-100) #shift the year axis to start with 0 (instead of 100)
    da.plot(**kws)
    #ax.plot(da.isel(year=-1).year, da.isel(year=-1), marker='o', fillstyle='none', color='gray')
    #ax.text(da.year.values[-1], da.values[-1], f'{da.year.values[-1]}', color='gray')
    
 
if __name__ == '__main__':
    from wyconfig import * #my plot settings

    # all the -6% solar experiments
    fig,ax = plt.subplots(figsize=(8,4))
    label = '-6% Solar'
    da = dass[label]
    da.pipe(wyplot, label=label+' from0101', reset_year=True)
    label = '-6% Solar from1001'
    yearspan_ctl = slice(1001,1100)
    da = dass[label]
    da.pipe(wyplot, label=label, reset_year=True, yearspan_ctl=yearspan_ctl)
    label = '-6% Solar from2001'
    yearspan_ctl = slice(2001,2100)
    da = dass[label]
    da.pipe(wyplot, label=label, reset_year=True, yearspan_ctl=yearspan_ctl)
    label = '-6% Solar from3001'
    yearspan_ctl = slice(3001,3100)
    da = dass[label]
    da.pipe(wyplot, label=label, reset_year=True, yearspan_ctl=yearspan_ctl)

    ax.legend()
    ax.set_ylabel(f'K')
    ax.set_title(f'CM2.1 GMST anom, $-6$% solar, {nwindow}-{dimlp}-lp')

    #savefig
    if 'savefig' in sys.argv or 's' in sys.argv:
        figname = __file__.replace('.py', f'__m6solar.png')
        plt.savefig(figname)
        # if 'overwritefig' in sys.argv or 'o' in sys.argv:
        #     wysavefig(figname, overwritefig=True)
        # else:
        #     wysavefig(figname)
    