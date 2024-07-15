# main.py

from material_generator import generate_material

def main():
    print("Welcome to the Speech Language Pathologist App")
    print("Please select the difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        difficulty = 'easy'
    elif choice == '2':
        difficulty = 'medium'
    elif choice == '3':
        difficulty = 'hard'
    else:
        print("Invalid choice")
        return

    words = generate_material(difficulty)
    print(f"\nGenerated words for {difficulty} difficulty level:")
    for word in words:
        syllables = '-'.join([char for char in word])
        print(syllables)
    
    combine_choice = input("\nWould you like to combine the syllables to form the words? (yes/no): ").strip().lower()
    if combine_choice == 'yes':
        print("\nCombined words:")
        for word in words:
            print(word)

if __name__ == "__main__":
    main()
