# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

from os import path
from setuptools import find_packages, setup

run_requirements = [
    "loguru==0.2.5",
    "pydantic==1.6.1",
    "fastapi==0.60.1",
    "uvloop==0.14.0rc2",
    "uvicorn==0.10.3",
    "pymongo==3.11.1",
    "gunicorn==19.9.0",
    "requests==2.23.0",
    "sphinx-rtd-theme==0.1.9",
    "recommonmark==0.6.0",
    "aiofiles==0.5.0",
    "numpy==1.19.4",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="cadastro_clientes",
    version="0.1.0",
    author="Kevin de Santana Araujo",
    author_email="kevin_santana.araujo@hotmail.com",
    packages=find_packages(exclude=["docs", "tests"]),
    url="https://github.com/kevinsantana/desafio-tecnico-juntos-somos-mais",
    description="API para cadastro de clientes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=run_requirements,
    python_requires=">=3.6",
)
