import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='SocialSentiment',
                packages=['SocialSentiment'],
                install_requires=install_requires)