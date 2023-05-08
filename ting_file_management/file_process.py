import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    for data in instance._data:
        if data["nome_do_arquivo"] == path_file:
            return False

    instance.enqueue(processed_data)

    return sys.stdout.write(str(processed_data))


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        path_file = file["nome_do_arquivo"]
        return sys.stdout.write(str(
            f"Arquivo {path_file} removido com sucesso\n"
        ))
    return sys.stdout.write(str("Não há elementos\n"))


def file_metadata(instance, position):
    try:
        return sys.stdout.write(f"{instance.search(position)}")
    except IndexError:
        return sys.stderr.write("Posição inválida")
