#  ### Written by Kenan Kamel A Alghythee ### 
## NetID: kalghy2, 
# UIC, Spring2022, Feb 23 
# Project2,par 2 
# Overview: This is what called presenation tier for 
# a database application that handles Movies and
# display s series of information that is needed 
# input from the user
# so it will be called  the 
# persenation tier, and it will has a serise of cmmands 
# and the user can pick one and input and recive 
# a respond based on the input 
# CS 341, Spring 2022


import objecttier
import sqlite3

## connecting the to the database 
dbConn = sqlite3.connect('MovieLens.db')

## this used to handle the frist command 
# it has a serise of if statment and call 
# the function of get_movies() and store the result
# in a variable and print it to the screen 
def command_one(dbConn,user_input):
  movies = objecttier.get_movies(dbConn, user_input)
  print()

  if (movies  == None):
    print("# of movies found: 0")
    return 
  elif(len(movies) > 100):
    print("# of movies found: " + str(len(movies)))
    print()
    print("There are too many movies to display, please narrow your search and try again...")
  else:
    
    print("# of movies found: " + str(len(movies)))
    print()
    for movie in movies:
      print(str(movie.Movie_ID) + " : " + str(movie.Title ) + " (" + str(movie.Release_Year) + ")" )

#######
## this used to handle the second command 
# it has a serise of if statment and call 
# the function of get_movie_details() and store the result
# in a variable and print it to the screen 
def command_two(dbConn,movie_id):
  movie_detials = objecttier.get_movie_details(dbConn, movie_id)
  print()
  if (movie_detials == None):
    print("No such movie...")
    return
  else:
    print(str(movie_detials.Movie_ID) + " : " + movie_detials.Title)
    print("  Release date: " + str(movie_detials.Release_Date))
    print("  Runtime: " + str(movie_detials.Runtime) + " (mins)")
    print("  Orig language: " + str(movie_detials.Original_Language))
    print("  Budget: $" + format(movie_detials.Budget,",") + " (USD)")
    print("  Revenue: $" + format(movie_detials.Revenue,",") + " (USD)")
    print("  Num reviews: " + str(movie_detials.Num_Reviews))
    print("  Avg rating: " + "{:0.2f}".format(movie_detials.Avg_Rating) + " (0..10)")
    print("  Genres: ",end = "")
    for p in movie_detials.Genres:
      print(p + ", ", end = "")
    print()
    print("  Production companies: ", end = "" )
    for p in movie_detials.Production_Companies:
      print(p + ", ", end = "")
    print()
    print("  Tagline: " + str(movie_detials.Tagline))


#################################################
## this used to handle the third command 
# it has a serise of if statment and call 
# the function of get_top_N_movies() and store the result
# in a variable and print it to the screen 
################################################
def command_three(dbConn,N_input):
  min_reviews = int(input("min number of reviews? "))
  
  if(min_reviews <=0):
    
    print("Please enter a positive value for min number of reviews...")
    return
  ## at this point everthing should be at it correct value 
  print()
  movies_rating = objecttier.get_top_N_movies(dbConn, int(N_input), int(min_reviews))
  
  if(movies_rating == None ):
    return 
  elif len(movies_rating) == 0:
    return 
    ## here we have at least one movie in returned 
      
  for movie in movies_rating:
    print(str(movie.Movie_ID) + " : " + movie.Title + " (" + movie.Release_Year + "), avg rating = " + "{:0.2f}".format(movie.Avg_Rating) + " (" + str(movie.Num_Reviews) + " reviews)" )


#################################################
## this used to handle the fourth command 
# it has a serise of if statment and call 
# the function of add_review() and determine
# if the user added the reivews correctly it
# is returned 1, else 0
################################################
def command_four(dbConn,review):
  id = int(input("Enter movie id: "))
  print()
  result = objecttier.add_review(dbConn, id, review)
  ## handel diffrent cases 
  if(result == 0):
    print("No such movie...")
  elif(result == 1):
    print("Review successfully inserted")
  return 


#################################################
## this used to handle the fifth command 
# it has a serise of if statment and call 
# the function of set_tagline() and determine
# if the user seted the tagline correctly it
# is returned 1, else 0
################################################
def command_five(dbConn):
  print()
  tagline = input("tagline? ")
  id = int(input("movie id? "))
  print()
  result = objecttier.set_tagline(dbConn, id, tagline)
  if(result == 0):
    print("No such movie...")
  elif(result == 1 ):
    print("Tagline successfully set")
  return
  





# the main information #
print('** Welcome to the MovieLens app **')
print()
print("General stats:")
## getting the number of movies from DB
num_movies = objecttier.num_movies(dbConn)
print("  # of movies: " + format(num_movies,","))
## getting the number of reviews from the database 
num_reviews = objecttier.num_reviews(dbConn)
print("  # of reviews: " +format(num_reviews,","))

## main loop of the program 
print()
user_input = input("Please enter a command (1-5, x to exit): ")
# the main loop to read input and output 
# and it's calling the commands functions 
while( user_input != 'x' ):

  if(user_input == "1"):
    print()
    movie_search = input("Enter movie name (wildcards _ and % supported): ")
    command_one(dbConn,movie_search)

  elif(user_input == "2"):
    print()
    movie_id = input("Enter movie id: ")
    command_two(dbConn,movie_id)

  elif(user_input == "3"):
    print()
    N_input = int(input("N? "))
    if(N_input > 0 ):
      command_three(dbConn,N_input)
    else:
      print("Please enter a positive value for N...")
      
  elif(user_input == "4"):
    print()
    review = int(input("Enter rating (0..10): "))
    if(review <0 or review > 10):
      print("Invalid rating...")
    else:
      command_four(dbConn,review)
      
  elif(user_input == "5"):
    command_five(dbConn)
  #  re-read the input again from the user  
  print()
  user_input = input("Please enter a command (1-5, x to exit): ")

