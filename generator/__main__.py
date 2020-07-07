import cement
import generator
from .core import generate_report


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
                                                  default='template',
                                                  help='Path to the LaTeX template directory.')),
            (['-o', '--output-file'], dict(type=str,
                                            required=True,
                                            help='Name of the PDF file that will be generated.')),
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


if __name__ == "__main__":
    with App() as app:
        app.run()
