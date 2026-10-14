print("===== COCOMO MODEL =====")
print("Project: Parcel Tracking System")

# Estimated project size in KLOC
kloc = float(input("Enter project size (in KLOC): "))

# Basic COCOMO - Organic Mode
a = 2.4
b = 1.05
c = 2.5
d = 0.38

# Effort estimation in person-months
effort = a * (kloc ** b)

# Development time in months
development_time = c * (effort ** d)

# Average team size
team_size = effort / development_time

# Display results
print("\n===== ESTIMATION RESULTS =====")
print(f"Project Size       : {kloc} KLOC")
print(f"Effort             : {effort:.2f} person-months")
print(f"Development Time   : {development_time:.2f} months")
print(f"Average Team Size  : {team_size:.0f} developers")

print("\nCOCOMO estimation completed successfully!")

