import setuptools

REQUIRED = [
    'pandas',
    're',
    'math'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kay-package", # Replace with your own username
    version="0.0.2",
    author="Kathy Roma",
    author_email="ekaterina-r@lambdastudents.com",
    description="Convertor time duration columns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KathyRoma/lambda_packages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)