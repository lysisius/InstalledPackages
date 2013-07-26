from sublime_plugin import WindowCommand
import sublime

class PluginListCommand(WindowCommand):
    def run(self):
        view = self.window.new_file()
        edit = view.begin_edit()

        installed_packages = self.get_installed_packages()
        packages = '\n'.join(map(str, installed_packages))

        view.insert(edit, 0, packages)
        view.end_edit(edit)

    def get_installed_packages(self):
        settings = sublime.load_settings('Package Control.sublime-settings')
        if not settings.has('installed_packages'):
            sublime.error_message("Could not find list of installed packages. Are you using Package Control?")
        packages = settings.get('installed_packages', [])
        if not packages:
            sublime.error_message("You don't have any plugins installed. Upgrade Away!")
        return packages

