from data.preprocess import clean_text, preprocess_record


def test_clean_text():
    text = "  Hello   world\n\nTest\ttext  "

    result = clean_text(text)

    assert result == "Hello world Test text"


def test_clean_text_non_string():
    assert clean_text(None) == ""
    assert clean_text(123) == ""


def test_preprocess_record():
    record = {
        "query_id": "123",
        "query": "  भारत में   क्या है? ",
        "Answer": "  यह एक उत्तर है।\n",
    }

    result = preprocess_record(record)

    assert result is not None
    assert result["query_id"] == "123"
    assert result["query"] == "भारत में क्या है?"
    assert result["answer"] == "यह एक उत्तर है।"


def test_empty_record_is_ignored():
    record = {
        "query_id": "123",
        "query": "   ",
        "Answer": "",
    }

    assert preprocess_record(record) is None