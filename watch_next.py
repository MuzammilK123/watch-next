#Similarity in description of movies

#imports
import spacy

nlp = spacy.load("en_core_web_md")

# Read movie descriptions from the movie.txt file
with open('movies.txt', 'r') as file:
    movie_descriptions = [line.strip() for line in file]

# Function that calculates similarities between the input description and each movie description
def find_most_similar_movie(description):
# Calculate similarities between the input description and each movie description
    similarities = []
    input_doc = nlp(description)
    for movie_description in movie_descriptions:
        movie_doc = nlp(movie_description)
        similarity = input_doc.similarity(movie_doc)
        similarities.append(similarity)
    
# Find the index of the most similar movie
    most_similar_index = similarities.index(max(similarities))
    most_similar_movie = movie_descriptions[most_similar_index].split(' :')[0]
    
    return most_similar_movie

description = "Will they save their world or destroy it? When the Hulk becomes dangerous for Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

most_similar_movie = find_most_similar_movie(description)
print("The most similar movie is:", most_similar_movie)
