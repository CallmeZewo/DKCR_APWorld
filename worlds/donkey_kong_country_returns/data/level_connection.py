from rule_builder.rules import Rule
class LevelConnection:
    def __init__(self,
                 from_level_index: int,
                 to_level_index: int,
                 rule: Rule = None,
                 ):
        self.from_level_index = from_level_index
        self.to_level_index = to_level_index
        self.rule = rule
