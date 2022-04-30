from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name = 'SpotifyToYoutubeMP3',
    version = '1.0',
    description='App that gets spotify songs and downloadds the YouTube MP3 version of it',
    author='Nisarg',
    author_email='nisargparab8691@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
