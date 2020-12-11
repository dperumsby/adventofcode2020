class SeatingSimulation:
    """ Used to predict the best place to sit, given a seating layout """

    def __init__(self):
        self.layout = []
        self.max_i = 0
        self.max_j = 0
        self.state_changed = 1 # a flag for checking if the state has changed from one iteration to the next
        
    def load_layout(self, file_name):
        with open(file_name, "r") as file:
            layout = file.read().splitlines()
        self.layout = layout
        self.max_i = len(self.layout) - 1
        self.max_j = len(self.layout[0]) - 1
        self.state_changed = 1

    def determine_seat_state(self, pos, curr_state, part2=False):
        i, j = pos
        adjacent = []
        deltas = [(-1,0), (1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

        if part2:
            tolerance = 5
            for dx, dy in deltas:
                m = 1
                while 0 <= i + m*dy <= self.max_i and 0 <= j + m*dx <= self.max_j:
                    looking_at = self.layout[i+m*dy][j+m*dx]
                    if looking_at in ["L", "#"]:
                        adjacent.append(looking_at)
                        break       
                    m += 1
        else:
            tolerance = 4
            for dx, dy in deltas:
                if 0 <= i + dy <= self.max_i and 0 <= j + dx <= self.max_j:
                    adjacent.append(self.layout[i+dy][j+dx])

        if curr_state == "L" and not "#" in adjacent:
            self.state_changed = 1
            return "#"
        elif curr_state == "#" and adjacent.count("#") >= tolerance:
            self.state_changed = 1
            return "L"
        else:
            return curr_state

    def determine_layout_state(self, part2=False):
        self.state_changed = 0
        new_layout = self.layout.copy()

        for i in range(0, self.max_i + 1):
            curr_row = list(new_layout[i])
            for j in range(0, self.max_j + 1):
                curr_state = self.layout[i][j]
                new_state = self.determine_seat_state((i, j), curr_state, part2)
                curr_row[j] = new_state
            new_layout[i] = "".join(curr_row)

        self.layout = new_layout
        return new_layout

    def find_stable_layout(self, part2=False):
        while self.state_changed:
            self.determine_layout_state(part2)
        return self.layout

    def num_occupied(self):
        total = 0

        for i in range(self.max_i + 1):
            total += self.layout[i].count("#")
        return total


ferry = SeatingSimulation()
ferry.load_layout("input.txt")
ferry.find_stable_layout()
print(ferry.num_occupied()) # 2263

ferry.load_layout("input.txt")
ferry.find_stable_layout(part2=True)
print(ferry.num_occupied()) # 2002
