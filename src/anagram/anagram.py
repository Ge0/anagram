import sys
import unicodedata

from collections import defaultdict
import itertools

from .errors import AnagramError


def load_file(filename, surnames_dict):
    with open(filename) as stream:
        for line in stream.readlines():
            name = line.strip()
            store_name(name, surnames_dict)


def strip_accents(name):
    name = unicodedata.normalize("NFKD", name)
    return name.encode("ascii", "ignore").decode()


def keyize_name(name):
    canonical_name = "".join(filter(str.isalpha, strip_accents(name))).upper()
    return "".join(sorted(canonical_name))


def store_name(name, surnames_dict):
    surnames_dict[keyize_name(name)].append(name.upper())


def diff_str(pattern, blacklist):
    output = ""
    for c in pattern:
        if c in blacklist:
            blacklist.remove(c)
            continue
        else:
            output += c
    return output


def find_anagrams(pattern, first_names_dict, names_dict):
    pairs = list()

    canonical_pattern = keyize_name(pattern)
    if len(canonical_pattern) <= 3:
        raise AnagramError("Pattern's length should be above 3 characters!")

    for i in range(2, len(canonical_pattern)-1):
        for permutation in itertools.combinations(canonical_pattern, i):
            found = False
            permutation = "".join(permutation)
            key = keyize_name(permutation)
            if key in names_dict:
                # Look for the other part in first names
                diff = diff_str(canonical_pattern, list(key))
                if diff in first_names_dict:
                    first_names, last_names = first_names_dict[diff], \
                        names_dict[key]
                    found = True
            elif key in first_names_dict:
                # Look for the other part in names.
                diff = diff_str(canonical_pattern, list(key))
                if diff in names_dict:
                    first_names, last_names = first_names_dict[key], \
                        names_dict[diff]
                    found = True

            if found:
                for pair in itertools.product(first_names, last_names):
                    if pair not in pairs:
                        pairs.append(pair)
                        yield pair
