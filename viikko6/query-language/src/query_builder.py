from matchers import All, And, Or, Not, PlaysIn, HasFewerThan, HasAtLeast

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def oneOf(self, *matchers):
        return QueryBuilder(And(self._matcher, Or(*matchers)))

    def invert(self):
        return QueryBuilder(Not(self._matcher))

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
