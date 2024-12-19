print("Siege Attacker or Defender?")
name = input("Insert Siege characters name: ").strip().capitalize()

match name:
    case "Ash":
        print("Attacker")
    case "Ace":
        print("Attacker")
    case "Blitz":
        print("Attacker")
    case "Rook":
        print("Defender")
    case "Bandit":
        print("Defender")
    case "Clash":
        print("Defender")

# A way to simplify this would be
    case "Nomad" | "Buck" | "Kali":
        print("Attacker")
    case "Mozzie" | "Lesion" | "Castle":
        print("Defender")

# case _: is for anything typed that isnt found in match like an else statement
    case _:
        print("Siege character not found. Please check your spelling.")