from distutils.core import setup
setup(name='bein-htminilims',
      version='1.065',
      url='http://madhadron.com/bein',
      description='Web frontend to the MiniLIMS from bein',
      author='Fred Ross',
      author_email='madhadron@gmail.com',
      packages=['bein_htminilims', 'bein_htminilims.data',
                'bein_htminilims.data.templates'],
      scripts=['htminilims'],
      classifiers=['Topic :: System :: Shells', 'Topic :: Scientific/Engineering :: Bio-Informatics'],
      install_requires = ['cherrypy', 'unittest2', 'mako'],
      )
