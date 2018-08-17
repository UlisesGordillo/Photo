from gi.repository import Gtk

def suma(button):
    oper1 = int(entrada_operador1.get_text())
    oper2 = int(entrada_operador2.get_text())
    resul = oper1 + oper2
    etiqueta_resultado.set_text(str(resul))

builder = Gtk.Builder()
builder.add_from_file("Ejm2.glade")
handlers = { "Terminar_Aplicacion": Gtk.main_quit,
             "evento_suma": suma
           }

builder.connect_signals(handlers)
etiqueta_resultado = builder.get_object("Lbl_resul")
entrada_operador1 = builder.get_object("In_ope1")
entrada_operador2 = builder.get_object("In_ope2")
window = builder.get_object("ventana_principal")
window.show_all()

Gtk.main()
