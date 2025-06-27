import os
import shutil

# Define the destination directories
model_out_dir = './MODEL_OUT'
global_mean_dir = './global_mean'
global_mean_ann_dir = './global_mean_annual'
forfeedbacks_dir = './MODEL_OUT/for_feedbacks'
forMOC_dir = './MODEL_OUT/for_MOC'
NPacific_dir = './MODEL_OUT/NPacific'
NPacific_box1_dir = './MODEL_OUT/NPacific/box1'
NPacific_box2_dir = './MODEL_OUT/NPacific/box2'
NPacific_box1_latlon_dir = './MODEL_OUT/NPacific/box1/latlon'
NPacific_box2_latlon_dir = './MODEL_OUT/NPacific/box2/latlon'

# Ensure the destination directories exist
os.makedirs(model_out_dir, exist_ok=True)
os.makedirs(global_mean_dir, exist_ok=True)
os.makedirs(forfeedbacks_dir, exist_ok=True)
os.makedirs(forMOC_dir, exist_ok=True)
os.makedirs(NPacific_dir, exist_ok=True)
os.makedirs(NPacific_box1_dir, exist_ok=True)
os.makedirs(NPacific_box2_dir, exist_ok=True)
os.makedirs(NPacific_box1_latlon_dir, exist_ok=True)
os.makedirs(NPacific_box2_latlon_dir, exist_ok=True)

# Get a list of all files in the current directory
files = os.listdir('.')

# Iterate through the files and move them based on the extension
for file in files:
    
    if file.endswith('output.nc'):
        shutil.move(file, os.path.join(model_out_dir, file))
        print(f'Moved {file} to {model_out_dir}')
    
    elif file.endswith('gm.nc'):
        shutil.move(file, os.path.join(global_mean_dir, file))
        print(f'Moved {file} to {global_mean_dir}')

    elif file.endswith('gm_ann.nc'):
        shutil.move(file, os.path.join(global_mean_ann_dir, file))
        print(f'Moved {file} to {global_mean_ann_dir}')
    
    elif file.endswith('forfeedbacks.nc'):
        shutil.move(file, os.path.join(forfeedbacks_dir, file))
        print(f'Moved {file} to {forfeedbacks_dir}')
    
    elif file.endswith('forMOC.nc'):
        shutil.move(file, os.path.join(forMOC_dir, file))
        print(f'Moved {file} to {forMOC_dir}')
    
    elif file.endswith('NPacific.nc'):
        shutil.move(file, os.path.join(NPacific_dir, file))
        print(f'Moved {file} to {NPacific_dir}')
    
    elif file.endswith('NPacific_box1.nc'):
        shutil.move(file, os.path.join(NPacific_box1_dir, file))
        print(f'Moved {file} to {NPacific_box1_dir}')
    elif file.endswith('NPacific_box1_latlon.nc'):
        shutil.move(file, os.path.join(NPacific_box1_latlon_dir, file))
        print(f'Moved {file} to {NPacific_box1_latlon_dir}')
    
        
    elif file.endswith('NPacific_box2.nc'):
        shutil.move(file, os.path.join(NPacific_box2_dir, file))
        print(f'Moved {file} to {NPacific_box2_dir}')
    elif file.endswith('NPacific_box2_latlon.nc'):
        shutil.move(file, os.path.join(NPacific_box2_latlon_dir, file))
        print(f'Moved {file} to {NPacific_box2_latlon_dir}')
        
    
