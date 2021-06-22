import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="SMTP Send Test")

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        host_port_box = Gtk.Box(spacing=10)
        host_port_box.set_homogeneous(False)
        host_label = Gtk.Label(label="SMTP Host")
        host_entry = Gtk.Entry()
        host_port_box.pack_start(host_label, False, False,0)
        host_port_box.pack_start(host_entry, False, False,0)
        port_label = Gtk.Label(label="SMTP Port")
        port_entry = Gtk.Entry() 
        host_port_box.pack_start(port_label, False, False,0)
        host_port_box.pack_start(port_entry, False, False,0)
        self.main_box.pack_start(host_port_box, False, False,0)

        user_pass_box = Gtk.Box(spacing=10)
        user_pass_box.set_homogeneous(False)
        user_label = Gtk.Label(label="SMTP User")
        user_entry = Gtk.Entry()
        user_pass_box.pack_start(user_label, False, False,0) 
        user_pass_box.pack_start(user_entry, False, False,0)
        pass_label = Gtk.Label(label="SMTP Pass")
        pass_entry = Gtk.Entry()
        user_pass_box.pack_start(pass_label, False, False,0)
        user_pass_box.pack_start(pass_entry, False, False,0)
        self.main_box.pack_start(user_pass_box, False, False,0)

        ssl_box = Gtk.Box(spacing=10)
        ssl_box.set_homogeneous(False)
        ssl_label = Gtk.Label(label="SSL/TLS")
        ssl_box.pack_start(ssl_label, False, False,0)
        ssl_select = Gtk.ListStore(int, str)
        ssl_select.append([1, "NONE"])
        ssl_select.append([2, "SSL/TLS"])
        ssl_combo = Gtk.ComboBox.new_with_model_and_entry(ssl_select)
        ssl_combo.connect("changed", self.on_ssl_combo_changed)
        ssl_combo.set_entry_text_column(1)
        ssl_box.pack_start(ssl_combo, False, False, 0)
        self.main_box.pack_start(ssl_box, False, False,0)

        from_to_box = Gtk.Box(spacing=10)
        from_to_box.set_homogeneous(False)
        from_label = Gtk.Label(label="From Address")
        from_entry = Gtk.Entry()
        from_to_box.pack_start(from_label, False, False,0)
        from_to_box.pack_start(from_entry, False, False,0)
        to_label = Gtk.Label(label="To Address")
        to_entry = Gtk.Entry()
        from_to_box.pack_start(to_label, False, False,0)
        from_to_box.pack_start(to_entry, False, False,0)
        self.main_box.pack_start(from_to_box, False, False,0)

        cc_bcc_box = Gtk.Box(spacing=10)
        cc_bcc_box.set_homogeneous(False)
        cc_label = Gtk.Label(label="CC Address")
        cc_entry = Gtk.Entry()
        cc_bcc_box.pack_start(cc_label, False, False,0)
        cc_bcc_box.pack_start(cc_entry, False, False,0)
        bcc_label = Gtk.Label(label="BCC Address")
        bcc_entry = Gtk.Entry()
        cc_bcc_box.pack_start(bcc_label, False, False,0)
        cc_bcc_box.pack_start(bcc_entry, False, False,0)
        self.main_box.pack_start(cc_bcc_box, False, False,0)

        subj_label = Gtk.Label(label="Subject Line")
        subj_entry = Gtk.Entry()
        self.main_box.pack_start(subj_label, False, False,0)
        self.main_box.pack_start(subj_entry, False, False,0)

        body_label = Gtk.Label(label="Email Body")
        body_entry = Gtk.TextView()
        self.main_box.pack_start(body_label, False, False,0)
        self.main_box.pack_start(body_entry, False, False,0)

        xsettings_box = Gtk.Box(spacing=10)
        xsettings_box.set_homogeneous(False)
        
        self.main_box.pack_start(xsettings_box, False, False,0)
                
        uibuttons_box = Gtk.Box(spacing=10)
        uibuttons_box.set_homogeneous(False)
        
        self.main_box.pack_start(uibuttons_box, False, False,0)
        self.add(self.main_box)

    def on_ssl_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
