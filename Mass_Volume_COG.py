import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        # Zugriff auf die aktuelle Anwendung und Benutzeroberfläche
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Zugriff auf das aktive Produkt (Design)
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        
        # Überprüfen, ob ein Design geöffnet ist
        if not design:
            ui.messageBox('Bitte öffnen Sie ein Design, bevor Sie das Skript ausführen.')
            return
        
        # Zugriff auf die Root-Komponente des Designs
        rootComp = design.rootComponent
        
        # Schleife durch alle Körper in der Root-Komponente
        bodies = rootComp.bRepBodies
        results = []
        for body in bodies:
            if body.isSolid:
                # Volumen auslesen
                volume = body.physicalProperties.volume
                
                # Oberfläche auslesen
                surface_area = body.physicalProperties.area
                
                # Schwerpunkt auslesen
                center_of_mass = body.physicalProperties.centerOfMass
                center_of_mass_str = f"({center_of_mass.x:.6f}, {center_of_mass.y:.6f}, {center_of_mass.z:.6f})"
                
                # Informationen formatieren
                result = (f'Körper: {body.name}\n'
                          f'Volumen: {volume:.6f} cm^3\n'
                          f'Oberfläche: {surface_area:.6f} cm^2\n'
                          f'Schwerpunkt: {center_of_mass_str}')
                results.append(result)
        
        # Ergebnisse anzeigen
        ui.messageBox('\n\n'.join(results))
                
    except:
        if ui:
            ui.messageBox('Fehler: {}'.format(traceback.format_exc()))

# Das Skript ausführen
run(None)
