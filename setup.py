import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configleaf",
    version="0.0.1",
    author="Austin Poor",
    author_email="a-poor@users.noreply.github.com",
    description="Easy app config library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/configleaf",
    project_urls={
        "Bug Tracker": "https://github.com/a-poor/configleaf/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={
        "": "src"
    },
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "boto3==1.14.63",
        "python-dotenv==0.19.1",
        "pyyaml==5.3.1",
        "redis==3.5.3",
        "toml==0.10.1",
    ],
)
