"""
Shared validators for GREAT
"""
from setuptools import setup, find_packages


setup(
    name='directory_validators',
    version='9.2.2',
    url='https://github.com/uktrade/directory-validators',
    license='MIT',
    author='Department for International Trade',
    description='Django validators for GREAT.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=3.2.18,<4.0.0',
        'olefile>=0.44,<1.0.0',
        'Pillow>=9.0.1',
        'pytz>=2017.2,<=2021.3',
        'urllib3>=1.26.5<2.0.0',
    ],
    extras_require={
        'test': [
            'pytest==3.0.2',
            'pytest-cov==2.3.1',
            'pytest-sugar==0.8.0',
            'flake8==5.0.4',
            'codecov>=2.1.8',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=65.0.2,<66.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
