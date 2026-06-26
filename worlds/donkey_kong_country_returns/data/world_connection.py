from rule_builder.rules import Rule
class WorldConnection:
    def __init__(self,
                 from_world_index: int,
                 to_world_index: int,
                 rule: Rule = None,
                 ):
        self.from_world_index = from_world_index
        self.to_world_index = to_world_index
        self.rule = rule
