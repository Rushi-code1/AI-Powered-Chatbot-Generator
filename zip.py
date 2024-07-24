import shutil 
import os.path

# Creating the ZIP file 
def ziped():
    path = os.getcwd()
    source_dir = os.path.join(path, "static", "uploded", "cast")
    archived = shutil.make_archive('Zipped file', 'zip', source_dir)
    print("ZIP file created:", archived) 
   
