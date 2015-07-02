import random

VALID = {'h', 'm', 's'}


def get_random_pos():
	return random.choice("ABCDEFGHIJ")+str(random.randint(1,10))

def get_position_from_grid(grid, last_hit):
	if last_hit is None:
		return get_random_pos()
	return get_random_pos()

def main():
	grid = {}
	sunk = 0
	last_hit = None
	while sunk < 10:
		pos = get_position_from_grid(grid, last_hit)
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