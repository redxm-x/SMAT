import json


hostname = ''

if __name__ == '__main__':
    with open(f'{hostname}.json', 'r') as f:
        data = json.load(f)

    for x in data:
        if x['Hostname'] == hostname:
            json_system = x['System']
            json_NIC = x['Nic']
            json_hostname = x['Hostname']

    print(f'Machine name: {json_hostname}')
    print(f'Machine system: {json_system}')
    print(f'Machine NIC: {json_NIC}')
