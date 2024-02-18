class Game:
    def __init__(self):
        self.levels = {
            'Local': {'Public Health': 50, 'Local Economy': 50, 'Community Happiness': 50},
            'Regional': {'Infrastructure': 50, 'Environmental Health': 50, 'Social Cohesion': 50},
            'Global': {'Global Economy': 50, 'Climate Change': 50, 'International Relations': 50}
        }

    def display_status(self):
        for level, stats in self.levels.items():
            print(f"{level} Level:")
            for category, value in stats.items():
                print(f" {category}: {value}")
            print()

    def apply_influence(self, source_level, target_level, influence):
        for category, influence_value in influence.items():
            if category in self.levels[target_level]:
                self.levels[target_level][category] += influence_value
                print(f"Influence from {source_level} to {target_level}: {category} += {influence_value}")

    def make_decision(self, decision):
        if decision == '1':
            # Local decision impacts
            self.levels['Local']['Public Health'] += 10
            # Influence Regional level
            self.apply_influence('Local', 'Regional', {'Environmental Health': 5})
        elif decision == '2':
            # Regional decision impacts
            self.levels['Regional']['Social Cohesion'] += 10
            # Influence Global level
            self.apply_influence('Regional', 'Global', {'International Relations': -5})

        # Dynamic inter-level influence based on conditions
        if self.levels['Regional']['Environmental Health'] > 60:
            self.apply_influence('Regional', 'Global', {'Climate Change': -10})
        if self.levels['Global']['International Relations'] < 40:
            self.apply_influence('Global', 'Local', {'Community Happiness': -10})

    def run(self):
        while True:
            self.display_status()
            decision = input("Make a decision (1/2, 'exit' to quit): ")
            if decision.lower() == 'exit':
                break

            self.make_decision(decision)

if __name__ == "__main__":
    enhanced_game = Game()
    enhanced_game.run()