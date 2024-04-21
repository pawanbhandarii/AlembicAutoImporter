import os
import unreal
import json


file_is_updated = False
file_up_to_date = False
json_file = r"Z:\BERG\CENTRALTEST\Content\Python\TestScripts\modification.json"  # Output file to store modification dates
directory_to_check = r"M:\IRAS\BERG\KTOFB"
extension = ".fbx"

def file_update_checker_fun():
    global file_is_updated
    global file_up_to_date
    previous_modification_dates={}
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            for line in file:
                file_path, modification_time = line.strip().split(": ")
                previous_modification_dates[file_path] = float(modification_time)
                
    # Check modification dates of files in the directory
    current_modification_dates = {}
    for root, dirs, files in os.walk(directory_to_check):
        for file_name in files:
            if file_name.lower().endswith(extension):
                file_path = os.path.join(root, file_name)
                current_modification_dates[file_path] = os.path.getmtime(file_path)
    
    # Compare modification dates
    file_is_updated = False
    for file_path, current_mod_time in current_modification_dates.items():
        if file_path not in previous_modification_dates or previous_modification_dates[file_path] < current_mod_time:
            file_is_updated = True
            break
    
    if file_is_updated:
        file_up_to_date = False
        print("Files have been modified.")
    else:
        file_up_to_date = True
        print("Files are up to date.")

def update_file_status(directory, extension, output_file):
    with open(output_file, 'w') as file:
        # Walk through the directory tree
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.lower().endswith(extension):
                    file_path = os.path.join(root, file_name)
                    modification_time = os.path.getmtime(file_path)
                    file.write(f"{file_path}: {modification_time}\n")
    
    print("Modification dates written to", output_file)

def import_files_from_txt(txt_file_to_open_from):
    with open(txt_file_to_open_from, 'r') as file:
        for line in file:
            file_path = line.strip()  # Remove any leading/trailing whitespace or newlines
            if file_path:  # Check if the line is not empty
                importAlembic(file_path)


def importAlembic(filename):

    task = unreal.AssetImportTask()

    auto = True
    destination_name = ''
    destination_path = '/Game/AlembicCache'
    filename = r"D:\Personal\testalembicfiles\bear01.abc"
    task.set_editor_property('automated', auto )
    task.set_editor_property('destination_name', destination_name)
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)

    task.options = unreal.AbcImportSettings()
    task.options.import_type = unreal.AlembicImportType.GEOMETRY_CACHE
    task.options.compression_settings.merge_meshes = True     
    task.options.material_settings.find_materials = True
    task.options.sampling_settings.frame_start = 900    
    task.options.sampling_settings.frame_end = 1300
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task]) 

file_update_checker_fun()

if file_is_updated == True:
    update_file_status(directory_to_check, extension, json_file)
    import_files_from_txt(json_file)

