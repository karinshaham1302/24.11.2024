oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a
oscar_winners.add('Emma Watsone')
print(oscar_winners)

# b
oscar_winners_copy = oscar_winners.copy()
print(oscar_winners)

oscar_winners_copy.remove('Meryl Streep')
print(oscar_winners_copy)

oscar_winners_copy.clear()
print(oscar_winners_copy)

# c
common_acctors = titanic_actors & dark_knight_actors
print(common_acctors)

# d
common_actors1 = iron_man_actors & avengers_actors
print(common_actors1)

# e
all_actors_winners = actor_list <= oscar_winners
print(all_actors_winners)

# f
all_avengers_in_actor_list = avengers_actors <= actor_list
print(all_avengers_in_actor_list)

# g
removed_actor = movie_cast.pop()
print(removed_actor)
print(movie_cast)

# h
movie_cast.remove('Matt Damon')
print(movie_cast)

# i
titanic_actors_not_oscar = titanic_actors - oscar_winners
print(titanic_actors_not_oscar)

# j
only_titanic = titanic_actors - dark_knight_actors
only_dark_knight = dark_knight_actors - titanic_actors
one_movie = only_titanic | only_dark_knight
print(one_movie)

# k
oscar_winners.add('Cate Blanchett')
oscar_winners.add('Daniel Day-Lewis')
print(oscar_winners)

# l
combined_actors = titanic_actors | dark_knight_actors
print(combined_actors)
