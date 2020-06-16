from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='importvers',
      version='0.0',
      description='Easily import different versions of git repository files',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Version Control :: Git',
        'Intended Audience :: Science/Research'
      ],
      keywords='import python git version control',
      #url='',
      author='Jake Sansom',
      author_email='jhsansom@gmail.com',
      license='MIT',
      packages=['importvers'],
      python_requires='>=3.0',
      install_requires=[
          'git',
          'os',
          'sys',
          'importlib',
          'shutil'
      ],
      zip_safe=False)
