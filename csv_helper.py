"""
@author Merlin von der Weide
@version 1.0.0-beta
@date 30.07.2024
"""
import csv
import os
import sys

from config import ABSOLUTE_FILE_PATH

OUTPUT_FILENAME = "esdar-check_result.csv"


def prepare_csv_output(security_check_result):
    # TODO: Design the output for the CSV output.
    return security_check_result


def create_csv_file(prepared_output):
    """
        Writes URL information to a CSV file.

        Parameters:
        url_info_list (list of lists): A list where each element is a String (TODO: check if this is true) containing information about the DNS records.
        """

    filename = "esdar-check_result.csv"
    # Define the headers for the CSV file
    headers = ["URL", "MX Record", "SPF Record", "DKIM Record", "DMARC Record"]

    # Ensure that the Directory exists
    os.makedirs(os.path.dirname(ABSOLUTE_FILE_PATH + filename), exist_ok=True)
    # Try open the file and write output, if not working file is opened in OS and has to be closed before
    try:
        with open(ABSOLUTE_FILE_PATH + filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=",")

            # Write the headers to the CSV file
            writer.writerow(headers)

            # Write the URL information to the CSV file
            if len(prepared_output) > 1:
                for url_info in prepared_output:
                    writer.writerow(url_info)
            else:
                writer.writerow(prepared_output)
    except:
        print(
            "can't write output because %s is open, close the file and run the script again." % (ABSOLUTE_FILE_PATH + filename))
        sys.exit(1)
