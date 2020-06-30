import os
import jinja2
from subprocess import Popen
import tempfile
import shutil


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

    def compile_tex(self, rendered_tex, out_pdf_path):
        tmp_dir = tempfile.mkdtemp()
        in_tmp_path = os.path.join(tmp_dir, 'rendered.tex')
        with open(in_tmp_path, 'w') as outfile:
            outfile.write(rendered_tex)
        out_tmp_path = os.path.join(tmp_dir, 'out.pdf')
        p = Popen(['pdflatex', '-jobname', 'out', '-output-directory', tmp_dir, in_tmp_path])
        p.communicate()
        shutil.copy(out_tmp_path, out_pdf_path)
        shutil.rmtree(tmp_dir)
