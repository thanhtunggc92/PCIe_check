from pcie_check import find_bus_ids



with open ("samples/lspci_laptop.txt") as f:
    lspci = f.read()

devices = lspci.splitlines()
# test_result=[]
# for i in devices:
#     if "bridge" in i.lower():
#         line= i.split()
#         test_result.append(line[0])
# print(test_result)

bus_id=['00:00.0', '00:06.0', '00:1c.0', '00:1c.7', '00:1f.0']

def test_pcie_link ():

    assert find_bus_ids("bridge",devices) == bus_id