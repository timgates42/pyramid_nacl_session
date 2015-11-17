from setuptools import find_packages
from setuptools import setup


with open('README.rst') as f:
    README = f.read()

with open('CHANGES.rst') as f:
    CHANGES = f.read()

setup(name='pyramid_nacl_session',
      version='0.1.dev0',
      description='Encrypted sessison cookie serializer ofr Pyramid',
      long_description='\n\n'.join([README, CHANGES]),
      url='https://github.com/zeomega/pyramid_nacl_session',
      license='Proprietary (copyright ZeOmega, all rights reserved)',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'pyramid>=1.5',
        'PyNaCl',
      ],
      test_suite='pyramid_nacl_session.tests',
)