from setuptools import setup, find_packages

setup(name='dezerogym',
      version='0.0.0',
      license='MIT License',
      install_requires=['numpy', 'matplotlib'],
      description='Reinforcement learning environment used in the book "Deep Learning from Scratch 4"',
      author='Koki Saitoh',
      author_email='koki0702@gmail.com',
      url='',
      packages=find_packages()
      )