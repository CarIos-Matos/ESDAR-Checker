"""
ESDAR-Checker should help to check for one or more up to a larger number of domains or URL's whether the following records are present:
- DMARC
- SPF
- DKIM
- MX Records

@author Merlin von der Weide
@version 1.1.0-beta
@date 06.08.2024
"""
from checkdmarc import get_dmarc_record
import dns.resolver
# Import Libraries for Domain specific check
#import pkg_resources
#pkg_resources.require("checkdmarc==4.4.1")


# Message Styling
from banner_message import get_banner_message as banner_message
from checkdmarc import UnverifiedDMARCURIDestination, MultipleDMARCRecords, DMARCRecordNotFound, InvalidDMARCTagValue
from csv_helper import *
from domain_validator import validate_args
from helper import remove_new_line_char, replace_characters
from terminal_message_handler import *

# Additional Imports
import argparse

selectors = []
append_new_lines = False


def initialize():
    # TODO SELECTOR MUST BE CHANGED to be able to retrieve multiple selectors
    parser = argparse.ArgumentParser(
        prog="esdar-checker_v2.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    domain_argument_group = parser.add_mutually_exclusive_group(required=True)
    domain_argument_group.add_argument("--domain", type=str,
                                       help="Check a single Domain (format: google.com) for DNS records (MXRecords/SPF/DKIM/DMARC")
    domain_argument_group.add_argument("--domains_file", type=str,
                                       help="File containing list of domains to check for DNS records (MXRecords/SPF/DKIM/DMARC")
    parser.add_argument("--selector", type=str, default="",
                        help="DKIM selector which is needed for DKIM record lookup")

    parser.add_argument("--append", type=str, default= False,
                        help="New checked domains are added to already the existing csv file, if no file exists a new file will be created")

    arguments = parser.parse_args()
    return arguments


def main(args):
    validate_args(args)

    domains_list = []

    if args.selector:
        selectors.append(args.selector)

    if args.append == "yes":
        global append_new_lines
        append_new_lines = True

    if args.domain:
        domains_list.append(args.domain)
    else:
        with open(args.domains_file, "r") as domains_file:
            # TODO: doesnt work correctly so far, cause for false behaviour wasnt found -> TO BE FIXED SOON
            domains_file_content = domains_file.readlines()
            cleaned_domains = remove_new_line_char(domains_file_content)
            domains_list.extend(cleaned_domains)

    domains_list = cleanup_domains_list(domains_list)

    if len(domains_list) > 0:
        # TODO: no no here should only one domain get provided and after the check it should be immediatly written to the CSV otherwise if there are to many entries it will result in an stack Overflow
        raw_esdar_check_result = perform_esdar_check(domains_list)
        if append_new_lines == True:
            write_new_line_to_csv_file(raw_esdar_check_result)
        else:
            write_rows_to_csv(raw_esdar_check_result)

    else:
        print_error("No domain(s) were provided")


## performs the dns security check and returns the list with the result
def perform_esdar_check(domains_list):
    iterator = 0
    single_domain_result = []
    domains_list_result = []
    for single_domain in domains_list:
        # clear the list
        single_domain_result.clear()
        # dns security check
        single_domain_result.append(single_domain)
        single_domain_result.append(lookup_mxrecords(single_domain))
        single_domain_result.append(lookup_spf_record(single_domain))
        single_domain_result.append(lookup_dkim_record(single_domain, selectors, iterator))
        single_domain_result.append(lookup_dmarc_record(single_domain))
        domains_list_result.append(single_domain_result.copy())
        # Iterator is needed if there are multiple domains and therefore multiple selectors for the DKIM Lookup
        iterator += 1
    return domains_list_result


def lookup_mxrecords(domain):
    print()
    print("Testing domain", domain, "for MXRecords...")
    try:
        mx_record = dns.resolver.resolve(domain, 'MX')
        mail_servers = []
        for a in mx_record:
            mail_servers.append(a)
            return mail_servers
    except:
        return "No MXRecord found."


def lookup_spf_record(domain):
    print()
    print("Testing domain", domain, "for SPF record...")
    try:
        txt_records = dns.resolver.resolve(domain, "TXT")
    except dns.resolver.NoAnswer:
        return "no SPF Record found"
    for record in txt_records:
        spf_record = "".join([a.decode("utf-8") for a in record.strings])
        if "v=spf" in spf_record:
            return spf_record


# TODO: works so far with one domain but with domain file it doesnt work atm
def lookup_dkim_record(domain, selector="", iterator=0):
    if selector:
        print()
        print("Testing domain", domain, "for DKIM record with selector", selector, "...")
        try:
            test_dkim = dns.resolver.resolve(selector + '._domainkey.' + domain, 'TXT')
            for dns_data in test_dkim:
                if 'DKIM1' in str(dns_data):
                    return str(dns_data)
        except:
            return "No DKIM record found with selector: %s." % selector
            pass
    return "No selector choosen, Provide a selector with the --selector [\"SELECTOR\"] option"


def lookup_dmarc_record(domain):
    print()
    print("Testing domain", domain, "for DMARC record...")
    dmarc_record_string = ""
    raw_dmarc_record = get_dmarc_record(domain, nameservers=["8.8.8.8", "https://ns1.avectris.ch"],
                                                   timeout=10)
    dmarc_record_list = list(raw_dmarc_record.items())
    (record, location, parsed) = dmarc_record_list
    dmarc_record_string += "Record: " + record[1] + "; " + "Location: " + location[1]
    return replace_characters(dmarc_record_string)


def prepare_summary_output(security_check_result):
    # TODO
    print(" Function not implemented atm")


def print_summary_on_terminal(prepared_output):
    # TODO
    print("Function not implemented atm")


def cleanup_domains_list(domains_list):
    domains_list = [d.lower() for d in domains_list]
    domains_list = list(dict.fromkeys(domains_list))

    domains_list.sort()
    return domains_list


if __name__ == "__main__":
    print(banner_message())
    arguments = initialize()
    main(arguments)
