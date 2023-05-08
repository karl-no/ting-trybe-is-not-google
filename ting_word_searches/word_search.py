def exists_word(word, instance):
    list_of_words = []

    for data in instance._data:
        for line in range(len(data["linhas_do_arquivo"])):
            if word.lower() in data["linhas_do_arquivo"][line].lower():
                list_of_words.append({"linha": line + 1})

        if len(list_of_words):
            return [{
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": list_of_words
                }]

        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
