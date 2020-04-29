import os
cwd = os.getcwd()


#execfile(cwd+'/python/pre_process.py')
#execfile(cwd+'/python/running_model.py')
#execfile(cwd+'/python/parsing_outputfile.py')
#execfile(cwd+'/python/post_process.py')

path1=os.path.join(cwd,'python','pre_process.py')
exec(compile(open(path1).read(), path1, 'exec'))

path2=os.path.join(cwd,'python','running_model.py')
exec(compile(open(path2).read(), path2, 'exec'))

path3=os.path.join(cwd,'python','parsing_outputfile.py')
exec(compile(open(path3).read(), path3, 'exec'))

path4=os.path.join(cwd,'python','post_process.py')
exec(compile(open(path4).read(), path4, 'exec'))
