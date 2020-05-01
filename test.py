import bowling

# test throw_ball
print("\ntesting throw_ball")
res = bowling.throw_ball(0)
bowling.throw_ball(res)

# test calculate_score
print("\ntesting calculate_score")
hit_pins_by_frame = [
    [1,4],
    [4,5],
    [6,4],
    [5,5],
    [10],
    [0,1],
    [7,3],
    [6,4],
    [10],
    [2,8,6],
]

# run through the calculate_score

game_score = []

for idx_frame, frame in enumerate(hit_pins_by_frame):
    
    for idx_roll, hit_pins in enumerate(frame):

        game_score, bonus = bowling.calculate_score(game_score, idx_frame + 1, idx_roll + 1, hit_pins)

for x in game_score:

    print("\n",x)
    



