import os
exec(open(os.path.join('python','parsing_result.py')).read())
#exec(open(os.path.join('python','plot_results.py')).read())


path_tr_opt=os.path.join('python','plot_results.py')
exec(compile(open(path_tr_opt).read(), path_tr_opt, 'exec'))


