import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        # Zugriff auf die aktuelle Anwendung und Benutzeroberfläche
        app = adsk.core.Application.get()
        ui = app.userInterface
        
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
        for body in bodies:
            if body.isSolid:
                # Volumen auslesen
                volume = body.physicalProperties.volume
                
                # Oberfläche auslesen
                surface_area = body.physicalProperties.area
                
                # Schwerpunkt auslesen
                center_of_mass = body.physicalProperties.centerOfMass
                center_of_mass_str = f"({center_of_mass.x:.6f}, {center_of_mass.y:.6f}, {center_of_mass.z:.6f})"
                
                # Materialeigenschaften auslesen
                material = body.material
                material_name = material.name if material else "Kein Material zugewiesen"
                
                # Massen- und Trägheitseigenschaften auslesen
                mass = body.physicalProperties.mass
                inertia_tensor = body.physicalProperties.getXYZMomentsOfInertia()
                inertia_str = f"Ixx={inertia_tensor[0]:.6f}, Iyy={inertia_tensor[1]:.6f}, Izz={inertia_tensor[2]:.6f}"
                
                # Anzahl der Flächen, Kanten und Scheitelpunkte
                num_faces = body.faces.count
                num_edges = body.edges.count
                num_vertices = body.vertices.count
                
                # Flächeninformationen
                face_info = []
                for face in body.faces:
                    face_type = face.geometry.surfaceType
                    face_area = face.area
                    face_info.append(f"Fläche: Typ={face_type}, Fläche={face_area:.6f} cm^2")
                
                # Kanteninformationen
                edge_info = []
                for edge in body.edges:
                    edge_length = edge.length
                    edge_info.append(f"Kante: Länge={edge_length:.6f} cm")
                
                # Scheitelpunktinformationen
                vertex_info = []
                for vertex in body.vertices:
                    vertex_coords = f"({vertex.geometry.x:.6f}, {vertex.geometry.y:.6f}, {vertex.geometry.z:.6f})"
                    vertex_info.append(f"Scheitelpunkt: Koordinaten={vertex_coords}")
                
                # Informationen formatieren
                result = (f'Körper: {body.name}\n'
                          f'Volumen: {volume:.6f} cm^3\n'
                          f'Oberfläche: {surface_area:.6f} cm^2\n'
                          f'Schwerpunkt: {center_of_mass_str}\n'
                          f'Material: {material_name}\n'
                          f'Masse: {mass:.6f} g\n'
                          f'Trägheitsmomente: {inertia_str}\n'
                          f'Anzahl der Flächen: {num_faces}\n'
                          f'Anzahl der Kanten: {num_edges}\n'
                          f'Anzahl der Scheitelpunkte: {num_vertices}\n'
                          f'Flächeninformationen:\n' + "\n".join(face_info) + '\n'
                          f'Kanteninformationen:\n' + "\n".join(edge_info) + '\n'
                          f'Scheitelpunktinformationen:\n' + "\n".join(vertex_info))
                
                # Ergebnis anzeigen
                ui.messageBox(result)
                
    except:
        if ui:
            ui.messageBox('Fehler: {}'.format(traceback.format_exc()))

# Das Skript ausführen
run(None)
