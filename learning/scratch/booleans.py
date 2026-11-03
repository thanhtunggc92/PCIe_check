def link_speed_check(lspeed):
    return lspeed >=16


print(f"link_8_check:{link_speed_check(8)}")

print(f"link_16_check:{link_speed_check(16)}")

print(f"link_32_check:{link_speed_check(32)}")



def link_width_check(link, width):
    link_cap= 16
    link_cap_width = 4
    return (link < link_cap and width < link_cap_width)


print (f"checking 16 and 16 : {link_width_check(16,16)}")

print (f"checking 16 and 4 : { link_width_check(16,4)}")
print (f"checking 8 and 4 : { link_width_check(8,4)}")