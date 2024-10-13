
V_plot Generator

This project generates a V-Plot to visualize the relationship between fragment length and relative position around a midpoint based on mapped genomic data in BED format. It processes the data, extracts fragment information, and generates a 3D plot using GNUplot.

## Prerequisites

To use this script, you'll need:
- Python (compatible with Python 2.x or 3.x lower than 3.6)
- Gnuplot
- Unix-based command-line tools (`zcat`)

## Files

- **v_plot.py**: The Python script that reads BED data, processes it, and generates a TSV file with relative positions, fragment lengths, and counts.
- **vplot.gnuplot**: The GNUplot script to plot the V-Plot based on the generated TSV file.

## Usage

1. **Prepare Input Data**:
    - The input file should be a `.bed.gz` file containing mapped genomic data.
  
2. **Running the Script**:
    - Use the following command to generate the V-Plot:

    ```bash
    zcat mapped.bed.gz | python v_plot.py | gnuplot vplot.gnuplot > vplot.png
    ```

    - This command will process the `mapped.bed.gz` file, generate a TSV file with fragment information, and output a `vplot.png` showing the V-Plot.

## Output

- **vplot.png**: A 3D scatter plot showing the relationship between fragment length and relative position around the midpoint.
- **vplot_data.tsv**: A tab-separated file containing the relative positions, fragment lengths, and counts used to generate the plot.

