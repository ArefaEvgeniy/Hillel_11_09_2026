from collections import namedtuple


plane_1_1 = ("Boeing", "747", 2010, 400, "ER-45624")
plane_1_2 = ("Airbus", "A380", 2015, 380, "LV-9987")
plane_1_3 = ("Cessna", "172", 2005, 4, "AB-1234")
plane_1_4 = ("Embraer", "E195", 2018, 120, "EM-5678")

planes_1 = [plane_1_1, plane_1_2, plane_1_3, plane_1_4]

sits = 300
for plane in planes_1:
    if plane[2] > sits:
        print(plane[-1])

print("---------------------")

plane_2_1 = {
    "manufacturer": "Boeing",
    "model": "747",
    "year": 2010,
    "sits": 400,
    "registration": "ER-45624"
}
plane_2_2 = {
    "manufacturer": "Airbus",
    "model": "A380",
    "year": 2015,
    "sits": 380,
    "registration": "LV-9987"
}
plane_2_3 = {
    "manufacturer": "Cessna",
    "model": "172",
    "year": 2005,
    "sits": 4,
    "registration": "AB-1234"
}
plane_2_4 = {
    "manufacturer": "Embraer",
    "model": "E195",
    "year": 2018,
    "sits": 120,
    "registration": "EM-5678"
}

planes_2 = [plane_2_1, plane_2_2, plane_2_3, plane_2_4]

sits = 300
for plane in planes_2:
    if plane["sits"] > sits:
        print(plane["registration"])

print("---------------------")

Plane = namedtuple("Plane", ["manufacturer", "model", "year", "sits", "registration"])

plane_3_1 = Plane("Boeing", "747", 2010, 400, "ER-45624")
plane_3_2 = Plane("Airbus", "A380", 2015, 380, "LV-9987")
plane_3_3 = Plane("Cessna", "172", 2005, 4, "AB-1234")
plane_3_4 = Plane("Embraer", "E195", 2018, 120, "EM-5678")

planes_3 = [plane_3_1, plane_3_2, plane_3_3, plane_3_4]

sits = 300
for plane in planes_3:
    if plane.sits > sits:
        print(plane.registration)
