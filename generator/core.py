import sys
import json
import os.path
from .ReportGenerator import ReportGenerator

__all__ = ['generate_report']



def generate_report(input_file, template_directory, output_file, compilation_log):
    """ Generate the given reproducibility report from the given input file, saving generated PDF to the output file.

    Args:
        input_file (:obj:`str`): path to JSON document describing the report
        template_directory (:obj:`str`): directory to the LaTeX template directory
        output_file (:obj:`str`): filename to save the generated PDF report to, if required
        compilation_log (:obj:`bool`): print pdftex compilation log to terminal if true
    """
    msg = 'Generating the CRBM Reproducibility Report from: {}'.format(input_file)
    if output_file is None:
        msg += '; generating LaTeX to the console.'
    else:
        msg += '; with generated report saved to: {}'.format(output_file)
    print(msg)

    # load the input file
    report_description = {}
    with open(input_file, "r") as read_file:
        report_description = json.load(read_file)
    # need to add in the logo for our template
    logo_image_path = os.path.join(template_directory, "figures", "CRBM-logo.png")
    report_description["logo_image"] = os.path.abspath(logo_image_path).replace('\\', '/')

    # create a generator that can locate our template directory
    generator = ReportGenerator(template_directory)

    # preprocess our report description
    generator.process_report_description(report_description)

    # and fetch the report template
    template = generator.get_template("template.tex")

    # process the template using the information from the input file
    rendered_tex = template.render(report_description)
    #print(rendered_tex)

    # if an output PDF file is provided, compile the rendered LaTeX into a PDF...
    if output_file is None:
        print(rendered_tex)
    else:
        generator.compile_tex(rendered_tex, output_file, compilation_log)

