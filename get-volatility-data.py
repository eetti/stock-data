import requests
import time

page = requests.get('http://www.optionstrategist.com/calculators/free-volatility-data')
data_lines = page.text.split('\n')[177:4905]
data_lines = data_lines[0:998] + data_lines[1003:2002] + data_lines[2007:3006] + data_lines[3011:4010] + data_lines[4015:]
data_lines = [line for line in data_lines if 'SERIAL' not in line]
data_array = [line.replace('/ ', ' ').replace('%ile', '').split() for line in data_lines]
for line in data_array:
    line[4] = line[4][0:2] + '-' + line[4][2:4] + '-' + line[4][4:]
data_lines_comma = [','.join(row) for row in data_array]

header = "Symbol,hv20,hv50,hv100,date,iv,days_calculated,percentile,close\n"
csv = header + '\n'.join(data_lines_comma)
current_date = time.strftime("%d_%m_%Y")
filename = 'volatility_{}.csv'.format(current_date)
print(csv)
with open(filename, 'w') as f:
    f.write(csv)

