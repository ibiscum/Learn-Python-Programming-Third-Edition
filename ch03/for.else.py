class DriverException(Exception):
    pass


people = [('James', 18), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print(driver)
        break
else:
    raise DriverException('Driver not found.')
