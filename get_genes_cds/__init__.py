#!/usr/bin/env python
import sys

from Bio import SeqIO


def has_start(sequence):
    return sequence.startswith("ATG")

def has_stop(sequence):
    stop_codons = set(["TAG", "TAA", "TGA"])
    if sequence[-3:] in stop_codons:
        return True

def is_gene(sequence):
    if has_start and has_stop:
        return True
    return False

def is_valid(record):
    name = None
    gene = None
    symbol = None

    for num, item in enumerate(record.description.split(" ")):
        if num == 0:
            name = item
        elif item.startswith("gene:"):
            gene = item.split("gene:")[-1]
        elif item.startswith("gene_symbol:"):
            symbol = item.split("gene_symbol:")[-1]

    if name and gene and symbol:
        return gene,name,symbol
    return False

def read_records(file_name=None):
    with open(file_name, "rU") as input_handle:
        records = []
        for num, record in enumerate(SeqIO.parse(input_handle, "fasta")):
            validated = is_valid(record)
            if validated:
                gene, name, symbol = validated
                if is_gene(record.seq):
                    print gene, name, symbol
