from setuptools import setup, find_packages

setup(
    name="helloworld",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A simple Hello World Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/helloworld",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # add dependencies here if needed
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "hello=helloworld.main:say_hello",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
