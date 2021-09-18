import random
import pandas as pd
import numpy as np

import shared.CONSTANTS as CONSTANTS
from shared.utils import Utils as utils
from models.coordinate_model import CoordinateModel
from src.gameplay import GamePlay as gameplay
from shared.MESSAGES import Messages as MESSAGE

class SkynetAI:
    
    coordinate_model = CoordinateModel()
    skynet_coordinate_x = []
    skynet_coordinate_y = []

    def generate_board():
        for ship_model in CONSTANTS.LIST_OF_SHIP_MODELS:
            SkynetAI.random_insertion( CONSTANTS.GRID_IA, ship_model )
            
        return CONSTANTS.GRID_IA
    
    def random_insertion( grid, ship_model ):
        inserted = False
        SkynetAI.coordinate_model.reset()
        
        while not inserted:
            SkynetAI.coordinate_model.coordinate_x = random.randint( 0, 9 )
            SkynetAI.coordinate_model.coordinate_y = random.randint( 0, 9 )
            SkynetAI.coordinate_model.position = random.randint( 0, 1 )
            
            if SkynetAI.coordinate_model.position == 0:
                SkynetAI.coordinate_model.position = "V"
            else:
                SkynetAI.coordinate_model.position = "H"
            
            inserted = gameplay.position_ship( grid, ship_model, SkynetAI.coordinate_model, False)

    # Genetic Algorithm Section ---------------------
    def random_generation(generation_size, genes):
        # create dataframe for gene pool
        generation = pd.DataFrame(columns=[CONSTANTS.CONST_SEQUENCE, CONSTANTS.CONST_CHROMOSSOME, CONSTANTS.CONST_GENERATION, 
            CONSTANTS.CONST_BIRTH, CONSTANTS.CONST_FITNESS, CONSTANTS.CONST_PARENTS])

        i = 0
        while i < generation_size:

            # create random chromosome
            chromosome = {}
            chromosome[CONSTANTS.CONST_SEQUENCE] = i+1
            chromosome[CONSTANTS.CONST_CHROMOSSOME] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
            chromosome[CONSTANTS.CONST_GENERATION] = 1
            chromosome[CONSTANTS.CONST_BIRTH] = CONSTANTS.CONST_RANDOM
            chromosome[CONSTANTS.CONST_PARENTS] = 0

            # check for uniqueness and add to gene pool
            if chromosome[CONSTANTS.CONST_CHROMOSSOME] not in generation[CONSTANTS.CONST_CHROMOSSOME]:
                generation = generation.append(chromosome, ignore_index=True)
                i += 1

        return generation

    def assign_elites(generation, elite_rate):
        # determine number of elites
        generation_size = generation.shape[0]
        elites = elite_rate * generation_size
        
        # assign elite status to most fit chromosomes
        generation[CONSTANTS.CONST_ELITE] = False
        generation = generation.sort_values(by=CONSTANTS.CONST_FITNESS, ascending=False)
        generation.iloc[0:int(elites),6:7] = True
        
        return generation

    def select_elites(generation):    
        # copy elites from old generation
        elites = generation.loc[generation[CONSTANTS.CONST_ELITE] == True].copy()
        
        # update attributes of new generation
        pool_size = generation[CONSTANTS.CONST_SEQUENCE].max()
        elites[CONSTANTS.CONST_PARENTS] = elites[CONSTANTS.CONST_SEQUENCE]
        elites[CONSTANTS.CONST_SEQUENCE] = range(pool_size + 1, pool_size + elites.shape[0] + 1)
        elites.loc[:,CONSTANTS.CONST_BIRTH] = CONSTANTS.CONST_ELITISM
        elites[CONSTANTS.CONST_ELITE] = False
        elites[CONSTANTS.CONST_GENERATION] = generation[CONSTANTS.CONST_GENERATION].max() + 1
        
        return elites

    def create_mutants(generation, mutants, bit_flip_rate):    
        # get generation attributes
        last_generation = generation[CONSTANTS.CONST_GENERATION].max()
        last_sequence = generation[CONSTANTS.CONST_SEQUENCE].max()
        n_elites = generation[CONSTANTS.CONST_BIRTH].value_counts()[CONSTANTS.CONST_ELITISM]
        
        # for each mutant
        i = 0
        while i < mutants:
            
            # create mutant chromosome
            chromosome = {}
            chromosome[CONSTANTS.CONST_SEQUENCE] = last_sequence + i + 1
            chromosome[CONSTANTS.CONST_GENERATION] = last_generation
            chromosome[CONSTANTS.CONST_BIRTH] = CONSTANTS.CONST_MUTATION
            chromosome[CONSTANTS.CONST_ELITE] = False
            
            # select random elite as new parent
            parent_index = np.random.choice(n_elites)
            chromosome['Parents'] = list(generation[CONSTANTS.CONST_SEQUENCE].values)[parent_index]
            parent = list(generation[CONSTANTS.CONST_CHROMOSSOME].values)[parent_index]

            # create array of random bit flips
            bit_flip_array = np.random.choice(2, len(parent), p=[1 - bit_flip_rate, bit_flip_rate])
            bits_to_flip = ''.join(str(x) for x in list(bit_flip_array.flatten()))

            # create mutant child from parent and flip bits from array
            mutant = ''
            for j in range(len(bits_to_flip)):
                if not int(bits_to_flip[j]):
                    mutant += parent[j]
                else:
                    mutant += str(abs(int(parent[j]) - 1))
            
            # check for uniqueness and add to gene pool
            chromosome[CONSTANTS.CONST_CHROMOSSOME] = mutant
            if chromosome[CONSTANTS.CONST_CHROMOSSOME] not in generation[CONSTANTS.CONST_CHROMOSSOME]:
                generation = generation.append(chromosome, ignore_index=True)
                i += 1
                
        return generation

    def create_splices(generation, n_splice_pairs):        
        # get generation attributes
        last_generation = generation[CONSTANTS.CONST_GENERATION].max()
        last_sequence = generation[CONSTANTS.CONST_SEQUENCE].max()
        n_elites = generation[CONSTANTS.CONST_BIRTH].value_counts()[CONSTANTS.CONST_ELITISM]
        
        # for each splice pair
        i = 0
        while i < n_splice_pairs:
            
            # create splice pair chromosome
            chromosome = {}
            chromosome[CONSTANTS.CONST_GENERATION] = last_generation
            chromosome[CONSTANTS.CONST_BIRTH] = CONSTANTS.CONST_SPLICE_PAIR
            chromosome[CONSTANTS.CONST_ELITE] = False
            
            # select random elite pair as new parents
            parent_indices = np.random.choice(n_elites, 2, replace=False)
            chromosome[CONSTANTS.CONST_PARENTS] = np.array(generation[CONSTANTS.CONST_SEQUENCE].values)[parent_indices]
            parents = np.array(generation[CONSTANTS.CONST_CHROMOSSOME].values)[parent_indices]

            # create random splice bit
            splice_bit = np.random.randint(len(parents[0]))

            # create splice pair children from parent and cross over bits
            splices = []
            splices.append(parents[0][0:splice_bit] + parents[1][splice_bit:len(parents[1])])
            splices.append(parents[1][0:splice_bit] + parents[0][splice_bit:len(parents[0])])
            
            # add splices to gene pool
            chromosome[CONSTANTS.CONST_CHROMOSSOME] = splices[0]
            chromosome[CONSTANTS.CONST_SEQUENCE] = last_sequence + i + 1
            generation = generation.append(chromosome, ignore_index=True)
            
            chromosome[CONSTANTS.CONST_CHROMOSSOME] = splices[1]
            chromosome[CONSTANTS.CONST_SEQUENCE] = last_sequence + i + 2
            generation = generation.append(chromosome, ignore_index=True)
                
            i += 1
                
        # return the generation
        return generation

    def fill_random(generation, generation_size, genes):        
        # get generation attributes
        last_generation = generation[CONSTANTS.CONST_GENERATION].max()
        last_sequence = generation[CONSTANTS.CONST_SEQUENCE].max()
        
        # for each random chromosome
        i = generation.shape[0]
        while i < generation_size:
            
            # create random chromosome
            chromosome = {}
            chromosome[CONSTANTS.CONST_SEQUENCE] = last_sequence + i + 1
            chromosome[CONSTANTS.CONST_CHROMOSSOME] = ''.join(str(x) for x in list(np.random.randint(2, size=genes)))
            chromosome[CONSTANTS.CONST_GENERATION] = last_generation
            chromosome[CONSTANTS.CONST_BIRTH] = CONSTANTS.CONST_RANDOM
            chromosome[CONSTANTS.CONST_PARENTS] = 0
            chromosome[CONSTANTS.CONST_ELITE] = False

            # check for uniqueness and add to gene pool
            if chromosome[CONSTANTS.CONST_CHROMOSSOME] not in generation[CONSTANTS.CONST_CHROMOSSOME]:
                generation = generation.append(chromosome, ignore_index=True)
                i += 1
                
        # return the generation
        return generation

    def create_descendents(gene_pool, elite_rate, solution, stop_limit):        
        # copy initial generation
        next_generation = gene_pool.copy()
        generation_size = next_generation.shape[0]
        
        # create generations until fitness criteria is achieved
        while gene_pool[CONSTANTS.CONST_FITNESS].max() < stop_limit:          
            # select elites with elite rate
            next_generation = SkynetAI.select_elites(next_generation)

            # add splice pairs to generation
            splice_pair_rate = elite_rate / 2
            n_splice_pairs = int(splice_pair_rate * generation_size)
            next_generation = SkynetAI.create_splices(next_generation, n_splice_pairs)

            # add mutants to generation
            mutant_rate = 0.60
            bit_flip_rate = 0.01
            n_mutants = int(mutant_rate * generation_size)
            next_generation = SkynetAI.create_mutants(next_generation, n_mutants, bit_flip_rate)

            # fill the rest of the generation with random chromosomes for diversity
            next_generation = SkynetAI.fill_random(next_generation, generation_size, 100)

            # compare fitness
            next_generation[CONSTANTS.CONST_FITNESS] = next_generation.apply(lambda row: SkynetAI.accuracy(row.Chromosome, solution), axis=1)

            # assign elites with elite rate
            elite_rate = 0.20
            next_generation = SkynetAI.assign_elites(next_generation, elite_rate)
            next_generation

            # add generation to gene pool
            gene_pool = gene_pool.append(next_generation)

        return gene_pool
    
    # fitness function
    def accuracy(solution, candidate):
        n_gene_matches = 0
        
        for i in range(len(solution)):
            if solution[i] == candidate[i]:
                n_gene_matches += 1
                
        return n_gene_matches / len(solution)

    def solve(solution, generation_size):
        # initialize the first random generation
        gene_pool = SkynetAI.random_generation(generation_size, 100)

        # compare fitness
        gene_pool[CONSTANTS.CONST_FITNESS] = gene_pool.apply(lambda row: SkynetAI.accuracy(row.Chromosome, solution), axis=1)

        # assign elites with elite rate
        elite_rate = 0.20
        gene_pool = SkynetAI.assign_elites(gene_pool, elite_rate)

        # create successive generations until termination criteria is met
        gene_pool = SkynetAI.create_descendents(gene_pool, elite_rate, solution, 1.0)
        gene_pool = gene_pool.set_index(CONSTANTS.CONST_SEQUENCE)
        
        return gene_pool

    def skynet_attack( grid, skynetCountMoves ):
        if skynetCountMoves == 0:
            MESSAGE.MESSAGE_SKYNET_THINKING()
            gridConvertedToSolution = utils.convert_grid_to_skynet_solution( grid )            
            genetic_solution = ( '' ).join( str( x ) for x in list( gridConvertedToSolution.flatten() ) )

            gene_pool = SkynetAI.solve( genetic_solution, 10 )
            gene_filtered = gene_pool.loc[gene_pool.Fitness.idxmax()]
            
            utils.draw_points()
            
            geneArrayReturned = np.array( list( gene_filtered.Chromosome ), dtype=int )
            geneArrayReshaped = np.reshape( geneArrayReturned, ( 10, 10 ) )
            
            ship_positions = np.where( geneArrayReshaped == 1 )
            SkynetAI.skynet_coordinate_x = ship_positions[1]
            SkynetAI.skynet_coordinate_y = ship_positions[0]
            SkynetAI.skynet_coordinate()
        else:
            SkynetAI.skynet_coordinate()
        return SkynetAI.coordinate_model
    
    def skynet_coordinate():
        SkynetAI.coordinate_model.coordinate_x = SkynetAI.skynet_coordinate_x[0]
        SkynetAI.coordinate_model.coordinate_y = SkynetAI.skynet_coordinate_y[0]
        SkynetAI.skynet_coordinate_x = np.delete(SkynetAI.skynet_coordinate_x, (0))
        SkynetAI.skynet_coordinate_y = np.delete(SkynetAI.skynet_coordinate_y, (0))

    
