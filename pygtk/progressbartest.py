import pygtk
pygtk.require('2.0')
import gtk


class MyProgressBar(gtk.ProgressBar):

    def __init__(self, *args, **kwargs):
        super(MyProgressBar, self).__init__(*args, **kwargs)

    def draw(self, *args, **kwargs):

        super(MyProgressBar, self).draw(*args, **kwargs)


class MainWin:

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        self.vbox = gtk.VBox()
        self.vbox.set_border_width(0)

        self.evbox = gtk.EventBox()
        self.evbox.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FFF'))
        self.evbox.modify_bg(gtk.STATE_ACTIVE, gtk.gdk.Color('#FFF'))

        # create a progress bar
        self.progressbar = MyProgressBar()
        self.progressbar.set_fraction(0.50)

        self.evbox.add(self.progressbar)
        self.vbox.add(self.evbox)

        self.window.add(self.vbox)
        self.window.show_all()
        import ipdb; ipdb.set_trace()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    MainWin().main()
