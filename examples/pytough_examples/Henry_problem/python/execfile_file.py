import os
cwd = os.getcwd()

#execfile(cwd+'/python/parsing_inputfile.py')

#execfile(cwd+'/python/')
#execfile(cwd+'/python/running_model.py')
#execfile(cwd+'/python/parsing_outputfile.py')
#execfile(cwd+'/python/post_process.py')

import os
exec(open(os.path.join('python','pre_process.py')).read())
exec(open(os.path.join('python','running_model.py')).read())
exec(open(os.path.join('python','parsing_outputfile.py')).read())
exec(open(os.path.join('python','/python/post_process.py')).read())

