import sublime, sublime_plugin

# Takes the focus to the last Tab in the current Group.
class PowerLastTabCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    views = window.views_in_group(window.active_group())
    window.focus_view(views[len(views) - 1])

# Takes the focus to the first Tab in the current Group.
class PowerFirstTabCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    views = window.views_in_group(window.active_group())
    window.focus_view(views[0])

# Takes the focus to the next Tab in the current Group.
class PowerNextTabCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    views = window.views_in_group(window.active_group())
    group, view_index = window.get_view_index(window.active_view())
    view_index += 1
    if view_index < len(views):
      window.focus_view(views[view_index])

# Takes the focus to the previous Tab in the current Group.
class PowerPreviousTabCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    views = window.views_in_group(window.active_group())
    group, view_index = window.get_view_index(window.active_view())
    view_index -= 1
    if view_index >= 0:
      window.focus_view(views[view_index])
