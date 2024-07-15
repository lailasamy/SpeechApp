# material_generator.py

def generate_material(difficulty):
    materials = {
        'easy': [
            "cat", "dog", "bat", "rat", "hat", "sun", "moon", "star", "sky", "tree",
            "flower", "grass", "leaf", "rock", "stone", "fish", "bird", "ant", "bee",
            "apple", "orange", "banana", "grape", "pear", "car", "bus", "bike", "road",
            "chair", "table", "bed", "door", "window", "cup", "plate", "spoon", "fork",
            "house", "home", "school", "book", "pen", "pencil", "paper", "notebook", "bag",
            "shoe", "sock", "hat", "glove", "coat", "shirt", "pants", "dress", "skirt",
            "ball", "bat", "game", "toy", "doll", "puzzle", "block", "card", "train",
            "light", "lamp", "fan", "clock", "phone", "watch", "radio", "tv", "computer",
            "mouse", "keyboard", "screen", "printer", "camera", "photo", "picture", "drawing",
            "paint", "brush", "color", "red", "blue", "green", "yellow", "black", "white",
            "brown", "purple", "orange", "pink", "gray", "gold", "silver", "circle", "square"
        ],
        'medium': [
            "elephant", "giraffe", "crocodile", "buffalo", "dolphin", "kangaroo", "penguin", "raccoon",
            "squirrel", "butterfly", "caterpillar", "mosquito", "grasshopper", "woodpecker", "parrot",
            "flamingo", "peacock", "sparrow", "pelican", "ostrich", "alligator", "chameleon", "lizard",
            "iguana", "tortoise", "hedgehog", "porcupine", "armadillo", "hamster", "rabbit", "swan",
            "ostrich", "turkey", "vulture", "lobster", "octopus", "scorpion", "tarantula", "rhinoceros",
            "hippopotamus", "chimpanzee", "orangutan", "gorilla", "baboon", "lemur", "koala", "panda",
            "jackal", "hyena", "meerkat", "antelope", "buffalo", "caribou", "wildebeest", "gazelle",
            "impala", "reindeer", "zebra", "donkey", "mule", "pony", "stallion", "tiger", "leopard",
            "cheetah", "panther", "jaguar", "lynx", "cougar", "bobcat", "mountain lion", "wolf", "fox",
            "coyote", "dingo", "seal", "walrus", "manatee", "narwhal", "dolphin", "whale", "orca", "beluga",
            "porpoise", "shark", "stingray", "jellyfish", "starfish", "seahorse", "coral", "anemone",
            "clam", "oyster", "mussel", "scallop", "barnacle", "crab", "lobster", "shrimp", "prawn"
        ],
        'hard': [
            "hippopotamus", "archaeology", "encyclopedia", "rhinoceros", "psychiatrist", "ophthalmologist",
            "otorhinolaryngologist", "aerodynamics", "electromagnetic", "neuroscientist", "physicochemistry",
            "paleontology", "astrophysics", "biotechnology", "cybersecurity", "epidemiology", "hematology",
            "nanotechnology", "pharmacology", "psychotherapy", "radiology", "seismology", "toxicology",
            "thermodynamics", "volcanology", "veterinarian", "quantum", "mechanics", "relativity", "superconductivity",
            "gravitational", "wave", "cosmology", "particle", "physics", "neutrino", "antimatter", "dark", "matter",
            "energy", "fusion", "fission", "reactor", "acceleration", "ionization", "oxidation", "reduction",
            "catalysis", "fermentation", "photosynthesis", "polymerization", "electrolysis", "transcription",
            "translation", "mutation", "replication", "recombination", "endocytosis", "exocytosis", "autophagy",
            "apoptosis", "metabolism", "homeostasis", "immunology", "biostatistics", "bioinformatics", "genomics",
            "proteomics", "metabolomics", "lipidomics", "glycomics", "biochemistry", "microbiology", "virology",
            "bacteriology", "parasitology", "mycology", "protozoology", "phycology", "environmental", "ecology",
            "conservation", "sustainability", "climatology", "meteorology", "oceanography", "limnology", "hydrology",
            "geophysics", "geochemistry", "petrology", "mineralogy", "paleoclimatology", "stratigraphy", "geochronology"
        ]
    }
    return materials.get(difficulty, [])
