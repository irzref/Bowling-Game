import random
import sys



def throw_ball(num_hit_pins):

    print("throwing ball ...")

    max_pins = 10 - num_hit_pins

    hit_pins = random.randint(0, max_pins)

    print("you hit", hit_pins)

    return hit_pins



def calculate_score(game_score, frame, roll, hit_pins):

    print("calculating ...")

    if frame > 10 :
        
        print("error maximum frame is 10")
        
        return game_score

    if frame != 10  and roll > 2 :
        
        print("error maximum roll per frame is 2 except 10th frame")
        
        return game_score        

    if frame == 10  and roll > 3 :
        
        print("error maximum roll in 10th frame is 3")
        
        return game_score



    # calculating score of current frame

    current_frame = frame - 1
    bonus = ""

    if roll == 1 :

        frame_dict = {
            'pins_by_roll' : [],
            'total_pins' : 0,
            'bonus' : "",
            'bonus_point' : 0,
            'frame_total_point' : 0,
            'game_total_point_until_this_frame' : 0
        }

        game_score.append(frame_dict)

        if hit_pins == 10 :

            bonus = "STRIKE"

    elif roll == 2 :

         if (game_score[ current_frame ]["total_pins"] + hit_pins) == 10 :

             bonus = "SPARE"



    game_score[ current_frame ]["pins_by_roll"].append(hit_pins)
    game_score[ current_frame ]["total_pins"] = sum(game_score[ current_frame ]["pins_by_roll"])
    game_score[ current_frame ]["frame_total_point"] = game_score[ current_frame ]["total_pins"]
    
    if bonus != "" : game_score[ current_frame ]["bonus"] = bonus



    # adding bonus to previous frame

    if frame != 1 :

        previous_frame = frame - 2

        if game_score[previous_frame]["bonus"] == "STRIKE" and roll < 3:

            game_score[previous_frame]["bonus_point"] += hit_pins

        if game_score[previous_frame]["bonus"] == "SPARE" and roll == 1 :

            game_score[previous_frame]["bonus_point"] += hit_pins

        game_score[previous_frame]["frame_total_point"] = game_score[previous_frame]["total_pins"] + game_score[previous_frame]["bonus_point"]

        game_score[ current_frame ]["game_total_point_until_this_frame"] = sum(frame_score['frame_total_point'] for frame_score in game_score) 

        game_score[previous_frame]["game_total_point_until_this_frame"] = game_score[ current_frame ]["game_total_point_until_this_frame"] - game_score[ current_frame ]["frame_total_point"]



    return game_score, bonus



def get_input(input_hit_pins_setting, input_message, hit_pins):

    if input_hit_pins_setting == "M" :

        additional_message = ", the number of available pins is " + str(10 - hit_pins)

        user_input = input(input_message + additional_message + " \n")

        try:

            hit_pins_input = int(user_input)                     

        except ValueError:
            
            print("Error parsing user input to integer")

            print("abort game")

            sys.exit()
        
        if hit_pins_input > 10 :

            print("The input hit pins is more than available pins")

            print("abort game")

            sys.exit()

        elif hit_pins != 0 and hit_pins_input > ( 10 - hit_pins ) :

            print("The input hit pins is more than available pins")

            print("abort game")

            sys.exit()
                                        
    elif input_hit_pins_setting == "R" :

        user_input = input(input_message + " \n")

        hit_pins_input = throw_ball(hit_pins)      



    return hit_pins_input



def game_play(input_hit_pins_setting, input_message):
    
    print("\ngame starts now")

    game_score = []
    strike = 0
    spare = 0

    for frame in range(10):
        
        hit_pins = 0        

        for roll in range(2):                

            print("\nyou play frame {0} roll {1}".format(frame + 1, roll + 1))

            hit_pins_input = get_input(input_hit_pins_setting, input_message, hit_pins)

            game_score, bonus = calculate_score(game_score, frame + 1, roll + 1, hit_pins_input)
            hit_pins += hit_pins_input

            if frame != 0 : print("previous frame score", game_score[frame - 1])
            print("current frame score", game_score[frame])

            if bonus == "STRIKE" :

                strike += 1

                break

            if bonus == "SPARE" :

                spare += 1

        if (frame + 1) == 10 and ( strike > 0 or spare > 0 ) :

            print("\nyou get extra roll")

            hit_pins = 0            

            hit_pins_input = get_input(input_hit_pins_setting, input_message, hit_pins)

            game_score, bonus = calculate_score(game_score, frame + 1, 3, hit_pins_input)
            hit_pins += hit_pins_input

            print("previous frame score", game_score[frame - 1])
            print("current frame score", game_score[frame])

    print("\nend score")

    for x in game_score:

        print("\n", x)



def play() :

    user_input = input('press M to input the hit pins manually, press R to input hit pins randomly \n')
    
    input_hit_pins_setting = str(user_input)

    input_message = ""

    if input_hit_pins_setting == "M" :

        print("you will set the number of hit pins in each roll")

        input_message = "please input number of hit pins"
        
    elif input_hit_pins_setting == "R" :

        print("the number of hit pins will be set randomly, you will only need to press enter to throw the ball")

        input_message = "please press enter to throw ball"
    
    else :

        print("unknown input")

        print("abort game")

        sys.exit()

    game_play(input_hit_pins_setting, input_message)