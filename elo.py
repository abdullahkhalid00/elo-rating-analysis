class Elo:
    def __init__(self, base_elo = 1500):
        self.base_elo = base_elo

    def calculate_elo(self, p1, p2, result, K=32):
        r1 = self.base_elo
        r2 = self.base_elo

        e_r1 = 1 / (1 + 10 ** ((r2 - r1) / 400))
        e_r2 = 1 / (1 + 10 ** ((r1 - r2) / 400))

        elo_p1 = r1 + K * (result - e_r1)
        elo_p2 = r2 + K * (result - e_r2)

        return elo_p1, elo_p2