from function import *
import pytest

@pytest.mark.display 
def test_display():
    assert display_compensation(0,0,0) == 0*340+0*60+((0-0)*1000)
    assert display_compensation(1,1,1) == 1*340+1*60+((1-1)*1000)
    assert display_compensation(30,30,30) == 30*340+30*60+((30-30)*1000)
    assert display_compensation(1,3,0) == 1*340+3*60+((1-0)*1000)
    #ทำงาน 30 วัน ไม่มาสาย 30 วัน ทำ OT 90 ชั่วโมง(ทุกวันวันละ 3 ชั่วโมง)
    assert display_compensation(30,90,30) == 30*340+90*60+((30-0)*1000)
