import os
import re
from setuptools import setup, find_packages

version = re.compile(r'__version__\s*=\s*\((.*?)\)')

def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "src/python/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return ".".join(m.groups()[0].split(", "))


if __name__ == '__main__':
    setup(name = 'Motu Client',
          version = get_package_version(),
          description = 'Download client for Mercator Ocean data',
          author='CLS (Collecte Localisation Satellites)',
          url='https://github.com/metocean/motu-client-python',
          package_dir={'motu':'src/python',
                       'motu.lib': 'src/python/lib'},
          package_data={'motu': ['etc/*']},
          packages=['motu','motu.lib'],
          entry_points={
            'console_scripts': [
                'motu = motu.motu_client:main',
        ],
    },
)