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
                                                  default='.',
                                                  help='Path to the LaTeX template directory.')),
            (['-o', '--output-directory'], dict(type=str,
                                                default='.',
                                                help='Directory to save generated report files.')),
            (['-v', '--version'], dict(action='version',
                                       version=generator.__version__)),
        ]

    @cement.ex(hide=True)
    def _default(self):
        args = self.app.pargs
        generate_report(args.input, args.template_directory, args.output_directory)

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
