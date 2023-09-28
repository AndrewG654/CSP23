# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
colors = ["pink", "blue", "red", "purple", "black", "green", "yellow", "orange"]
size = [.1, .5, 1, 1.5, 2, 3, 5, 10]
spot_size = rand.choice(size)
spot_color = rand.choice(colors)
score = 0
font_setup = "Arial", 20, "normal"
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape("circle")
spot.shapesize(2)

spot.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,100)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-40,-200)

#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    

def update_score():
  score_writer.clear()
  global score
  score = score + 1
  score_writer.write(score, font=font_setup)
  

  
def change_position():
  spot_color = rand.choice(colors)
  spot.fillcolor(spot_color)
  spot_size = rand.choice(size)
  spot.shapesize(spot_size)
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)
  update_score()

  
def spot_clicked(x,y):
  if(timer_up == False):
    change_position()
  if(timer_up == True):
    spot.hideturtle()
    spot.goto(1000,0)
  
  # Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
    
  
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("aqua")
wn.ontimer(countdown, counter_interval) 

wn.mainloop()