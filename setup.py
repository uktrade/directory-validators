"""
Shared validators for GREAT
"""
from setuptools import setup, find_packages


setup(
    name='directory_validators',
    version='7.0.0',
    url='https://github.com/uktrade/directory-validators',
    license='MIT',
    author='Department for International Trade',
    description='Django validators for GREAT.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=2.2.24,<3.0a1',
        'olefile>=0.44,<1.0.0',
        'Pillow>=8.2.*',
        'pytz>=2017.2,<=2020.1',
        'urllib3>=1.26.5<2.0.0',
    ],
    extras_require={
        'test': [
            'pytest==3.0.2',
            'pytest-cov==2.3.1',
            'pytest-sugar==0.8.0',
            'flake8==3.0.4',
            'codecov>=2.1.8',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
