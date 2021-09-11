import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
setup(
    name='wagtail-blog-simple',
    version='1.0.1',
    packages=find_packages(),
    url='https://github.com/pupattan/wagtail-blog-simple',
    license='MIT',
    include_package_data=True,
    keywords="django wagtail blog app",
    author='Pulak Pattanayak',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=[
        'Django>=3.0.0',
        'wagtail',
    ],
    author_email='pkbsdmp@gmail.com',
    description='Simple and customizable blog app for wagtail',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)