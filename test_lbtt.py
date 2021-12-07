from tax_calc import lbtt
from tax_calc_2 import lbtt2

def test_compare():
    for i in range(1, 1000000):
        assert lbtt(i) == lbtt2(i), "Value" + str(i) 

def test_in_first_band():
    assert lbtt(100000) == 0

def test_first_band_upper_limit():
    assert lbtt(145000) == 0

def test_second_band_lower_limit():
    assert lbtt(145001) == 0

def test_second_band_lowest_non_zero_result():
    assert lbtt(145050) == 1

def test_in_second_band():
    assert lbtt(150000) == 100

def test_second_band_upper_limit():
    assert lbtt(250000) == 2100

def test_third_band_lower_limit():
    assert lbtt(250001) == 2100

def test_in_third_band():
    assert lbtt(275000) == 3350

def test_third_band_upper_limit():
    assert lbtt(325000) == 5850

def test_fourth_band_lower_limit():
    assert lbtt(325001) == 5850

def test_in_fourth_band():
    assert lbtt(500000) == 23350

def test_fourth_band_upper_limit():
    assert lbtt(750000) == 48350

def test_fifth_band_lower_limit():
    assert lbtt(750001) == 48350

def test_fifth_band_1():
    assert lbtt(845289) == 59784

def test_fifth_band_2():
    assert lbtt(942356) == 71432

def test_fifth_band_3():
    assert lbtt(19865422) == 2342200