from pyteomics import mzxml
import csv

# Path to your mzXML file
mzxml_path = r'C:\Users\skl448\Desktop\phd\data\zooms\phd_data\phd_data_sjaelland\second_run\20240416-0910_TTF_011479_ONJ_TR_JonasHJ_2024_04_16_CPH2101005550_partial.mzXML'

# Directory to store output TSV files
output_directory = r'C:\Users\skl448\Desktop\phd\data\zooms\phd_data\phd_data_sjaelland\second_run\.tsv'

# Read the mzXML file
with mzxml.read(mzxml_path) as reader:
    for i, spectrum in enumerate(reader):
        # Create a unique filename for each spectrum
        tsv_path = f'{output_directory}\\spectrum_{spectrum["id"]}.tsv'

        # Open the output TSV file for writing for the current spectrum
        with open(tsv_path, 'w', newline='') as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter='\t')
            
            # Write headers (customize as needed)
            tsv_writer.writerow(['m/z', 'intensity', 'charge'])

            # Data for the current spectrum
            mzs = spectrum['m/z array']
            intensities = spectrum['intensity array']
            charges = spectrum.get('charge array', [None] * len(mzs))

            # Write each peak to the TSV for the current spectrum
            for mz, intensity, charge in zip(mzs, intensities, charges):
                tsv_writer.writerow([mz, intensity, charge])

print("Conversion of all spectra completed and saved in separate files.")
