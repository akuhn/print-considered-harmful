from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = None


setup(
  name = 'print-considered-harmful',
  packages = ['debug'],
  version = '1.4.0',
  description = 'Switch from print to debugger() and never look back!',
  long_description = long_description,
  author = 'Adrian Kuhn',
  author_email = 'akuhnplus@gmail.com',
  url = 'https://github.com/akuhn/print-considered-harmful',
  install_requires = ['ipdb'],
)
