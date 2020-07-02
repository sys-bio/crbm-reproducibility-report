# crbm-reproducibility-report

Python script to generate a CRBM report from a LaTeX template using Jinja2.

## Installation

1. Make a Python virtual environment in the usual way
2. Clone this repository
3. `pip install -r requirements.txt`

## Using

```
(venv) $> python crbm-generator.py --help
```

To generate example report when in the root folder of the cloned repository:

```
(venv) $> python crbm-generator.py -i example-report.json -o example.pdf
```

To generate the example report outside the root folder of the cloned repository:

```
(venv) $> python path/to/crbm-reproducibility-report/crbm-generator.py -i path/to/crbm-reproducibility-report/example-report.json -t path/to/crbm-reproducibility-report/template
```

## Report description file

JSON file containing the information required for the report. See `example-report.json` for an example.