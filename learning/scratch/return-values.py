def link_width(current_link, max_link):
    percent= (current_link/max_link) * 100
    return percent

percentage = link_width(8,16)
print(percentage,"%")