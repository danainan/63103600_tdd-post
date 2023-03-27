from function import inputt,display_compensation,validate_number
import pytest


@pytest.mark.code
def test_validate_number():
    assert validate_number(30,90,30) == True

#day มากกว่า 30
@pytest.mark.code
def test_display_compensation_day_morethan_30():
    assert display_compensation(31,0,0) == False

#day น้อยกว่า 0
@pytest.mark.code
def test_display_compensation_day_lessthan_1():
    assert display_compensation(-1,0,0) == False

#ot มากกว่า 3 เท่าของ วันทำงานใน 1 วัน
@pytest.mark.code
def test_display_compensation_ot_morethan_3():
    assert display_compensation(1,4,0) == False

#ot น้อยกว่า 0
@pytest.mark.code
def test_display_compensation_ot_lessthan_0():
    assert display_compensation(0,-1,0) == False

#late มากกว่า วันทำงาน
@pytest.mark.code
def test_display_compensation_late_morethan_day():
    assert display_compensation(1,0,2) == False
    
    
#late น้อยกว่า 0
@pytest.mark.code
def test_display_compensation_late_lessthan_0():
    assert display_compensation(0,0,-1) == False
    
@pytest.mark.code
def test_display_compensation_string():
    assert display_compensation(a,a,a) == False
 
