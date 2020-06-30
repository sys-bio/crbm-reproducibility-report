import sys
import os.path
from .ReportGenerator import ReportGenerator

__all__ = ['generate_report']



def generate_report(input_file, template_directory, output_directory):
    """ Generate the given reproducibility report from the given input file, saving output files to the output directory.

    Args:
        input_file (:obj:`str`): path to JSON document describing the report
        template_directory (:obj:`str`): directory to the LaTeX template directory
        output_directory (:obj:`str`): directory to store the outputs of the report generation
    """
    print("Generating the CRBM Reproducibility Report from: " + input_file +
          "; with output stored in the directory: " + output_directory)

    generator = ReportGenerator(template_directory)
    template = generator.get_template("template.tex")
    logo_image_path = os.path.join(template_directory, "figures", "CRBM-logo.png")
    rendered_tex = template.render(title="Title goes here",
                                   logo_image=os.path.abspath(logo_image_path).replace('\\', '/'),
                                   journal="PLoS Computational Biology",
                                   journal_submission_id="PCOMPBIOL-D-20-1234",
                                   curation_outcome_summary="This is awesome and short.",
                                   summary_comments="This would be a longer bit of text.")
    #print(rendered_tex)
    generator.compile_tex(rendered_tex, "bob.pdf")

