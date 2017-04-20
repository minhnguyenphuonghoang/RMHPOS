import distutils.sysconfig
from distutils.core import setup
setup(name         = 'robotframework-whitelibrary',
      version      = '0.0.1',
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'Minh Nguyen',
      author_email = 'minhnph@hotmail.com',
      url          = 'https://github.com/minhnguyenphuonghoang',
      package_dir  = {'' : 'src'},
      py_modules = ['WhiteLibrary'],
      data_files = [(distutils.sysconfig.get_python_lib(), ["../WhiteLibrary/bin/WhiteLibrary.dll"])]
      )