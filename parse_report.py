"""
This script extracts data from a PDF file containing a medical report.
"""
import os
import camelot
from crewai_tools import tool
from dotenv import load_dotenv

load_dotenv()

file_path = os.getenv("FILE_PATH")

#C:\Users\Vatsal\OneDrive\Desktop\Wingily assignment\WM17S _diabatic.pdf
@tool("parse_report_tool")
def extract_data_from_pdf(file_path=file_path):
    """
    Extracts data from a PDF file.

    Parameters:
        file_path (str): The path to the PDF file.

    Returns:
        list: A list of extracted data.
    """
    tables = camelot.read_pdf(file_path, pages="all", flavor="stream", edge_tol=2000)

    # Initialize a list to hold the extracted data
    extracted_data = []

    # Iterate over each table and extract relevant information
    for table in tables:
        df = table.df
        for index, row in df.iterrows():
            # Check if the row contains the expected number of columns (at least 4)
            if len(row) >= 4:
                # Trim white spaces or unwanted characters from the data
                test_name = row[0].strip()
                results = row[1].strip()
                units = row[2].strip()
                bio_ref_interval = row[3].strip()

                # Check if results, units, or bio_ref_interval are not null or empty
                if results and units and bio_ref_interval:
                    # Populate the output structure
                    test_data = {
                        "Test_Name": test_name,
                        "Results": results,
                        "Units": units,
                        "Bio.Ref.Interval": bio_ref_interval,
                    }

                    # Append to the extracted data list
                    extracted_data.append(test_data)
    return extracted_data
