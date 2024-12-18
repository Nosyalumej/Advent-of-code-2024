import logging

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
input_file = 'input.txt'
left = []
right = []
seperator = '   '
with open(input_file) as f:
    for line in f:
        left.append(line.split(seperator)[0])
        right.append(line.split(seperator)[1].strip('\n'))

left = sorted(list(map(int, left)))
right = sorted(list(map(int,right)))

total_distance = sum(abs(l - r) for l, r in zip(left, right))
logging.debug(f"TOTAL DISTANCE {total_distance}")