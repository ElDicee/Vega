from App.Desktop.Win.Code.integrations import VegaAPI as api

import wikipedia as wiki


def search_articles(keyworkds: str, results: int):
    return wiki.search(keyworkds, results=results)


def get_summary(keywords: str):
    return wiki.summary(keywords)


def set_language(chars: str):
    wiki.set_lang(chars)


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Wikipedia")
    vega.add_method(api.Method(search_articles, api.OPERATOR, outputs={"Articles": None}, event=False,
                               formal_name="Search Articles"))
    vega.add_method(api.Method(set_language, api.EXECUTION, event=False, formal_name="Set Language"))
    vega.add_method(
        api.Method(get_summary, api.OPERATOR, outputs={"Summary": None}, event=False, formal_name="Summary"))
    return vega


if __name__ == "__main__":
    wiki.set_lang("es")
    print(wiki.search("Python"))