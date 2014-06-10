try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name':'PIBooth',
    'version': '0.1.0',
    'author': 'Paul Schuette',
    'author_email': 'paul@hanseartic.de',
    'packages': ['pibooth'],
    'scripts': [],
    'url': 'https://github.com/hanseartic/PIBooth/',
    'license': 'LICENSE.markdown',
    'description': 'Raspberry controlled photobooth.',
    'long_description': open('README.markdown').read(),
    'install_requires': [
        "RPi.GPIO >= 0.5.5",
    ]
}

setup(**config)
