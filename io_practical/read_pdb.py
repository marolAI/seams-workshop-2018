#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:57:57 2018

@author: maro
"""
for line in open('1hrc.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        type = list[2]
        if type == 'CA':
            residue = list[3]
            print(residue)

#from Bio.PDB import PDBParser
#parser = PDBParser()
#cyto_c = parser.get_structure('CytoC', '1hrc.pdb')
#
