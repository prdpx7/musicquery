from setuptools import setup

setup(name="musicquery",
      version="0.24",
      test_suite='nose.collector',
      tests_require=['nose'],
      description="Get song_path from matched arguments with song tags",
      url="http://github.com/prdpx7/musicquery",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      packages=["musicquery"],
      keywords='music song-tags metadata linux script cli-tool',
      install_requires=[
          "tinytag",
      ],
      zip_safe=False)

