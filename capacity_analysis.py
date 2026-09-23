team_capacity = {
    "Alex": 7,
    "Jordan": 6,
    "Taylor": 9,
    "Morgan": 5,
    "Casey": 7,
    "Riley": 3
}

print ("Team Capacity Report")
for team_member, active_projects in team_capacity.items():
    print(team_member, "has", active_projects, "active projects.")