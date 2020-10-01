import setuptools

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.description }}",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.6",
)
