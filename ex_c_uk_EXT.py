united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

united_kingdom(["wales"]["capital"]) = "Cardiff"
print(united_kingdom)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
new_dictionary =
{
  "name" : "Nothern Ireland"
  "population" : "1,811,000"
  "capital" : "Belfast"
  united_kingdom.update(new_dictionary)


}
# 3. Use a loop to print the names of all the countries in the UK.

for name in united_kingdom
print(name)

# 4. Use a loop to find the total population of the UK.
for population in united_kingdom:
  total = 


