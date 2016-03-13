try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple program that returns a random tweet based on the given keyword',
    'author': 'Nick Sypteras',
    'url': 'www.github.com/Syps/rand_tweet',
    'download_url': 'www.github.com/Syps/rand_tweet',
    'author_email': 'nsypteras@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['rand_tweet'],
    'scripts': [],
    'name': 'rand_tweet'
}

setup(**config)
