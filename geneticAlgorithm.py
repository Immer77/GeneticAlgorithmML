from typing import List
from random import choices
from collections import namedtuple

#General representation for the data set that we are going to run a genetic algorithm on.
Genome = List[int]

# En population er bare en list af den generelle genome list.
Population = List[Genome]

# En tuple thing der har et navn, vægt og en value.
Thing = namedtuple('Thing', ['name','value','weight'])

FitnessFunc = Callable([Genome], int)


things = [  
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water bottle', 30, 192),
]

more_things = [
    Thing('Mints', 5, 25),
    Thing('Socks', 10, 38),
    Thing('Tissues', 15, 80),
    Thing('Phone', 500, 200),
    Thing('Baseball Cap', 100, 70),
]

def generate_genome(length: int) -> Genome:
    return choices([0,1], k=length)


# for at fylde noget data i populationen.
def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

# En fitness funktion til at evaluere en løsning.
# En fitness funktion tager 3 inputs
# Genome
# En liste af ting vi kan vælge fra
# Et max antal kg på hvor meget vi kan have med i.
def fitness(genome : Genome, things: Thing, weight_limit: int) -> int:
    if(len(genome) != len(things)):
        raise ValueError("Genome and things must be of the same length")
    
    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value
            # Hvis vægten overstiger er denne løsning invalid.
            if weight > weight_limit:
                return 0
    
    # Når vi igennem alle items uden at overstige maks vægt kan vi bare returnere værdien.
    return value


# Denne funktion udvælger 2 solutions som vil blive parents for den næste generation
def selection_Pair(population: Population, fitness_func: fitness) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        #k=2 simulere vi trækker 2 altså et pair
        k=2
    )
