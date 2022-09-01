""" Instalador para el paquete "tostadas_pipo". """

from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="tostadas_pipo",
    version="0.1",
    description="Sistema Administrativo de Tostadas Pipo C.A.",
    long_description=long_description,
    # Get more https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # ¿Cuan maduro esta este proyecto? Valores comunes son
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indique a quien va dirigido su proyecto
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        # Indique licencia usada (debe coincidir con el "license")
        "License :: OSI Approved :: GNU General Public License",
        # Indique versiones soportas, Python 2, Python 3 o ambos.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords="ejemplo instalador paquete tostadas_pipo",
    author="Leonardo J. Caballero G.",
    author_email="leonardocaballero@gmail.com",
    url="https://twitter/macagua",
    download_url="https://github.com/macagua/tostadas_pipo",
    license="GPL",
    platforms="Unix",
    packages=["tostadas_pipo", "tostadas_pipo/utilidades/"],
    include_package_data=True,
)
