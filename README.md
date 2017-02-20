# Rosalind-katas

## Computing GC content

- **source:** http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.


##Testing and ENV setup

Set up a virtual environment

`pip install -e .`
`pip install -e .[test]`

will install all required packages.

Run tests in a virtual environment with the command

`python -m pytest tests/`