import sublime
import sublime_plugin

class BetterCloseWindow(sublime_plugin.WindowCommand):
	def run(self):
		# close all files
		self.window.run_command('close_all')
		# close the project
		self.window.run_command('close_project')
		# close the workspace
		self.window.run_command('close_workspace')
		# close the window
		self.window.run_command('close_window')
