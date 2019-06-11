#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created By  : Robert Rösler
"""
Loesung fuer Aufgabe 6, Aufgabenblatt 3 Kognitive Systeme SS19.

Run levenshtein.py, that's it. 
"""



def main():
    #reference
    ref = "wenn es im Juni viel donnert kommt ein trüber Sommer"
    #hypotheses
    h1 = "im Juni viel Sonne kommt einen trüberen Sommer"
    h2 = "viel Donner im Juni einen trüberen Sommer bringt"
    h3 = "Juni Donner einen Sommer"
    h4 = "im Juni viel Donner bringt einen trüben Sommer"
    h5 = "wenns im Juno viel Donner gibts einen trüben Sommer"

    print("ref: ",ref,"\n \n","h1:",h1,"\n","h2: ",h2,"\n","h3: ",h3,"\n","h4: ",h4,"\n","h5: ",h5,"\n")

    # Part a)
    #calculate levenshtein distances
    print("a) Calculate levenshtein distances, pass sentences as list of words: \n")
    print("ref - h1: ",levenshtein(ref.split(),h1.split()),"\n")
    print("ref - h2: ",levenshtein(ref.split(),h2.split()),"\n")
    print("ref - h3: ",levenshtein(ref.split(),h3.split()),"\n")
    print("ref - h4: ",levenshtein(ref.split(),h4.split()),"\n")
    print("ref - h5: ",levenshtein(ref.split(),h5.split()),"\n")

    # Part b)
    #calculate levenshtein distances
    print("b) Calculate levenshtein distances, pass sentences as string: \n")
    print("ref - h1: ",levenshtein(ref,h1),"\n")
    print("ref - h2: ",levenshtein(ref,h2),"\n")
    print("ref - h3: ",levenshtein(ref,h3),"\n")
    print("ref - h4: ",levenshtein(ref,h4),"\n")
    print("ref - h5: ",levenshtein(ref,h5),"\n")

    # Part c)
    #calculate levenshtein distances
    print("c) Calculate levenshtein distances with substitution error-value = 2: \n")#
    print("ref - h1: ",levenshtein(ref.split(),h1.split(),2),"\n")
    print("ref - h2: ",levenshtein(ref.split(),h2.split(),2),"\n")
    print("ref - h3: ",levenshtein(ref.split(),h3.split(),2),"\n")
    print("ref - h4: ",levenshtein(ref.split(),h4.split(),2),"\n")
    print("ref - h5: ",levenshtein(ref.split(),h5.split(),2),"\n")
    


def levenshtein(s1, s2,subst_error_points=1):
    """
    Imported from  https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance.
    """

    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1
            if subst_error_points != 1:
                if (c1 != c2): 
                    substitutions = previous_row[j] + subst_error_points
                else:
                    substitutions = previous_row[j]
            else:
                substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

if __name__ == "__main__":
        main()