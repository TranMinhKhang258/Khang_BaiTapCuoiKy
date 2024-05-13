class HanoiTower:
    def move_disk(self, start, end):
        print("Move disk from Tower", start, "to Tower", end)

    def move_tower(self, height, start, end, intermediate):
        if height >= 1:
            self.move_tower(height - 1, start, intermediate, end)
            self.move_disk(start, end)
            self.move_tower(height - 1, intermediate, end, start)

hanoi = HanoiTower()
height = 3 
start_pos = 1 
end_pos = 3  
intermediate_pos = 2  

print("Di chuyển tháp Hanoi:")
hanoi.move_tower(height, start_pos, end_pos, intermediate_pos)
