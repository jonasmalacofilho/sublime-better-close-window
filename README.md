BetterCloseWindow
=================

I got fed up with Sublime opening the last project and a new window when closed and being launched. This super-simple plugin offers `better_close_window` and `better_exit` commands, that first close the project and all open files and then the window/application.

Default keybinding is set to override the default `close_window` and `exit` commands.

## Before

1. Work on a `foo.sublime-project` or a folder.
2. Close sublime
3. Start sublime opening a folder/project. `subl ~/bar`
4. Two sublime windows open - first with the `foo` project, second with `~/bar` folder.

## Now

1. Work on a `foo.sublime-project` or a folder.
2. Close sublime via this plugin
3. Start sublime opening a folder/project. `subl ~/bar`
4. A single sublime window opens - with `~/bar` folder.
