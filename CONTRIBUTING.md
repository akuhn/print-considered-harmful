# Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/print-considered-harmful

# Deployment

To build this package, run

    brew install pandoc
    pip install pypandoc
    python setup.py sdist

For my personal use, to deploy this package, run

    # Requires accounts on pypi
    # Requires .pypirc file in home folder
    twine upload -r test dist/print-considered-harmful-0.0.0.tar.gz
    twine upload dist/print-considered-harmful-0.0.0.tar.gz
