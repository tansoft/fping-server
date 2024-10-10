import ipaddress
import csv

def ip_range_to_cidr(start_ip, end_ip):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)

    subnet = ipaddress.ip_network(f'{start}/{32}', strict=False)
    subnets = []

    while subnet.broadcast_address <= end:
        subnet_mask = subnet.prefixlen
        subnets.append(str(subnet))

        if subnet.broadcast_address == end:
            break

        subnet = ipaddress.ip_network(f'{subnet.broadcast_address + 1}/{32}', strict=False)

    return subnets

# 打开CSV文件
with open('iprange.csv', 'r') as file:
    # 创建一个CSV阅读器对象
    reader = csv.DictReader(file)

    # 遍历每一行数据
    for row in reader:
        # 处理每一行数据
        cidr = ipaddress.summarize_address_range(ipaddress.IPv4Address(row['start_ip']), ipaddress.IPv4Address(row['end_ip']))
        print(row['start_ip'], row['end_ip'], '[' + ', '.join(str(item) for item in cidr) + ']')
