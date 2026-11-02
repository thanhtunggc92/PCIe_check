def component_value():
    Fan_RPM= 4000

    return Fan_RPM

def fan_speed_list(fan_list):
    new_fan_list=[]
    for i in fan_list:
        if i > 3000:
            new_fan_list.append(i)
    return len(new_fan_list)


def test_fan_rpm():
    assert component_value() == 4000


def test_fan_num():
    assert fan_speed_list([2000,4000,1000]) == 2