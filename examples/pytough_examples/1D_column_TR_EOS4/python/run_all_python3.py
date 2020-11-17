import os
cwd = os.getcwd()

path_del=os.path.join('..','python','delete_prexisting_files.py')
exec(compile(open(path_del).read(), path_del, 'exec'))

path1=os.path.join('..','python','pre_process.py')
exec(compile(open(path1).read(), path1, 'exec'))

path2=os.path.join('..','python','run_tough2.py')
exec(compile(open(path2).read(), path2, 'exec'))

#path3=os.path.join('..','python','parsing_outputfile.py')     # this seems to be the same as parsing_tr_output.py
#exec(compile(open(path3).read(), path3, 'exec'))


path_tr_opt=os.path.join('..','python','parsing_tr_output.py')
exec(compile(open(path_tr_opt).read(), path_tr_opt, 'exec'))

read_field_data=os.path.join('..','python','read_field_data.py')
exec(compile(open(read_field_data).read(), read_field_data, 'exec'))

#parsing_tr_output.py 


#path4=os.path.join('..','python','post_process.py')
#exec(compile(open(path4).read(), path4, 'exec'))

#path5=os.path.join('..','python','check_balance.py')
#exec(compile(open(path5).read(), path5, 'exec'))

plot_tr_output=os.path.join('..','python','plot_tr_output.py')
exec(compile(open(plot_tr_output).read(), plot_tr_output, 'exec'))



#path6=os.path.join('..','python','validate_swcc.py')
#exec(compile(open(path6).read(), path6, 'exec'))
#
#
#path6=os.path.join('..','python','calc_swcc.py')
#exec(compile(open(path6).read(), path6, 'exec'))

