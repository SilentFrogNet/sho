class ShO:
    configured_shells = None

    def __init__(self, verbose=False):
        self.verbose = verbose
        self._setup()

    def _setup(self):
        self._load_shells()

    def _load_shells(self):
        self.configured_shells = [
            {
                'name': 'apio_demo',
                'host': '10.0.13.121',
                'is_ssh': True
            }
        ]

    def list(self):
        if not self.verbose:
            return [s['name'] for s in self.configured_shells]

        out = []
        for s in self.configured_shells:
            out.append(f"{'ssh' if s['is_ssh'] else 'local'} @ {s['name']} - {s['host']}")
