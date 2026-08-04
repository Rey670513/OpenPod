from .base import BaseGenerator


class ModernRock(BaseGenerator):

    def __init__(self):
        super().__init__("richie_sambora.pgp")

        #
        # Snapshot
        #

        self.snapshots[0].name = "Crystal Clean"
        self.snapshots[1].name = "Warm Crunch"
        self.snapshots[2].name = "Arena Rhythm"
        self.snapshots[3].name = "Arena Lead"

        #
        # Amp
        #

        self.amp.drive = 0.74

        #
        # Cab
        #

        self.cab.high_cut = 7000
        self.cab.low_cut = 90
        from .base import BaseGenerator


class ModernRock(BaseGenerator):
    """
    Modern Rock preset generator.
    """

    def __init__(self):
        super().__init__("richie_sambora.pgp")

        # Snapshot
        self.snapshots[0].name = "Crystal Clean"
        self.snapshots[1].name = "Warm Crunch"
        self.snapshots[2].name = "Arena Rhythm"
        self.snapshots[3].name = "Arena Lead"

        # Amp
        self.amp.drive = 0.74

        # Cab
        self.cab.high_cut = 7000
        self.cab.low_cut = 90
        