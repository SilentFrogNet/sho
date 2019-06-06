import random


class Banners:
    DEFAULT_BANNER = "*************************************\n" \
                     "*        _____ _      ____          *\n" \
                     "*       / ____| |    / __ \         *\n" \
                     "*      | (___ | |__ | |  | |        *\n" \
                     "*       \___ \| '_ \| |  | |        *\n" \
                     "*       ____) | | | | |__| |        *\n" \
                     "*      |_____/|_| |_|\____/         *\n" \
                     "*                                   *\n" \
                     "* ShO - Shell Orchestrator          *\n" \
                     "* Ilario Dal Grande                 *\n" \
                     "* http://silentfrog.net             *\n" \
                     "* ilario.dalgrande@silentfrog.net   *\n" \
                     "*************************************\n"

    @classmethod
    def get_random_banner(cls, version=None):
        banners = [cls.DEFAULT_BANNER]

        str_banner = random.choice(banners)

        if not version:
            version = "1.0.0"
        return str_banner.format(version)
