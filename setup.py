from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="next_episode",
      version="0.0.1",
      author="Sven Speckmaier",
      packages=find_packages(where="src"),
      long_description=long_description,
      long_description_content_type="text/markdown",
      package_dir={"": "src"},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      scripts=[
          'bin/next-episode',
          'bin/next-season',
          'bin/remove-episode',
               ]
      )