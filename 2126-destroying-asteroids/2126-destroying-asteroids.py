class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        if mass+sum(asteroids[:-1])<asteroids[-1]:
            return False
        for x in asteroids:
            if mass>=x:
                mass+=x
            else:
                return False
        return True               