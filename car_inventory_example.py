inventories = {
    'Toyota':{ 
    'Camry', 'Yaris', 'Corolla','Supra','Tacoma'},
    'Chevrolet':{ 
    'Camaro', 'Spark', 'Tahoe','Malibu','Traverse'}
}
active = True

while True:
    prompt = 'What kind of car rental would you like?: '
    manufact = input(prompt)
    if manufact in inventories.keys():
        print("Manufacturer: " + manufact + '\nModels:')
        for car in inventories[manufact]:
            print('\t ' + car)
        while True:
            prompt = "What selected model, from the list, would you like? "
            models = input(prompt)
            if models in inventories[manufact]:
                print("excellent choice")
                print("Final selection, " + manufact + ':' + models)
                break
            else:
                print("That is not a " + manufact + " model.")
                continue
    else:
        print("Sorry that car type is not available")
        continue
    break
