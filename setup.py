from distutils.core import setup
setup(
  name = 'hsmpy3',
  packages = ['hsmpy3'],
  version = '1.0',
  license='bsd-2-clause',
  description = 'Highway Safety Manual Calculations',
  author = 'Mahdi Rajabi',
  author_email = 'mahdi.rajabi.96@gmail.com',
  url = 'https://github.com/mahdirajabi96',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Highway Safety Manual'],
  install_requires=['arcpy'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)