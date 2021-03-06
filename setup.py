from setuptools import setup, find_packages
import pathlib


requires = [
    'sphinx>=1.8',
]


def read(filename):
    return (pathlib.Path(__file__).parent / filename).read_text()


setup(
    name='sphinxcontrib-ogp',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    packages=find_packages(),
    url='https://github.com/sphinx-contrib/ogp',
    license='BSD License',
    author='shimizukawa',
    author_email='shimizukawa@gmail.com',
    description='Sphinx OGP feature for html builder',
    long_description=read('README.rst') + read('CHANGES.rst'),
    install_requires=requires,
    python_requires=">=3.5",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
