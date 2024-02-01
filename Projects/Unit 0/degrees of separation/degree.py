import csv
import sys
import time
import termcolor as tc

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])
        print("Total People: ", len(people))
    
    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }
        print("Total Movies: ", len(movies))
    
    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print()
    tc.cprint("Loading data...", "blue")
    load_data(directory)
    tc.cprint("Data Loaded", "green")
    repeat =  True
    while repeat:
        source = None
        target = None
        while source is None:
            source = person_id_for_name(input("\nSource Name: "))
            if source is None:
                print("Person not found.")
                print("try again")
        while target is None:
            target = person_id_for_name(input("\nTarget Name: "))
            if target is None:
                print("Person not found")
                print("try again")

        
        print("\nSearching...")
        path = shortest_path(source, target)
        
        if len(path) == 0:
            tc.cprint("!!!Not Connected!!!", "red")
        else:
            degrees = len(path)
            print(f"\n{degrees} degrees of separation.\n")
            path = [(None, source)] + path
            for i in range(degrees):
                person1 = people[path[i][1]]["name"]
                person2 = people[path[i + 1][1]]["name"]
                movie = movies[path[i + 1][0]]["title"]
                year = movies[path[i + 1][0]]["year"]
                other_actor = set()
                for idss in list(movies[path[i + 1][0]]["stars"]):
                    other_actor.add(people[idss]["name"])
                
                other_actor = other_actor - set([person1, person2])
                print(f"\t{i + 1}: {person1} and {person2} starred in {movie} in {year} with {other_actor}")
    
        c = input("Enter 1 if you want try more with stars: ")
        if c != '1':
            repeat = False


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"\tWhich '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"\tID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("\tIntended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    person_movies = list(people[person_id]["movies"])
    result = set()
    for movie_id in person_movies:
        star_ids = list(movies[movie_id]["stars"])
        for star_id in star_ids:
            result.add((movie_id, star_id))
    return result

def makeSolution(node):
    solution = []
    while node.parent is not None:
        solution.append((node.action, node.state))
        node = node.parent
    solution.reverse()
    return solution


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    
    If no possible path, returns None.
    """

    exploredSet = set()
    cost = 0
    frontier = QueueFrontier()
    node = Node(source, None, None)
    frontier.add(node)
    
    start_time = time.time()
    print("Progress: ", end=" ")
    while True:
        if frontier.is_empty() is True:
            return []
        node = frontier.remove()
        cost = cost + 1
        total = len(people)
        
        if time.time() - start_time >= 1:
            sys.stdout.write("\rProgress: {}/{}".format(cost, total))
            start_time = time.time()
        sys.stdout.flush()
        
        if node.state == target:
            tc.cprint("\n Searchign completed", "yellow")
            Solution = makeSolution(node)
            return Solution
        
        exploredSet.add(node.state)
        
        for movie, stars in neighbors_for_person(node.state):
            if frontier.is_contain(stars) is False and stars not in exploredSet:
                newNode = Node(stars, node, movie)
                frontier.add(newNode)





if __name__ =="__main__":
    main()
