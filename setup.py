from distutils.core import setup
setup(
  name = 'hsmpy3',
  packages = ['hsmpy3'],
  version = '1.0',
  license='GNU GPLv3',
  description = 'Highway Safety Manual Calculations',
  author = 'Mahdi Rajabi',
  author_email = 'mahdi.rajabi.96@gmail.com',
  url = 'https://github.com/mahdirajabi96',
  download_url = 'https://github.com/mahdirajabi96/hsmpy3/archive/v1.0.tar.gz',
  keywords = ['Highway Safety Manual'],
  install_requires=['arcpy'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU GPLv3',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
