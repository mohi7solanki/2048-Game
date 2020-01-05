import random


dir_code = {
	'UP': (1,0),
	'DOWN': (-1,0),
	'LEFT': (0,1),
	'RIGHT': (0,-1)
}




SCORE = 0


def merge(array):
	global SCORE
	output = [i for i in array if i != 0]
	for i in range(len(output)-1):
		pair = output[i:i+2]
		if pair[0] == pair[1]:
			sum_of_pair = pair[0] + pair[1]
			output[i] = sum_of_pair
			SCORE += sum_of_pair
			del output[i+1]
			output.append(0)
	diff = len(array) - len(output)
	output = output + [0] * diff
	return output


def iterate(start_point, direction, steps):
    output = []
    for step in range(steps):
        row = start_point[0] + direction[0] * step
        col = start_point[1] + direction[1] * step
        output.append((row,col))
    return output


class TwentyFortyEight:
	
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.reset()
		self.first_dir = {}
		self.first_dir['UP'] = [(0,i) for i in range(self.column)]
		self.first_dir['DOWN'] = [(self.row-1,i) for i in range(self.column)]
		self.first_dir['LEFT'] = [(i,0) for i in range(self.row)]
		self.first_dir['RIGHT'] = [(i,self.column-1) for i in range(self.row)]

	def __str__(self):
		board = ''
		for row in self.GRID:
			board += str(row) + '\n'
		return board

	def reset(self):
		self.GRID = [[0 for i in range(self.column)] for j in range(self.row)]
		self.make_new_cell(initial=True)

	def make_new_cell(self, initial=False):
		tiles = [2] * 9 + [4]
		if initial:
			rows = random.sample(range(self.row), 2)
			columns = random.sample(range(self.column), 2)
			x1, x2 = rows
			y1, y2 = columns
			self.GRID[x1][y1] = random.choice(tiles)
			self.GRID[x2][y2] = random.choice(tiles)
		else:
			while True:
				row = random.randint(0,self.row-1)
				column = random.randint(0,self.column-1)
				if self.GRID[row][column] == 0:
					self.GRID[row][column] = random.choice(tiles)
					break
				else:
					continue

	def move(self,direction):
		initial_GRID = [row[:] for row in self.GRID]
		indices = self.first_dir[direction]
		for index in indices:
			array_indices = iterate(index, dir_code[direction], self.row)
			array_to_be_merged = []
			for row, col in array_indices:
				array_to_be_merged.append(self.GRID[row][col])
			merged_array = merge(array_to_be_merged)
			for index, i in zip(array_indices,range(len(merged_array))):
				row, col = index
				self.GRID[row][col] = merged_array[i]
		if self.GRID != initial_GRID:
			self.make_new_cell()



if __name__ == '__main__':
	game = TwentyFortyEight(4,4)
	while True:
		print(f'SCORE: {SCORE}')
		print(game)
		move = input('Enter the move: ')
		game.move(move)
		print('')
