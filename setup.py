from setuptools import setup

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2",
    "Topic :: Software Development :: Libraries",
]

setup(
    name='De Exchange Broker',
    version='0.0.0',
    packages=['deexbroker'],
    url='https://github.com/deginner/de-exchange-broker',
    license='MIT',
    classifiers=classifiers,
    author='deginner',
    author_email='support@deginner.com',
    description='',
    setup_requires=['pytest-runner'],
    include_package_data = True,
    install_requires=[
        'sqlalchemy>=1.0.9',
        'secp256k1==0.11',
        "bitjws==0.6.3.1",
        "flask>=0.10.0",
        "flask-login",
        "flask-cors",
        "flask-bitjws>=0.1.1.2",
        "alchemyjsonschema",
        "sqlalchemy-login-models"
    ],
    tests_require=['pytest', 'pytest-cov'],
    extras_require={"build": ["flask-swagger"]}
)
