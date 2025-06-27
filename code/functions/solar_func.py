import numpy as np
import xarray as xr

def rename_latlon(da): # rename lat lon coordinates
    if 'xt_ocean' in da.dims:
        da = da.rename(xt_ocean='lon')
    if 'xt' in da.dims:
        da = da.rename(xt='lon')
    if 'xu_ocean' in da.dims:
        da = da.rename(xu_ocean='lon')
    if 'yt_ocean' in da.dims:
        da = da.rename(yt_ocean='lat')
    if 'yt' in da.dims:
        da = da.rename(yt='lat')
    if 'yu_ocean' in da.dims:
        da = da.rename(yu_ocean='lat')
    if 'st_ocean' in da.dims:
        da = da.rename(st_ocean='depth')
    return da


def get_basin(da, basin='Pacific',cutoff=True):
    
    if basin in ['Atlantic','Pacific','Indian','IndoPacific','SouthernOcean']:

        mask = xr.open_dataarray('../Solar/ocean_index_with_ATL_PAC_IND_mod_FIXED_MOC.nc') 
        
        if basin == 'Atlantic':
            da_masked = da.where(mask==1)
        if basin == 'Pacific':
            da_masked = da.where((mask == 2) | (mask == 3))
        if basin == 'Indian':
            da_masked = da.where(mask==4)
        if basin == 'IndoPacific':
            da_masked = da.where((mask == 2) | (mask == 3) | (mask == 4))
        if basin == 'SouthernOcean':
            da_masked = da.sel(lat=slice(None,-45))
        
        if cutoff == True and basin != 'SouthernOcean':
            da_masked = da_masked.sel(lat=slice(-45,None))
            #print(f'Retrieved {basin} basin, not including Southern Ocean.')
            
        #else:
        #    print(f'Retrieved entire {basin} basin.')
        
        return da_masked
    
    else:
        
        print('Invalid basin: Please select Atlantic, Pacific, Indian, IndoPacific, or SouthernOcean')


##### get x and y coordinates to plot stars indicating crashed experiments #####
def get_crash_coords(xdata, ydata, crash_year=-1, 
               window_yr=10):
    # note that the input data is often smoothed, so we have to plot at the closest central time
    # default: monthly data is smoothed with 10-year smoothing window
    # output: x and y coordinates for the crash to plot

    if crash_year == -1: # last year
        x_crash = xdata[-6*window_yr]
        y_crash = ydata[-6*window_yr]

    else: # if the crash year is any other year
        x_crash = xdata[crash_year*12]
        y_crash = ydata[crash_year*12]

    return x_crash, y_crash

# Implementation
# if (modelnames[ii] == 'FLOR' and (labels[iexp] == '-4%' or labels[iexp] == '-6%')) or (modelnames[ii] == 'CM2.1p1' and labels[iexp] == 
#                                                                     '+6%' or labels[iexp] == '-6%'):
#     #print(f'{modelnames[ii]} {labels[iexp]} crashed')
#     x_crash, y_crash = get_crash_coords(x, y, crash_year=-1)
#     ax[0,ii].scatter(x_crash, y_crash,
#                    marker = '*', s=100, color = 'r', zorder=10)

#     if modelnames[ii] == 'CM2.1p1' and labels[iexp] == '-6%':
#         x_crash, y_crash = get_crash_coords(x, y, crash_year=933)
#         ax[0,ii].scatter(x_crash, y_crash,
#                    marker = '*', s=100, color = 'r', zorder=10)

# find files that start with a certain pattern
def find_files(directory,start_str):
    import os
    files = [f for f in os.listdir(directory) if f.startswith(start_str)]

    # If you want to handle only the first matching file
    if files:
        matching_file = files[-1]
        #print(f"Found file: {matching_file}")
        return matching_file
    else:
        print("No file found.")
        return None

def get_experiment_names(model):
    if model == 'FLOR':
        extension = 'tigercpu_intelmpi_18_576PE'
        exps = ['p6p0sol_CTL1860',
                'p4p0sol_CTL1860',
                'p2p0sol_CTL1860', 
                'p1p0sol_CTL1860',
                'CTL1860_newdiag',
                'm1p0sol_CTL1860', 
                'm2p0sol_CTL1860',
                'm4p0sol_CTL1860',
                'm6p0sol_CTL1860',]
        modelstr = 'FLOR'

    if model == 'CM2.1p1':
        extension = 'tigercpu_intelmpi_18_80PE'
        exps = ['CTL1860_p6pctSolar', 
                'CTL1860_p4pctSolar',
                'CTL1860_p2pctSolar',
                'CTL1860_p1pctSolar', 
                'CTL1860',
                'CTL1860_m1pctSolar',
                'CTL1860_m2pctSolar',
                'CTL1860_m4pctSolar',
                'CTL1860_m6pctSolar',
                ]
        modelstr = 'CM2.1'
    return exps, extension, modelstr


def find_and_open_xarray_file(directory, keywords, verbose=True, use_first_if_multiple=False):

    # Inputs: 
    # directory: path to search
    # keywords: list of strings in filename
    # verbose: True = print messages
    # use_first_if_multiple: True = open first result if multiple exist

    # Outputs:
    # xarray DataArray if opened
    # list of matching files if not opened
    # None if no match
    
    from pathlib import Path
    import xarray as xr

    directory = Path(directory)
    matching_files = [
        file for file in directory.glob("*.nc")
        if all(kw in file.name for kw in keywords)
    ]

    if len(matching_files) == 1:
        if verbose:
            print(f"Opening file: {matching_files[0].name}")
        return xr.open_dataarray(matching_files[0])
    elif len(matching_files) > 1:
        if use_first_if_multiple:
            if verbose:
                print(f"Multiple matches found, using first: {matching_files[0].name}")
            return xr.open_dataarray(matching_files[0])
        else:
            if verbose:
                print(f"Multiple matches found: {[f.name for f in matching_files]}")
            return matching_files
    else:
        if verbose:
            print("No matching files found.")
        return None
