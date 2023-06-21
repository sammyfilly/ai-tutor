class Section:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Plan:
    def __init__(self, sections=None):
        if sections is None:
            self.sections = []
        else:
            self.sections = sections
        self.current_index = 0

    def next(self):
        if self.current_index < len(self.sections):
            next_section = self.sections[self.current_index]
            self.current_index += 1
            return next_section
        else:
            print("No more sections.")
            return None