# Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/py-omakase

# Deployment

To build this package, run

    brew install pandoc
    pip install pypandoc
    python setup.py sdist

For my personal use, to deploy this package, run

    # Requires accounts on pypi
    # Requires .pypirc file in home folder
    twine upload -r test dist/omakase-0.5.3.tar.gz
    twine upload dist/omakase-0.5.3.tar.gz
