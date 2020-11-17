import os

def delete_file_if_exists(filename='a'):
    try:
        os.remove(filename)
        print("file " + filename+ " deleted; ")
    except OSError:
        print("file " + filename+ " does not exist; ")
        pass


print("Current directory is " + cwd + "\n")

## this is to ensure 'pre_process' failed to generate new flow.inp and the simulation would therefore based on existing flow.inp
#
#if os.path.exists(inp_path):
#    os.remove(inp_path)
#    print("Existing " + inp.title + " deleted\n")
#else:
#    print("Can not delete " + inp.title + "  as it doesn't exists\n")
 
# this is to ensure 'pre_process' failed to generate new flow.inp and the simulation would therefore based on existing flow.inp
delete_file_if_exists('flow.inp')
# TO200917 it is found that if a previous case enables GENER, and the current case deleted GENER, the file 'GENER' will exist and impact the simulation result
# therefore, it is necessary to delete all capitalised files. 
delete_file_if_exists('MESH')
delete_file_if_exists('SAVE')
delete_file_if_exists('VERS')
delete_file_if_exists('TABLE')
delete_file_if_exists('INCON')
delete_file_if_exists('LINEQ')
delete_file_if_exists('GENER')
delete_file_if_exists('chemical.out')
delete_file_if_exists('solute.out')

