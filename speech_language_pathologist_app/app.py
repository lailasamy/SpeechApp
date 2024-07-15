from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Dummy data for word difficulties
words = {
    'easy': [
        "apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "igloo", "jar", "kite", "lion", "moon", "nest", 
        "orange", "pig", "queen", "rat", "sun", "top", "umbrella", "van", "whale", "xylophone", "yak", "zebra", 
        "ant", "bird", "cow", "duck", "elf", "frog", "gift", "horse", "ice", "jam", "key", "leaf", "mouse", "nut", 
        "owl", "panda", "quilt", "rabbit", "snake", "turtle", "unicorn", "vase", "wolf", "yarn", "zigzag", "arm", 
        "bear", "coat", "drum", "ear", "flag", "game", "hill", "insect", "jeep", "kite", "lake", "monkey", "nurse", 
        "octopus", "park", "quail", "rainbow", "star", "tree", "unicorn", "violin", "window", "yellow", "zebra", "ax", 
        "box", "cup", "door", "egg", "fan", "gum", "hero", "iguana", "jet", "king", "lamp", "mitten", "nose", "oven", 
        "pizza", "quiz", "robot", "soap", "tiger", "ukulele", "vest", "wand", "x-ray", "yolk", "zigzag", "alligator", 
        "boat", "chair", "desk", "engine", "fork", "grapes", "house", "island", "jelly", "kangaroo", "lemon", "marker", 
        "notebook", "ostrich", "piglet", "quarter", "rocket", "shoe", "table", "umbrella", "volcano", "watermelon", 
        "xylophone", "yogurt", "zipper", "airplane", "bike", "car", "deer", "eagle", "fox", "giraffe", "hippo", 
        "iguana", "jack", "kite", "lion", "monkey", "nest", "ostrich", "peacock", "quack", "rocket", "ship", "tiger", 
        "umbrella", "violin", "whale", "xylophone", "yacht", "zebra", "apple", "banana", "carrot", "donut", "elephant", 
        "flower", "goat", "hat", "ink", "jacket", "key", "leaf", "monkey", "nut", "octopus", "pencil", "queen", "rabbit", 
        "sock", "tree", "umbrella", "vase", "whale", "x-ray", "yak", "zebra", "ant", "ball", "cat", "dog", "egg", "fish", 
        "goat", "hat", "ice", "jar", "kite", "lion", "moon", "nest", "orange", "pig", "queen", "rat", "sun", "top", 
        "umbrella", "van", "whale", "xylophone", "yak", "zebra", "ant", "bird", "cow", "duck", "elf", "frog", "gift", 
        "horse", "ice", "jam", "key", "leaf", "mouse", "nut", "owl", "panda", "quilt", "rabbit", "snake", "turtle", 
        "unicorn", "vase", "wolf", "yarn", "zigzag", "arm", "bear", "coat", "drum", "ear", "flag", "game", "hill", 
        "insect", "jeep", "kite", "lake", "monkey", "nurse", "octopus", "park", "quail", "rainbow", "star", "tree", 
        "unicorn", "violin", "window", "yellow", "zebra", "ax", "box", "cup", "door", "egg", "fan", "gum", "hero", 
        "iguana", "jet", "king", "lamp", "mitten", "nose", "oven", "pizza", "quiz", "robot", "soap", "tiger", "ukulele", 
        "vest", "wand", "x-ray", "yolk", "zigzag", "alligator", "boat", "chair", "desk", "engine", "fork", "grapes", 
        "house", "island", "jelly", "kangaroo", "lemon", "marker", "notebook", "ostrich", "piglet", "quarter", "rocket", 
        "shoe", "table", "umbrella", "volcano", "watermelon", "xylophone", "yogurt", "zipper", "airplane", "bike", 
        "car", "deer", "eagle", "fox", "giraffe", "hippo", "iguana", "jack", "kite", "lion", "monkey", "nest", "ostrich", 
        "peacock", "quack", "rocket", "ship", "tiger", "umbrella", "violin", "whale", "xylophone", "yacht", "zebra", 
        "apple", "banana", "carrot", "donut", "elephant", "flower", "goat", "hat", "ink", "jacket", "key", "leaf", 
        "monkey", "nut", "octopus", "pencil", "queen", "rabbit", "sock", "tree", "umbrella", "vase", "whale", "x-ray", 
        "yak", "zebra", "ant", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jar", "kite", "lion", "moon", 
        "nest", "orange", "pig", "queen", "rat", "sun", "top", "umbrella", "van", "whale", "xylophone", "yak", "zebra"
    ],
    'medium': [
        "elephant", "giraffe", "crocodile", "buffalo", "dolphin", "zebra", "tiger", "rabbit", "squirrel", "kangaroo", 
        "parrot", "turtle", "alligator", "butterfly", "cheetah", "dinosaur", "eagle", "flamingo", "gorilla", "hedgehog", 
        "iguana", "jellyfish", "koala", "leopard", "monkey", "narwhal", "octopus", "penguin", "quail", "rhinoceros", 
        "snake", "toucan", "urchin", "vulture", "walrus", "xerus", "yak", "zebu", "alpaca", "beetle", "cricket", 
        "dragon", "emu", "falcon", "gecko", "hippo", "insect", "jackal", "kudu", "llama", "mule", "newt", "ostrich", 
        "panda", "quokka", "raccoon", "scorpion", "tarantula", "urchin", "viper", "wombat", "xenopus", "yak", "zebra", 
        "antelope", "baboon", "chimpanzee", "dingo", "elephant", "ferret", "gazelle", "hyena", "impala", "jaguar", 
        "kangaroo", "lemur", "meerkat", "nyala", "orangutan", "panther", "quail", "raven", "seal", "tortoise", "unicorn", 
        "vulture", "wolf", "xenopus", "yak", "zebra", "airplane", "balloon", "chocolate", "dancing", "exercise", 
        "fireworks", "garden", "helicopter", "island", "jungle", "kite", "laughter", "mountain", "nature", "ocean", 
        "picnic", "quilt", "rainbow", "sailing", "trampoline", "underwater", "volcano", "waterfall", "xylophone", 
        "yogurt", "zebra", "astronaut", "bicycle", "climbing", "diving", "exploring", "festival", "galaxy", "hiking", 
        "ice cream", "jigsaw", "kayaking", "library", "music", "nighttime", "orchestra", "painting", "quiet", "reptile", 
        "safari", "traveling", "umbrella", "vacation", "wildlife", "xylophone", "yoga", "zookeeper", "animation", 
        "basketball", "camping", "drumming", "entertainment", "festival", "gardening", "hiking", "ice skating", 
        "juggling", "kite flying", "lights", "movies", "navigating", "outdoors", "photography", "quilting", "racing", 
        "sports", "tinkering", "universe", "vacationing", "wrestling", "x-ray", "yodeling", "zip lining", "adventure", 
        "baking", "crafting", "drawing", "education", "friendship", "games", "happiness", "imagination", "jumping", 
        "kicking", "learning", "mystery", "nature", "origami", "playground", "quests", "reading", "science", "teaching", 
        "unicorns", "volunteering", "wandering", "xeroxing", "yawning", "zigzagging", "architecture", "backpacking", 
        "costumes", "dinosaurs", "electronics", "fantasy", "gardens", "holograms", "inventions", "jungle gym", 
        "kaleidoscope", "landscapes", "museums", "nebula", "observation", "puzzles", "quilting", "robots", "sculpture", 
        "technology", "universe", "videos", "windmills", "xenon", "yo-yo", "ziplines", "activity", "balancing", 
        "comics", "doodles", "experiment", "fascination", "gadget", "holidays", "insects", "jamboree", "keepsake", 
        "labyrinth", "magnets", "navigation", "observatory", "paddleboarding", "quests", "rollercoaster", "skydiving", 
        "telescope", "unity", "voyage", "wilderness", "xenon", "yo-yo", "zoology", "aviation", "biology", "chemistry", 
        "discovery", "ecosystem", "frogs", "galaxies", "horizon", "innovation", "jumpstart", "kinetic", "landscape", 
        "meteorology", "navigation", "oasis", "paleontology", "quirky", "rocks", "science", "trail", "utopia", 
        "velocity", "whirlwind", "xerox", "yodel", "zephyr", "artwork", "boulders", "craftsman", "detour", "electronics", 
        "floral", "garden", "highlands", "iceberg", "jewelry", "kayak", "lagoon", "mountains", "nautical", "outdoor", 
        "painting", "quartz", "rafting", "scenery", "tourism", "utensil", "viewpoint", "wilderness", "xenon", "yarn", 
        "zipper", "adventure", "bungee", "canyon", "dolphin", "expedition", "fossil", "gale", "horizon", "inlet", 
        "journey", "kayaking", "lake", "meadow", "navigation", "oceanic", "parachute", "quiver", "river", "skyline", 
        "tundra", "utopia", "volcano", "waterfall", "xenon", "yawn", "zephyr", "acrobatic", "baseball", "carnival", 
        "doodle", "ecosystem", "festival", "gardener", "helium", "invention", "jumping", "kickball", "landscape", 
        "magic", "nurture", "observe", "puzzle", "quest", "robotics", "surfing", "teleport", "underwater", "virtual", 
        "windsurf", "xerox", "yoyo", "zigzag", "artistic", "backpack", "creation", "discover", "earthquake", "fossils", 
        "galaxy", "hover", "idea", "juggle", "kale", "lightning", "mechanical", "navigational", "orbit", "planet", 
        "quasar", "rock", "stellar", "telescope", "unicorn", "voyager", "whale", "xenon", "yoga", "zipper", "adventurous"
    ],
    'hard': [
        "hippopotamus", "archaeology", "encyclopedia", "rhinoceros", "psychiatrist", "veterinarian", "biotechnology", 
        "counterintuitive", "discombobulated", "extraterrestrial", "fossilization", "gastroenterologist", "hippocampus", 
        "immunohistochemistry", "jurisprudence", "kleptomania", "laryngoscope", "metamorphosis", "neuroplasticity", 
        "osteoporosis", "paleontologist", "quantitative", "radiography", "subconscious", "thermodynamics", 
        "utilitarianism", "ventriloquism", "whimsicality", "xenotransplantation", "yesteryear", "zooplankton", 
        "abstemious", "bibliography", "circumlocution", "dendrochronology", "electrophoresis", "fluoroscopically", 
        "gastronomy", "hexadecimal", "ichthyology", "juxtaposition", "kaleidoscope", "lexicographical", 
        "multidisciplinary", "nanotechnology", "ornithologist", "pharmacodynamics", "quintessential", 
        "radiotelegraphy", "spectrophotometer", "telecommunications", "uncharacteristically", "vexillology", 
        "wunderkind", "xylophonist", "yellowtail", "zoogeography", "anesthesiologist", "biomechanics", "cholecystectomy", 
        "dermatopathology", "endocrinology", "fibrinolysis", "gastroenteritis", "hematopoiesis", "infrastructure", 
        "jurisdiction", "kleptocracy", "liposuction", "microbiologist", "nephrologist", "ophthalmology", "psychotherapy", 
        "quarantine", "rehabilitation", "sociolinguistics", "thermochemistry", "ultrasonography", "venipuncture", 
        "wastewater", "xenobiotics", "yellowstone", "zoonosis", "agriculture", "bibliophile", "cryptography", 
        "differentiation", "electroencephalography", "forensic", "gravitational", "hydrodynamics", "infrastructure", 
        "jurisdiction", "kinesiology", "lithosphere", "metallurgy", "neurology", "oncology", "pathology", "quasars", 
        "radiology", "seismology", "topography", "ultrasound", "vector", "waveform", "xanthophyll", "yottabyte", 
        "zygote", "algorithm", "biochemistry", "cytoplasm", "dermatology", "evolutionary", "fluorescence", 
        "genomics", "herbivorous", "invertebrate", "jurisprudence", "kinetics", "leukocytes", "macroeconomics", 
        "neurosurgery", "optometry", "paleontology", "quaternary", "recombination", "spectroscopy", "taxidermy", 
        "ultraviolet", "veterinary", "wavelength", "xenon", "yottabyte", "zoonotic", "acoustics", "biotechnology", 
        "cellulose", "diffraction", "ethnobotany", "fluctuation", "genotype", "hypothesis", "introspection", 
        "jurisprudence", "kinetics", "lymphocytes", "metabolism", "neurotransmitter", "oxidation", "phylogenetics", 
        "quantum", "retrovirus", "synchronization", "thermodynamics", "unobservable", "vibration", "wavelength", 
        "xenon", "yield", "zoology", "astronomy", "biome", "chlorophyll", "decomposition", "ecology", "fluorocarbon", 
        "geophysics", "hematology", "immunology", "jurisprudence", "karyotype", "lysosome", "metamorphosis", 
        "neutron", "oscillation", "polypeptide", "quarantine", "resonance", "sublimation", "taxonomy", "ultrasound", 
        "vortex", "wavelength", "xenon", "yield", "zooplankton", "anatomy", "biomechanics", "chromosome", "diffusion", 
        "endocrine", "fluorescent", "geology", "hormone", "isotope", "jurisprudence", "kinematics", "lipid", 
        "molecular", "neuron", "osmosis", "photosynthesis", "quark", "radiation", "spectrum", "tetrahedron", 
        "universe", "vector", "wavelength", "xenon", "yield", "zymurgy", "allometry", "biophysics", "cladogram", 
        "dendrite", "eukaryote", "fermentation", "genome", "homeostasis", "interference", "jurisprudence", "kinetic", 
        "luminescence", "mutation", "nucleic", "osmosis", "phenotype", "quark", "receptor", "symbiosis", "transcription", 
        "ultraviolet", "voltage", "wavelength", "xenon", "yield", "zygomorphic", "allele", "biodiversity", 
        "cytoplasmic", "dehydrogenase", "enzymatic", "fluorine", "genetics", "heredity", "ionization", "jurisprudence", 
        "karyotype", "ligase", "morphogenesis", "nucleotide", "oxidative", "phytoplankton", "quantum", "ribosome", 
        "synapse", "telomere", "undergraduate", "vaccine", "waterfall", "xylem", "yield", "zygospore", "acceleration", 
        "biosynthesis", "chloroplast", "dichotomy", "equilibrium", "fossilization", "geochemical", "hydrogen", 
        "interstellar", "jurisprudence", "karyokinesis", "lichen", "magnetosphere", "nucleotide", "oxidation", 
        "phosphorylation", "quark", "resonance", "synergistic", "turbulence", "ultrastructure", "viscosity", 
        "waveform", "xenogenesis", "yield", "zoological"
    ]
}


# A list to store words that are hard to pronounce
word_bank = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word', methods=['POST'])
def get_word():
    data = request.get_json()
    difficulty = data.get('difficulty')
    if difficulty not in words:
        return jsonify({'error': 'Invalid difficulty level'}), 400
    word = random.choice(words[difficulty])
    return jsonify({'word': word})

@app.route('/get_similar_words', methods=['POST'])
def get_similar_words():
    data = request.get_json()
    syllable = data.get('syllable')
    similar_words = [word for difficulty_words in words.values() for word in difficulty_words if syllable in word]
    if not similar_words:
        similar_words = ["No similar words found."]
    word = random.choice(similar_words)
    return jsonify({'word': word})

@app.route('/word_bank', methods=['GET'])
def get_word_bank():
    return jsonify({'word_bank': word_bank})

@app.route('/add_to_word_bank', methods=['POST'])
def add_to_word_bank():
    data = request.get_json()
    word = data.get('word')
    if word and word not in word_bank:
        word_bank.append(word)
    return jsonify({'status': 'success'})

@app.route('/remove_from_word_bank', methods=['POST'])
def remove_from_word_bank():
    data = request.get_json()
    word = data.get('word')
    if word in word_bank:
        word_bank.remove(word)
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
