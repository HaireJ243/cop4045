import csv

def display_top_collaborators(rated_file, cast_file):
    """Displays director/actor pais and their movies"""

    try:
        #store top movies
        rated_movies = []

        with open(rated_file, "r", encoding = "utf-8-sig") as file:
            reader = csv.reader(file)

            #skip heading
            next(reader)

            for row in reader:
                title = row[1]
                year  = row[2]

                rated_movies.append((title, year))

        collaborations = {}

        with open(cast_file, "r", encoding = "utf-8-sig") as file:
            reader = csv.reader(file)

            for row in reader:
                title    = row[0]
                year     = row[1]
                director = row[2]

                # only use what is in top rated list
                if (title, year) in rated_movies:

                    #top actors
                    for i in range(3, len(row)):
                        actor = row[i]

                        if actor != "":
                            pair = (director, actor)

                            if pair in collaborations:
                                collaborations[pair] += 1
                            else:
                                collaborations[pair] = 1

        # rated_movies dict info into list
        results = []

        for pair in collaborations:
            director = pair[0]
            actor    = pair[1]
            count    = collaborations[pair]

            results.append((count, director, actor))

        #sort in descending order
        results.sort(reverse=True)

        print("Top collaborations: ")

        rank = 1
        for item in results[:10]:
            count    = item[0]
            director = item[1]
            actor    = item[2]

            print(rank, director, actor, count)
            rank += 1

    except:
        print("Error occured finding collaborations.")
        raise

def display_top_actors(top_gross_file, cast_file):
    """Rank actors by total gross money"""

    try:
        #store actors and their movies
        movie_cast = {}

        with open(cast_file, "r", encoding = "utf-8-sig") as file:
            reader = csv.reader(file)

            for row in reader:
                title = row[0]
                year  = row[1]

                actors = []

                for i in range(3, len(row)):
                    if row[i] != "":
                        actors.append(row[i])

                movie_cast[(title, year)] = actors

        #store total gross money
        actors_totals = {}

        with open(top_gross_file, "r", encoding = "utf-8-sig") as file:
            reader = csv.reader(file)

            #skip heading
            next(reader)

            for row in reader: #limited to fin in terminal
                title = row[1]
                year  = row[2]
                money = row[3]

                #remove characters 
                money = money.replace("$", "") #characters that could interfere with 
                                               #coverting to integer
                money = money.replace(",", "") 

                if money != "":
                    box_office = int(money)
                    movie      = (title, year)

                    if movie in movie_cast:
                        actors = movie_cast[movie]

                        for actor in actors:
                            if actor in actors_totals:
                                actors_totals[actor] += box_office
                            else:
                                actors_totals[actor] = box_office

        #movie_cast dict info into list
        results = []

        for actor in actors_totals:
            total = actors_totals[actor]

            results.append((total, actor))

        results.sort(reverse= True)

        print("\nTop Actors: ")

        rank = 1
        for item in results[:10]: #limited to fit in terminal
            total = item[0]
            actor = item[1]

            print(rank, actor, total)
            rank += 1

    except:
        print("Error occurred finding top actors")
        raise

def main():
    """Tests functions"""

    try: 
        display_top_collaborators("imdb-top-rated.csv", "imdb-top-casts.csv")

        display_top_actors("imdb-top-grossing.csv", "imdb-top-casts.csv")

    except: 
        print("Error occurred while testing program")
        raise

main()
