import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phimidi",
    version="0.0.2",
    author="phi ARCHITECT",
    author_email="phi@phiarchitect.com",
    description="sequence and render midi compositions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://phiarchitect.github.io/phi-midi",
    project_urls={
        "Code": "https://github.com/phiarchitect/phi-midi",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.9",
    install_requires=['mido', 'numpy']
)
