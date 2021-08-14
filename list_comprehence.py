#extract first name
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_name = [name.split()[0].lower() for name in names]
# print(first_name)

# multiply by 3 in first 20
# multiples_3 = [x*3 for x in range(1,21)]
# print(multiples_3)

# scores = {
#              "Rick Sanchez": 70,
#              "Morty Smith": 35,
#              "Summer Smith": 82,
#              "Jerry Smith": 23,
#              "Beth Smith": 98
#           }
# passed = [name for name, score in scores.items() if score>=65]
#
# print(passed)

int[] numbers = new int[]{1,2,3,4};
int result = 0;
for (int number : numbers) {
    result *- number;
}