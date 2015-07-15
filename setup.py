import setuptools

setuptools.setup(
    name="django-admin-actions",
    version="0.1.0",
    url="https://github.com/zerc/django-admin-actions",

    author="Vladimir Savin",
    author_email="zero13cool@yandex.ru",

    description="Extension for action system of django's admin with some useful boilerplate stuff",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
