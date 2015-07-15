# coding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = [
    'Django>=1.5.1',
]

setuptools.setup(
    name="django-admin-actions",
    version="0.1.0",
    url="https://github.com/zerc/django-admin-actions",

    author="Vladimir Savin",
    author_email="zero13cool@yandex.ru",

    description=("Extension for action system of django's admin with some "
                 "useful boilerplate stuff"),
    long_description=readme,

    packages=[
        'django_admin_actions',
    ],
    package_dir={'django_admin_actions':
                 'django_admin_actions'},

    install_requires=requirements,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
