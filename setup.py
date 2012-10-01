from distutils.core import setup

setup(
    name='cstypo',
    version='0.1.0',
    author='Juda Kaleta',
    author_email='juda.kaleta@gmail.com',
    packages=['cstypo', 'cstypo.tests'],
    scripts=['bin/cstypo.py'],
    url='https://github.com/yetty/cstypo',
    license=open('LICENSE.md').read(),
    description='Package to apply Czech typography easily',
    long_description=open('README.md').read(),
    install_requires=[],
)