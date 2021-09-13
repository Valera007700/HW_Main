while True:

    input_data = int(input("Enter BYN money"))

    if input_data <= 0:
        print("Enter money above 0")
        continue

    bun_to_usd = int(input_data) / 2.5

    print("USD = ", bun_to_usd)



