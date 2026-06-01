class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        newmass=mass
        for i in asteroids:
            if newmass<i:
                return False
            else:
                newmass+=i
        return True