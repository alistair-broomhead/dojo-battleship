import random

VALID = {'h', 'm', 's'}


def get_random_pos():
	return random.choice("ABCDEFGHIJ")+str(random.randint(1,10))

def get_position_from_grid(grid, last_hit):
	if last_hit is None:
		return None, get_random_pos()
	
	column, *row = last_hit
	row = int(''.join(row))

	for i in [-1, 0, 1]:
		col = chr(ord(column) + i)
		if not 'A' <= col <= 'J':
			continue
		for j in [-1, 0, 1]:
			row_ = row + j
			if not row_ in range(1, 10):
				continue
			pos = col + str(row_)
			if pos not in grid:
				return last_hit, pos

	return None, get_random_pos()

def main():
	grid = {}
	sunk = 0
	last_hit = None
	while sunk < 10:
		last_hit, pos = get_position_from_grid(grid, last_hit)
		if pos in grid:
			continue
		print(pos)
		answer = input().strip().lower()
		assert answer in VALID, "'{}' is not a valid answer, expected {}".format(
			answer, VALID)
		if answer == 's':
			sunk += 1
		if answer == 'h':
			last_hit = pos

		grid[pos] = answer




if __name__ == "__main__":
	main()