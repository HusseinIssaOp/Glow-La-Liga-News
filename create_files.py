import os
import random

def generate_text():

    topics = [  # I collected random topics
        "Real Madrid secured a crucial win against Barcelona in the latest La Liga match.",
        "Atletico Madrid's star striker scored a hat-trick in their recent victory.",
        "Sevilla FC announced the signing of a promising young talent from South America.",
        "Barcelona's manager expressed confidence in the team's ability to bounce back from recent losses.",
        "Valencia FC faced criticism following their disappointing performance against bottom-ranked teams.",
        "La Liga officials introduced new regulations aimed at promoting fair play and sportsmanship.",
        "Real Sociedad climbed to the top of the La Liga table after a series of impressive wins.",
        "Athletic Bilbao's goalkeeper sustained an injury during training, casting doubt on his availability for upcoming matches.",
        "FC Barcelona is reportedly in talks with a top European manager to replace their current coach.",
        "Real Madrid's young midfielder received praise for his exceptional performance in the last match.",
        "Atletico Madrid's captain expressed optimism about their chances of winning the La Liga title this season.",
        "Sevilla FC's supporters are thrilled with the team's recent run of form.",
        "Valencia FC is rumored to be targeting several high-profile signings in the upcoming transfer window.",
        "Getafe CF's manager criticized the team's lack of consistency in recent games.",
        "Espanyol secured a vital victory in their battle to avoid relegation from La Liga.",
        "Villarreal CF's striker is leading the race for the Pichichi Trophy with an impressive goal-scoring record.",
        "Real Betis unveiled plans for a major stadium renovation project to enhance fan experience.",
        "Granada CF shocked fans with a stunning comeback win against a top-ranked opponent.",
        "Levante UD's defender is attracting interest from several big clubs after his standout performances.",
        "Cadiz CF's relegation battle suffered a setback with a string of defeats in crucial matches.",
        "SD Huesca's coach emphasized the importance of team unity in their fight against relegation.",
        "Alaves is considering a change in leadership after a disappointing season so far.",
        "Elche CF's goalkeeper won plaudits for his heroic saves in the recent match."
    ]

    text = ' '.join(random.choices(topics, k=100))
    return text

task_folder = "Task1" # here i created the folder
os.makedirs(task_folder, exist_ok=True)


for i in range(1, 201): # 200 text file ??
    filename = os.path.join(task_folder, f"{i}.txt")
    with open(filename, 'w') as file:
        file.write(generate_text())
