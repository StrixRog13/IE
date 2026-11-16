# -*- coding: utf-8 -*-
"""
Задание 20.2

Создать шаблон templates/cisco_router_base.txt.

В шаблон templates/cisco_router_base.txt должно быть включено содержимое шаблонов:
* templates/cisco_base.txt
* templates/alias.txt
* templates/eem_int_desc.txt

При этом, нельзя копировать текст шаблонов.

Проверьте шаблон templates/cisco_router_base.txt, с помощью
функции generate_config из задания 20.1. Не копируйте код функции generate_config.

В качестве данных, используйте информацию из файла data_files/router_info.yml

"""

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
