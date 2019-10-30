class Scientist:
    def __init__(self, name, field, country):
        self.name = name
        self.field = field
        self.country = country
    def scientist_details(self):
        return f" The name of scientist is {self.name}, field is {self.field} and country is {self.country}"

#inheritance
class Researcher(Scientist):
    def __init__(self, name, field, country, research_field):
        self.name = name
        self.field = field
        self.country = country
        self.research_field = research_field
    def research_details(self):
        return f" researchers fields are {self.research_field}"
        
scientist1 = Scientist("Isaac Newton", "Physsicist", "England")
scientist2 = Scientist("Einstin", "Theory of Relativity", "Germany")
scientist3 = Researcher("Charls", "Chemisist", "France", ["charl's law", "V = kT"])
scientist4 = Researcher("pascal", "fluid Mechanics", "England", ["Pascal's law", "P=F/A"] )

print(scientist1.scientist_details())
print(scientist3.research_details())
print(scientist4.scientist_details())
