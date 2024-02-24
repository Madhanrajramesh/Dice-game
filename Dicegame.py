# import modules 

import turtle 

import random 

  
# creating the screen 

d = turtle.Screen() 

d.setup(width=300, height=300) 

d.bgcolor('white') 

d.title('Dice Play') 

d.tracer(1) 

  
# creating the dots 

dot_positions = [[(0, 0, 'red'), (-100, 100, 'white'), (-100, 0, 'white'), (-100, -100, 'white'), (100, 100, 'white'), 

                  (100, 0, 'white'), (100, -100, 'white')], 

  

                 [(0, 0, 'white'), (-100, 100, 'red'), (-100, 0, 'white'), (-100, -100, 'white'), (100, 100, 'white'), (100, 0, 'white'), 

                  (100, -100, 'red')], 

  

                 [(0, 0, 'red'), (-100, 100, 'red'), (-100, 0, 'white'), (-100, -100, 'white'), (100, 100, 'white'), (100, 0, 'white'), 

                  (100, -100, 'red')], 

  

                 [(0, 0, 'white'), (-100, 100, 'red'), (-100, 0, 'white'), (-100, -100, 'red'), (100, 100, 'red'), (100, 0, 'white'), (100, -

                                                                                                                                       100, 'red')], 

  

                 [(0, 0, 'red'), (-100, 100, 'red'), (-100, 0, 'white'), (-100, -100, 'red'), (100, 100, 'red'), (100, 0, 'white'), (100, -

                                                                                                                                     100, 'red')], 

  

                 [(0, 0, 'white'), (-100, 100, 'red'), (-100, 0, 'red'), (-100, -100, 'red'), (100, 100, 'red'), (100, 0, 'red'), (100, -

                                                                                                                                   100, 'red')]] 

  

  

dot = [turtle.Turtle() for _ in range(7)] 

  

  

def click(): 

  # generating random number 

    num = random.randint(1, 6) 

  

    print(f" The number rolled on dice is {num}\n ") 

    for i in range(7): 

        dot[i].shape('circle') 

        dot[i].color(dot_positions[num-1][i][2]) 

        dot[i].penup() 

        dot[i].goto(dot_positions[num-1][i][0], dot_positions[num-1][i][1]) 

        dot[i].dot() 

  

  
d.listen() 

d.onkeypress(click, 'space') 
d.mainloop() 
