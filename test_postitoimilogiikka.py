import postinumerot

TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}


def test_postitoimilogiikka1():
    tulos = postinumerot.ryhmittele_toimipaikoittain(TOIMIPAIKAT)
    assert tulos['MUURUVESI'] == ['73460']


def test_postitoimilogiikka2():
    tulos = postinumerot.ryhmittele_toimipaikoittain(TOIMIPAIKAT)
    assert tulos['KIURUVESI'] == ['74701', '74700']
