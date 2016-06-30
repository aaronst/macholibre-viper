# Viper module for macholibre
# https://github.com/aaronst/macholibre.git
# Aaron Stephens (aaron@icebrg.io)


from viper.common.abstracts import Module
from viper.core.session import __sessions__
from macholibre import macholibre


class MachOLibreModule(Module):
    cmd = 'macholibre'
    description = 'Mach-O & Universal binary parser'
    authors = ['Aaron Stephens (aaron@icebrg.io)']

    def __init__(self):
        super(MachOLibreModule, self).__init__()
        self.parser.add_argument('-p', '--path', action='store', help='Path to mach-o')
        self.parser.add_argument('-o', '--output', action='store', help='Path for JSON output')

    def run(self):
        super(MachOLibreModule, self).run()
        if self.args.output or self.args.path:
            if self.args.output is not None:
                out = open(self.args.output, 'w')
                if self.args.path is not None:
                    macholibre.parse(self.args.path, f=out)
                    self.log('success', 'Done')
                else:
                    try:
                        macholibre.parse(str(__sessions__.current.file.path), f=out)
                    except AttributeError:
                        self.log('error', 'No file open and no path specified')
                    self.log('success', 'Done')
            else:
                self.log('success', macholibre.parse(self.args.path))
        else:
            try:
                self.log('success', macholibre.parse(str(__sessions__.current.file.path)))
            except AttributeError:
                self.log('error', 'No file open and no path specified')

