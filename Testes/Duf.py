        if len(obstacles) == 0:
            if points < 1000:
                z = random.randint(0, 3)
                if z == 0:
                    obstacles.append(Cone(OBS2))
                elif z == 1:
                    obstacles.append(Barreira(OBS1))
                elif z == 2 or z == 3:
                    obstacles.append(Zero(ROCK))

            elif points >= 1000 and points < 2000:
                z2 = random.randint(0, 3)
                if z2 == 3:
                    obstacles.append(Naves(ROCK))
                elif z2 == 0:
                    obstacles.append(Cone(OBS2))
                elif z2 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z2 == 2:
                    obstacles.append(Zero(ROCK))

            elif points >= 2000 and points < 3000:
                z3 = random.randint(0, 5)
                if z3 == 3:
                    obstacles.append(Naves(ROCK))
                elif z3 == 0:
                    obstacles.append(Cone(OBS2))
                elif z3 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z3 == 5 or 2:
                    obstacles.append(Zero(ROCK))

            elif points >= 3000 and points < 4000:
                z4 = random.randint(0, 6)
                if z4 == 3:
                    obstacles.append(Naves(ROCK))
                elif z4 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z4 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z4 == 5 or 6:
                    obstacles.append(Zero(ROCK))


            elif points >= 4000 and points < 5000:
                z5 = random.randint(0, 7)
                if z5 == 3:
                    obstacles.append(Naves(ROCK))
                elif z5 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z5 == 1 or 7:
                    obstacles.append(Barreira(OBS1))
                elif z5 == 5 or 6:
                    obstacles.append(Zero(ROCK))

            elif points >= 5000 and points < 6000:
                z6 = random.randint(0, 8)
                if z6 == 3:
                    obstacles.append(Naves(ROCK))
                elif z6 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z6 == 1 or 7:
                    obstacles.append(Barreira(OBS1))
                elif z6 == 5 or 6 or z6 == 8:
                    obstacles.append(Zero(ROCK))

            elif points >= 7000:
                z7 = random.randint(0, 9)
                if z7 == 3 or z7 == 7:
                    obstacles.append(Naves(ROCK))
                elif z7 == 0:
                    obstacles.append(Cone(OBS2))
                elif z7 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z7 == 5 or z7 == 6:
                    obstacles.append(Zero(ROCK))