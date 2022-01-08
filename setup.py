from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="next_episode",
      version="1.0.0",
      author="Sven Speckmaier",
      license="MIT",
      url='',
      packages=find_packages(where="src"),
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[
          'uuid'
      ],
      package_dir={"": "src"},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Intended Audience :: Kodi Users',
      ],
      scripts=[
          'bin/next-episode',
          'bin/next-season',
          'bin/remove-episode',
          'bin/fill-episode',
          'bin/generate-nfo',
          'bin/generate-show-nfo',
          'bin/next-artwork',
               ]
      )