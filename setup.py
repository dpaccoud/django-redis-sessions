from setuptools import setup, find_packages


setup(
    name = 'django-redis-sessions',
    version = '0.1',
    author = 'David Paccoud',
    author_email = 'dpaccoud@gmail.com',
    description = 'Redis Sessions Backend for Django',
    license = 'BSD',
    url = 'http://bitbucket.org/dpaccoud/django-redis-sessions/',
    keywords=['django', 'redis', 'sessions'],
    packages = find_packages(),
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
