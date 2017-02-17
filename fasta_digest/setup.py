from setuptools import setup

setup(name='fasta_digest',
    version='0.1.0',
    description='Get the signature of a fasta file',
    scripts=['bin/compute_fasta_digest'],
    url='http://github.com/COMBINE-lab/FastaDigest',
    author='Rob Patro',
    license='BSD',
    packages=['fasta_digest'],
    install_requires=[
        'coloredlogs'
    ],
    zip_safe=False)
