class BowlingGame:
    def __init__(self):
        """
        This function initates the code and creates a list.
        """
        self.rolls = []

    def roll(self,pins):
        """
        This function takes the list we just made and adds the number of knocked over pins to the list.
        """
        self.rolls.append(pins)

    def score(self):
        """
        This function calculates the number of points the player needs to add to their score.
        It takes into account if it was a spare/strike.

        Args:
        (result) Type = int
        This is the number of points the player has.
        (rollIndex) Type = int
        This is the number of rolls that has been done by the player.

        Return:
        Type = int
        This returns the result, making sure it has been changed if there is a spare/strike.
        """
        result = 0
        rollIndex = 0

        for frameIndex in range(10):

            if frameIndex in range(10):
                result += self.strikeScore(rollIndex)
                rollIndex += 1

            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2

            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2

            return result

    def isStrike(self, rollIndex):
        """
        Return:
        Type = int
        This returns the score of the strike.
        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """
        Return:
        Type = int
        This returns the score of the spare.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10
    
    def strikeScore(self,rollIndex):
        """
        Return:
        Type = int
        This caclulates the score and bonuses you get from a strike and returns the overall score of the strike.
        """
        return  10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """
        Return:
        Type = int
        This caclulates the score and bonuses you get from a spare and returns the overall score of the spare.
        """
        return  10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Return:
        Type = int
        This caclulates the score and returns the score of the roll.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]