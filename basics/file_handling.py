
# Reading File
with open('text.txt', 'r') as file:
    print(file.read())
    file.close()


# Writing File
with open('result.txt', 'w') as file:
    for i in range(5):
        name = input('Please input name of the winner {} :'.format(str(i+1)))
        file.write('Winner {}: {}\n'.format(str(i+1), name))

    file.close()

