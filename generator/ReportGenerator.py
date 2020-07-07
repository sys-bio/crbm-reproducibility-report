import os
import jinja2
from subprocess import Popen, PIPE
import tempfile
import shutil


def texify(cond):
    tex = '\\absent'
    if cond:
        tex = '\\present'
    return tex


class ReportGenerator:

    def __init__(self, template_directory):
        self._latex_jinja_env = jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(template_directory)
        )

    def print_template(self, template_filename):
        print(self._latex_jinja_env.loader.get_source(self._latex_jinja_env, template_filename)[0])

    def get_template(self, template_filename):
        return self._latex_jinja_env.get_template(template_filename)

    def process_report_description(self, report_description):
        """turn the detailed rubric into an array of \present or \absent values for the template to use

        :param report_description:
        :return:
        """
        encoded_rubric = []
        rubric = report_description['rubric']
        reproducibility_criteria = rubric['reproducibility_criteria']

        pcode = reproducibility_criteria['procedural_code']
        dcode = reproducibility_criteria['declarative_code']
        encoded_rubric.append(texify(pcode['present'] or dcode['present']))

        encoded_rubric.append(texify(pcode['present']))
        encoded_rubric.append(texify(pcode['compilation_documentation']))
        encoded_rubric.append(texify(pcode['execution_documentation']))
        encoded_rubric.append(texify(pcode['boundary_conditions']))
        encoded_rubric.append(texify(pcode['postprocessing_documentation']))

        encoded_rubric.append(texify(dcode['present']))
        encoded_rubric.append(texify(dcode['algorithms_documented']))
        encoded_rubric.append(texify(dcode['algorithms_parameterised']))
        encoded_rubric.append(texify(dcode['postprocessing_documentation']))

        exe = reproducibility_criteria['executable_implementation']
        encoded_rubric.append(texify(exe['present']))
        encoded_rubric.append(texify(exe['executable']))
        encoded_rubric.append(texify(exe['simulations_documented']))

        math = reproducibility_criteria['mathematical_description']
        encoded_rubric.append(texify(math['present']))
        encoded_rubric.append(texify(math['equations']))
        encoded_rubric.append(texify(math['parameters']))
        encoded_rubric.append(texify(math['boundary_conditions']))
        encoded_rubric.append(texify(math['machine_parameters']))
        encoded_rubric.append(texify(math['machine_boundary_conditions']))

        sed = reproducibility_criteria['simulation_experiments']
        encoded_rubric.append(texify(sed['present']))
        encoded_rubric.append(texify(sed['integration_algorithm']))
        encoded_rubric.append(texify(sed['stochastic_algorithm']))
        encoded_rubric.append(texify(sed['random_number_generator']))
        encoded_rubric.append(texify(sed['parameter_estimation_algorithm']))
        encoded_rubric.append(texify(sed['simulation_execution_documentation']))

        report_description['_er'] = encoded_rubric

    def compile_tex(self, rendered_tex, out_pdf_path, print_log):
        tmp_dir = tempfile.mkdtemp()
        in_tmp_path = os.path.join(tmp_dir, 'rendered.tex')
        with open(in_tmp_path, 'w') as outfile:
            outfile.write(rendered_tex)
        out_tmp_path = os.path.join(tmp_dir, 'out.pdf')
        p = Popen(['pdflatex', '-jobname', 'out', '-output-directory', tmp_dir, in_tmp_path], stdout=PIPE, stderr=PIPE)
        [stdout, stderr] = p.communicate()
        if print_log:
            print("pdftex stdout:\n==============\n")
            print(stdout.decode('utf-8'))
            print("\npdftex stderr:\n==============\n")
            print(stderr.decode('utf-8'))
        shutil.copy(out_tmp_path, out_pdf_path)
        shutil.rmtree(tmp_dir)
