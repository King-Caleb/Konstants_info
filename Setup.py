from setuptools import setup, find_packages

setup(
    name="KonstantsAPI",  # Your package name
    version="1.0.0",  # Package version
    author="King Caleb",  # Your name
    author_email="your-email@example.com",  # Your email
    description="A powerful API for handling constants efficiently.",  # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",
    url="https://github.com/King-Caleb/Konstants_info",  # GitHub repository URL
    packages=find_packages(),  # Automatically find all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
