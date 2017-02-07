import sublime, sublime_plugin

class PowerLastTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        views = window.views_in_group(window.active_group())
        if len(views) >= 9:
          window.focus_view(views[9])
        else:
          window.focus_view(views[-1])

class PowerFirstTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        views = window.views_in_group(window.active_group())
        window.focus_view(views[0])

class PowerNextTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        views = window.views_in_group(window.active_group())
        view = window.get_view_index(self.window.active_view)
        view = view + 1
        if view < views:
          window.focus_view(views[view])

class PowerPreviousTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        view = window.get_view_index(self.window.active_view)
        view = view - 1
        if view > 0:
          window.focus_view(views[view])
