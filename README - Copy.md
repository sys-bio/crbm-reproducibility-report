# crbm-reproducibility-report

Python script to generate a CRBM report from a LaTeX template using Jinja2.

## Installation

1. Make a Python virtual environment in the usual way
2. Clone this repository
3. `pip install -r requirements.txt`

If wanting to generate PDFs then `pdflatex` will also need to be available.

## Using

```
(venv) $> python crbm-generator.py --help
```

To generate an example report LaTeX when in the root folder of the cloned repository:

```
(venv) $> python crbm-generator.py -i example-report.json
```

To generate an example report and compile to PDF, when in the root folder of the cloned repository (requires `pdflatex` to be available):

```
(venv) $> python crbm-generator.py -i example-report.json -o example.pdf
```

To generate the example report LaTeX outside the root folder of the cloned repository:

```
(venv) $> python path/to/crbm-reproducibility-report/crbm-generator.py -i path/to/crbm-reproducibility-report/example-report.json -t path/to/crbm-reproducibility-report/template
```

## Report description file

JSON file containing the information required for the report. See `example-report.json` for an example.


## Overleaf
Blank Overleaf template of v 1.3 available at https://www.overleaf.com/read/htfphvrdgfsb#360fd0


## Documentation 

Documentation for v 1.3 is available at https://docs.google.com/spreadsheets/d/1NFApGabBi3ZtP328lVAYsy0dCcfHoXfnvjzz7Byl3Mk/edit?usp=sharing

