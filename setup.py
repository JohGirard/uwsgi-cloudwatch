from setuptools import setup, find_packages


setup(
    name='uwsgi-cloudwatch',
    version='0.0.1.4',
    packages=find_packages(exclude=('etc')),
    include_package_data=True,
    author='Johannes Girard Forked from Justin Stewart',
    author_email='johannes.girard@gmail.com',
    description='uwsgi-cloudwatch',
    url='https://github.com/JohGirard/uwsgi-cloudwatch',
    install_requires=[
        'click==6.6',
        'requests==2.10.0',
        'boto3==1.9.73',
        'arrow==0.8.0',
        'asyncio==3.4.3'
    ],
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ),
    entry_points={
        'console_scripts': [
            'uwsgi-cloudwatch = uwsgi_cloudwatch.main:cli'
        ]
    }
)
