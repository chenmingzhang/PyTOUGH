import os
# below does not shown error
#exec(open(os.path.join('..','python','parsing_result.py')).read())
#exec(open(os.path.join('..','python','plot_results.py')).read())


path1=os.path.join('..','python','parsing_result.py')
exec(compile(open(path1).read(), path1, 'exec'))

