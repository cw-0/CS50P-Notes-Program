try:
    print("\nHello")
    input("Pause ... ")
except KeyboardInterrupt:
    print(chr(8) + chr(8), end="")
    print("Interrupted by user")