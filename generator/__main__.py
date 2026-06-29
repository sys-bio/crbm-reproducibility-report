import cement
import generator
from pathlib import Path
from .core import generate_report


def default_template_directory():
    """Return the repository template path relative to this package."""
    return str((Path(__file__).resolve().parents[1] / 'template'))


class BaseController(cement.Controller):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = ("CRBM Reproducibility Report generator <https://gitlab.com/crbm-reproducibility-reports/crbm-reproducibility-report>.")
        help = "crbm-generator"
        arguments = [
            (['-i', '--input'], dict(type=str,
                                     required=True,
                                     help='Path to JSON encoded input file describing the report.')),
            (['-t', '--template-directory'], dict(type=str,
                                                  default=default_template_directory(),
                                                  help='Path to the LaTeX template directory.')),
            (['-o', '--output-file'], dict(type=str,
                                            required=False,
                                            help='Name of the PDF file that will be generated (requires pdflatex).')),
            (['-l', '--pdftex-log'], dict(action='store_true',
                                          help='Dump the pdftex compilation log to the terminal.')),
            (['-v', '--version'], dict(action='version',
                                       version=generator.__version__)),
        ]

    @cement.ex(hide=True)
    def _default(self):
        args = self.app.pargs
        generate_report(args.input, args.template_directory, args.output_file, args.pdftex_log)

class App(cement.App):
    """ Command line application """
    class Meta:
        label = 'cbrm-generator'
        base_controller = 'base'
        handlers = [
            BaseController,
        ]


def main():
    with App() as app:
        app.run()


if __name__ == "__main__":
    main()
