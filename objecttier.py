#
# objecttier
#
# Builds Movie-related objects from data retrieved through 
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#

#  ### Written by Kenan Kamel A Alghythee ### 
# # NetID: kalghy2, UIN:664753831
# UIC, Spring2022, Feb 23 
# Project2,par 2 
# Overview: This is what called Objecttier for 
# a database application that handles Movies and
# display s series of information that is needed 
# input from the user , but this is only the 
# objecttier , so it will be called by the 
# persenation tier, 
# CS 341, Spring 2022





import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:

  def __init__(self,id,title,release_year):
    self._Movie_ID = int(id)
    self._Title = str(title)
    self._Release_Year = str(release_year)
  
  @property
  def Movie_ID(self):
    return self._Movie_ID
  
  @property
  def Title(self):
    return self._Title
  
  @property
  def Release_Year(self):
    return self._Release_Year



   


##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:
  def __init__(self,id,title,release_year,num_reviews,avg_rating):
    self._Movie_ID = int(id)
    self._Title = str(title)
    self._Release_Year = str(release_year)
    self._Num_Reviews = int(num_reviews)
    self._Avg_Rating = float(avg_rating)
  @property 
  def Movie_ID(self):
    return self._Movie_ID
  @property
  def Title(self):
    return self._Title
  @property
  def Release_Year(self):
    return self._Release_Year
  @property
  def Avg_Rating(self):
    return self._Avg_Rating
  @property
  def Num_Reviews(self):
    return self._Num_Reviews



##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:
  def __init__(self,id,title,release_date,runtime,langauge,budget,revenue,num_reviews,avg_rating,tagline,genres = [],production_companies = []):
    self._Movie_ID = int(id)
    self._Title = str(title)
    self._Release_Date = str(release_date)
    self._Runtime = int(runtime)
    self._Original_Language = str(langauge)
    self._Budget = int(budget)
    self._Revenue = int (revenue)
    self._Num_Reviews = int(num_reviews)
    self._Avg_Rating = float(avg_rating)
    self._Tagline = str(tagline)
    self._Genres = genres
    self._Production_Companies = production_companies

  @property
  def Movie_ID(self):
    return self._Movie_ID
  
  @property
  def Title(self):
    return self._Title
  
  @property
  def Release_Date(self):
    return self._Release_Date
   
  @property
  def Runtime(self):
    return self._Runtime
    
  @property
  def Original_Language(self):
    return self._Original_Language
    
  @property
  def Budget(self):
    return self._Budget
   
  @property
  def Revenue(self):
    return self._Revenue

  @property
  def Num_Reviews(self):
    return self._Num_Reviews
    
  @property
  def Avg_Rating(self):
   return self._Avg_Rating

  @property
  def Tagline(self):
   return self._Tagline

  @property
  def Genres(self):
    return self._Genres

  @property
  def Production_Companies(self):
   return self._Production_Companies



##################################################################
# 
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  sql = "select count(movie_ID) from Movies"
  ## call the rows and execute it 
  row  = datatier.select_one_row(dbConn,sql)
  ## hanlde the errors and return -1, if it's empty
  # or return none as if failed 
  if row is None:
    return -1
  elif row == ():
    return -1
  # if there is no error , read the values and 
  # return it and result
  for r in row:
    return r 
 
  return -1 ## in case unkown case , return -1 
 




##################################################################
# 
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
  sql = "select count(rating) from ratings"

  row  = datatier.select_one_row(dbConn,sql )
  ## in case there was an error  or it's empty 
  if row is None:
    return -1
  # if there is no error , return the result 
  for r in row:
    return r 
  
  return -1 ## in case unkown case , return -1 


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
  sql = """select movie_ID, title, strftime('%Y',Release_Date)
 from Movies
 where title like ?
 order by title asc;"""
  ## exectue the SQL
  rows = datatier.select_n_rows(dbConn,sql,[pattern])
  result = []
  # handle the cases of error, and return [] list if there is one
  if rows is None:
    return []
  else: ## othereise if there is no errors , create a list of #objects or type Movies and return it 
    for row in rows:
      movie = Movie(row[0],row[1],row[2])
      result.append(movie)
  return result



 



##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  sql = """ select Movies.Movie_ID, title, date(release_date),runtime, original_language,budget,revenue,
  count(Ratings.Rating),avg(Ratings.rating), Movie_Taglines.Tagline from Movies 
  left join  Movie_Taglines on (Movies.Movie_ID = Movie_Taglines.Movie_ID)
  left join Ratings on (Ratings.Movie_ID = Movies.Movie_ID)
  where Movies.Movie_ID = ? 
  """
  row_movie = datatier.select_one_row(dbConn,sql,[movie_id])
  ## handle the error cases 
  if row_movie[0] is None:
    return None
  elif row_movie[0] == ():
    return None
  ## used to hanlde and return the genres of the given movie
  sql_genres = """ select Genres.genre_name from Genres
  join Movie_genres on (Genres.Genre_ID = Movie_genres.Genre_ID)
  where Movie_genres.Movie_ID = ?
  order by Genres.genre_name  asc """
  row_genre = datatier.select_n_rows(dbConn,sql_genres,[movie_id])
   
  ## getting the genres  
  genres = []
  for r in row_genre:
    genres.append(r[0])
  ## retunr the companies of a given movie 
  sql_companies = """ select Companies.company_name from Companies
  join Movie_Production_Companies on (Movie_Production_Companies.company_ID = companies.company_ID)
  where Movie_Production_Companies.Movie_ID = ?
  order by Companies.company_name asc;"""
  row_companies = datatier.select_n_rows(dbConn,sql_companies,[movie_id])
  companies = []
  ## creating hte object and store all of its value 
  for r in row_companies:
    companies.append(r[0])
  ## handle the diffrent possible cases of tagline, and avg_rating
  if(row_movie[8] == None ):
    avg_rating = float(0.00)
  else:
    avg_rating = row_movie[8]
  
  if(row_movie[9] == None):
    tagline = ""
  else:# setup the MovieDeatils object and return it 
    tagline = row_movie[9]
  movie_details = MovieDetails(row_movie[0],row_movie[1],row_movie[2],
  row_movie[3], row_movie[4],row_movie[5],row_movie[6],row_movie[7],avg_rating, tagline,genres,companies)
  
  return movie_details 



  

   
         

##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average 
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error 
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
  sql = """ select Movies.Movie_ID , title, strftime('%Y',Release_Date),  avg(Ratings.rating),count(Ratings.rating) from Movies
  join Ratings on (Ratings.Movie_ID = Movies.Movie_ID)
  group by Movies.Movie_ID
  Having count(Ratings.Rating) >= ? 
  order by avg(Ratings.Rating) desc
  limit ?  """
  # verysimilar to the obove just a diffrent SQL , and new object of type
  # movieRating
  rows = datatier.select_n_rows(dbConn,sql,[min_num_reviews,N])
  if rows == None:
    return []
  elif rows == []:
    return []
  
  result = []
  for r in rows:
    movie_rating = MovieRating(r[0],r[1],r[2],r[4],r[3])
    result.append(movie_rating)


    
  return result





##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
  # here is used to search for the ID 
  sql_ID = " select Movie_ID from Movies where movie_ID = ? "
  search_result = datatier.select_one_row(dbConn,sql_ID,[movie_id])
  
  ## an issue happend with the ID
  if search_result == None:
    return 0
  elif search_result== "()":
    return 0
  
  ## if the id exits then inser the infroation and hanld the errors 
  sql_rating = """insert into Ratings(Movie_ID,Rating)
  values(?,?); """
  insert_result = datatier.perform_action(dbConn,sql_rating,[movie_id,rating])
  if(insert_result == -1):
    return 0
  else:
    return 1 




##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively 
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
  ## search for the ID , and handle the case of errors 
  sql_ID = " select Movie_ID from Movies where movie_ID = ? "
  search_result = datatier.select_one_row(dbConn,sql_ID,[movie_id])
  if(search_result == None):
    return 0  
  elif (search_result) == "()":
    return 0
  ## no issue happend then start searching the DB
  ## SQL, for searching TAG, and inserting and updating 
  sql_Tag = "select  Tagline from Movie_Taglines where movie_ID = ?"
  sql_insert = """insert into Movie_Taglines(Movie_ID,Tagline)
  values(?,?); """
  sql_update = " update Movie_Taglines set Tagline = ? where Movie_ID = ?"
  ## execute the SQL,and based on the result execute diffrent cases, inseart,
  # or update 
  search_tagline = datatier.select_one_row(dbConn,sql_Tag,[movie_id])
  ## no tagline or empty , then inseart 
  if (search_tagline == None or search_tagline == () ):
    insert_result = datatier.perform_action(dbConn,sql_insert,[movie_id,tagline])
    ## handle errors of insrting 
    if(insert_result == -1):
      return 0
    else:
      return 1
  else: ## in case there is a Tagline, then update 
    update_result = datatier.perform_action(dbConn,sql_update,[tagline,movie_id])
    ## handle the cases of failer or not and return 
    if(update_result == -1):
      return 0
    else:
      return 1 






   
