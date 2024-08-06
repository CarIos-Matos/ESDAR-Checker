"""
@author Merlin von der Weide
@version 1.1.0-beta
@date 06.08.2024
"""


def remove_new_line_char(domains):
    cleaned_domains = []
    for domain in domains:
        cleaned_domain = domain.replace('\n', '')
        cleaned_domains.append(cleaned_domain)
    return cleaned_domains


def replace_characters(record_to_check):
    char_to_replace = ";"
    new_char = ","
    # for record in record_to_check:
    updated_string = record_to_check.replace(char_to_replace, new_char)
    return updated_string
