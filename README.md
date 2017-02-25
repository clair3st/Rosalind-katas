# Rosalind-katas [![Build Status](https://travis-ci.org/clair3st/Rosalind-katas.svg?branch=master)](https://travis-ci.org/clair3st/Rosalind-katas) [![Coverage Status](https://coveralls.io/repos/github/clair3st/Rosalind-katas/badge.svg?branch=master)](https://coveralls.io/github/clair3st/Rosalind-katas?branch=master)

### Finding a Shared Motif

- **source:** http://rosalind.info/problems/lcsm/

Given: A collection of kk (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

### Consensus and Profile

- **source:** http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

### Substring

- **source:** http://rosalind.info/problems/subs/

Given: Two DNA strings ss and tt (each of length at most 1 kbp).

Return: All locations of tt as a substring of ss.

### Translation

- **source:** http://rosalind.info/problems/prot/

Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by ss.

### Point Mutations

- **source:** http://rosalind.info/problems/hamm/

Given two strings ss and tt of equal length, the Hamming distance between ss and tt, denoted dH(s,t)dH(s,t), is the number of corresponding symbols that differ in ss and tt. See Figure 2.

Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)dH(s,t).

### Computing GC content

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