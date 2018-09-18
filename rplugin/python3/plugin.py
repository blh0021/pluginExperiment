import neovim

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('HelloWorld', range='', nargs='*', sync=True)
    def commandHandler(self, args, range):
        self.vim.command('echo "Hello World"')
