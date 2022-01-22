from setuptools import setup, find_packages


setup(
    name='validate_field',
    version='0.1',
    license='MIT',
    author="Sarath Chandran",
    author_email='programspeaker@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)