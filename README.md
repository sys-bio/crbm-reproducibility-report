# CRBM Reproducibility Report

The authoritative source repository for the CRBM Reproducibility Report is: https://github.com/sys-bio/crbm-reproducibility-report.

This repository tracks the development of a "reproducibility report" developed at the [Center for Reproducibile Biomedical Modeling](https://reproduciblebiomodels.org/) (CRBM) and used to evaluate the reproducibility of computational models described in scientific articles. The report originated when the CRBM partnered with PLOS Computational Biology to launch a pilot peer review workflow to assess reproducibility [Papin et al (2020)](https://doi.org/10.1371/journal.pcbi.1007881). This report is also tightly integrated into articles published in the [*Physiome*](https://journal.physiomeproject.org/) journal.

An example report (as generated below) can be viewed here: [example.pdf](example.pdf).

In this repository we have a Python generator that uses a JSON report with the LaTeX template to produce a reproducibility report. Instructions on the installation and use of this generator is given below. Documentation describing the report's contents and criteria for evaluating the report rubric is available [here](documentation_table.md).

The report template and guidance for performing the reproducibility review evolve over time. The report template is therefore versioned and beginning with version 1.3 we make releases of this Github repository to archive the versions.

## Overleaf
Overleaf is a platform for collaborative editing of LaTeX documents. A blank Overleaf template of version 1.3 of this reproducibility report is available at: https://www.overleaf.com/read/htfphvrdgfsb#360fd0

## Python generator

In an effort to ease the generation of reproducibility reports, we have created a Python generator that uses the LaTeX template and a JSON configuration file to generate a reproducibility report. This may one day be used with a user interface to simplify the evaluation and production of these reproducibilty reports.

### Installation

1. Make a Python virtual environment in the usual way
2. Clone this repository
3. `pip install -r requirements.txt`

If wanting to generate PDFs then `pdflatex` will also need to be available.

### Using

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

### Report description file

JSON file containing the information required for the report. See [`example-report.json`](example-report.json) for an example.
