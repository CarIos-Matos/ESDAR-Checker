"""
@author Merlin von der Weide
@version 1.0.0-beta
@date 30.07.2024
"""
import os
import sys

from validators import domain as validate_domain

from terminal_message_handler import print_error, print_warning


def validate_provided_domains(domains):
    for domain in domains:
        if not validate_domain(domain):
            print_error("Invalid domain provided (%s)" % domain)
            sys.exit(1)


def validate_args(args):
    domain_arg_valid = args.domain is None or validate_domain(args.domain)
    domain_file_arg_valid = args.domains_file is None or os.path.isfile(
        args.domains_file)

    if not domain_arg_valid:
        print_warning("Domain is not valid. Is it formatted correctly?")
    elif not domain_file_arg_valid:
        print_warning("Domain file is not valid. Does it exist?")

    valid_args = domain_arg_valid and domain_file_arg_valid
    if not valid_args:
        print_error("Arguments are invalid.")
        sys.exit(1)

    return valid_args
