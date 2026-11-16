
import os

import yaml

from jinja2 import Environment, FileSystemLoader





def generate_config(template, data_dict):

    """Генерирует конфигурацию на основе шаблона Jinja2.



    template — путь к файлу с шаблоном (например, "templates/for.txt"),

    data_dict — словарь со значениями, которые надо подставить в шаблон.

    Возвращает строку с сгенерированной конфигурацией.

    """

    template_dir, template_name = os.path.split(template)

    env = Environment(

        loader=FileSystemLoader(template_dir or "."),

        keep_trailing_newline=True,

    )

    tmpl = env.get_template(template_name)

    return tmpl.render(**data_dict)





if __name__ == "__main__":

    data_file = "data_files/for.yml"

    template_file = "templates/for.txt"

    with open(data_file) as f:

        data = yaml.safe_load(f)

    print(generate_config(template_file, data))

