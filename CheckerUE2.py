import adsk.core, adsk.fusion, traceback
import csv
import os

# Vorgabewerte der Musterlösung
reference_body = {
    'name': 'Body1',
    'volume': 17.469597,
    'surface_area': 199.095916,
    'center_of_mass': (0.000008, 4.885446, 0.477482),
    'material': 'Steel',
    'mass': 0.137136,
    'inertia': (1.000000, 4.550505, 0.321375),
    'num_faces': 45,
    'num_edges': 92,
    'num_vertices': 64,
    'face_areas': [
        3.424515, 3.424515, 0.235619, 52.423301, 14.137167, 7.823792, 
        0.511451, 11.451105, 53.064194, 9.811913, 1.106547, 1.284327, 
        2.660000, 0.463495, 1.539380, 3.814535, 2.660000, 1.729049, 
        1.284327, 0.235619, 0.463495, 1.539380, 0.516717, 0.392284, 
        0.516717, 0.392284, 0.359992, 3.204503, 3.748718, 2.381511, 
        2.147562, 0.057267, 0.471239, 0.057267, 0.471239, 2.004577, 
        5.228180, 0.250236, 0.437931, 0.437931, 0.250236, 0.268701, 
        0.072197, 0.072197, 0.268701
    ],
    'edge_lengths': [
        0.250000, 3.800000, 0.250000, 0.500000, 0.883755, 2.800000, 
        0.883755, 0.500000, 0.250000, 3.800000, 0.250000, 0.500000, 
        0.883755, 2.800000, 0.883755, 0.500000, 0.942478, 0.942478, 
        9.424778, 3.800000, 1.999431, 3.800000, 1.999431, 9.424778, 
        4.153907, 8.412463, 3.141593, 0.785320, 0.785329, 0.742550, 
        0.828099, 8.482300, 0.605051, 0.605051, 8.482300, 2.199115, 
        1.099722, 1.099722, 0.337981, 3.800000, 0.337981, 3.800000, 
        0.700000, 3.800000, 0.700000, 3.800000, 1.754760, 0.337981, 
        1.727876, 0.700000, 2.199115, 2.199115, 3.800000, 2.199115, 
        1.099557, 3.800000, 1.099557, 3.800000, 0.700000, 3.800000, 
        2.199115, 3.800000, 1.727876, 3.800000, 0.337981, 0.942478, 
        0.942478, 1.754760, 0.600000, 0.785398, 0.600000, 0.785398, 
        1.499782, 1.499782, 0.900012, 0.900012, 1.999661, 2.634343, 
        2.523476, 2.110381, 0.785398, 0.000000, 0.785398, 0.000000, 
        0.115245, 0.115245, 0.115245, 0.115245, 0.070711, 0.070711, 
        0.070711, 0.070711
    ],
    'vertex_coordinates': [
        (0.300000, 3.000000, 2.200000), (0.300000, 3.000000, 2.450000),
        (0.300000, 6.800000, 2.450000), (0.300000, 6.800000, 2.200000),
        (0.300000, 6.300000, 2.200000), (0.300000, 6.300000, 1.316245),
        (0.300000, 3.500000, 1.316245), (0.300000, 3.500000, 2.200000),
        (-0.300000, 6.800000, 2.200000), (-0.300000, 6.800000, 2.450000),
        (-0.300000, 3.000000, 2.450000), (-0.300000, 3.000000, 2.200000),
        (-0.300000, 3.500000, 2.200000), (-0.300000, 3.500000, 1.316245),
        (-0.300000, 6.300000, 1.316245), (-0.300000, 6.300000, 2.200000),
        (0.000000, 2.295999, -1.500000), (-0.609375, 3.000000, 1.370643),
        (-0.609375, 6.800000, 1.370643), (0.609375, 6.800000, 1.370643),
        (0.609375, 3.000000, 1.370643), (0.000000, 8.500000, 1.500000),
        (0.000000, 0.707115, 0.661115), (0.000000, 1.751691, -1.338885),
        (0.000000, 0.162806, 0.500000), (0.353553, -0.000000, -0.353553),
        (-0.353547, 0.000000, -0.353559), (-0.353553, 0.000000, 0.353553),
        (0.322065, -0.000000, 0.382479), (0.000000, 8.500000, 1.350000),
        (0.000000, 2.044400, 1.350000), (0.000000, 0.503206, 0.350000),
        (-0.247487, 0.000000, -0.247487), (0.247487, -0.000000, 0.247487),
        (0.550000, 3.000000, 1.800000), (0.550000, 3.000000, 1.462019),
        (0.550000, 6.800000, 1.462019), (0.550000, 6.800000, 1.800000),
        (0.700000, 6.800000, 1.800000), (0.700000, 6.800000, 2.500000),
        (0.700000, 3.000000, 2.500000), (0.700000, 3.000000, 1.800000),
        (-0.550000, 6.800000, 1.462019), (-0.550000, 6.800000, 1.800000),
        (-0.700000, 6.800000, 1.800000), (-0.700000, 6.800000, 2.500000),
        (-0.700000, 3.000000, 2.500000), (0.350000, 3.000000, 2.500000),
        (-0.350000, 3.000000, 2.500000), (-0.350000, 6.800000, 2.500000),
        (0.350000, 6.800000, 2.500000), (-0.700000, 3.000000, 1.800000),
        (-0.550000, 3.000000, 1.800000), (-0.550000, 3.000000, 1.462019),
        (-0.125000, 6.800000, 2.200000), (-0.125000, 3.000000, 2.200000),
        (0.374850, -1.710092, -1.237626), (-0.375000, -2.290024, -0.762279),
        (0.225000, -2.174014, -0.857367), (-0.224910, -1.826055, -1.142575),
        (-0.125000, 3.000000, 1.600000), (-0.000000, 3.000000, 1.524892),
        (-0.125000, 6.800000, 1.600000), (0.000000, 6.800000, 1.524892)
    ]
}

def run(context):
    ui = None
    try:
        # Zugriff auf die aktuelle Anwendung und Benutzeroberfläche
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Fusionsdatendienst
        dataService = app.data

        # Projektname (ändern Sie diesen Wert entsprechend)
        project_name = 'NXtest'

        # Zugriff auf das Projekt
        projects = dataService.activeHub.dataProjects
        project = None
        for proj in projects:
            if proj.name == project_name:
                project = proj
                break

        if not project:
            ui.messageBox(f'Projekt nicht gefunden: {project_name}')
            return

        # Zugriff auf den Root-Ordner des Projekts
        root_folder = project.rootFolder

        # Liste der zu überprüfenden Dateien im Root-Ordner
        files_to_check = [item for item in root_folder.dataFiles if item.fileExtension == 'f3d']

        # Funktion zum Überprüfen einer Datei
        def check_file(file):
            try:
                # Öffnen der Datei
                doc = app.documents.open(file, True)

                # Zugriff auf das aktive Dokument und das Design
                design = app.activeProduct

                # Überprüfen, ob ein Design geöffnet ist
                if not design:
                    return [file.name, "Die Datei enthält kein gültiges Design"], []

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
                        center_of_mass_tuple = (center_of_mass.x, center_of_mass.y, center_of_mass.z)

                        # Materialeigenschaften auslesen
                        material = body.material
                        material_name = material.name if material else "Kein Material zugewiesen"

                        # Massen- und Trägheitseigenschaften auslesen
                        mass = body.physicalProperties.mass
                        inertia_tensor = body.physicalProperties.getXYZMomentsOfInertia()
                        inertia_tuple = (inertia_tensor[0], inertia_tensor[1], inertia_tensor[2])

                        # Anzahl der Flächen, Kanten und Scheitelpunkte
                        num_faces = body.faces.count
                        num_edges = body.edges.count
                        num_vertices = body.vertices.count

                        # Flächeninformationen
                        face_areas = [face.area for face in body.faces]

                        # Kanteninformationen
                        edge_lengths = [edge.length for edge in body.edges]

                        # Scheitelpunktinformationen
                        vertex_coords = [(vertex.geometry.x, vertex.geometry.y, vertex.geometry.z) for vertex in body.vertices]

                        # Überprüfung der Eigenschaften gegen die Vorgabewerte
                        def compare_lists(list1, list2, tolerance=1e-6):
                            if len(list1) != len(list2):
                                return False
                            for a, b in zip(list1, list2):
                                if isinstance(a, tuple) and isinstance(b, tuple):
                                    if not compare_tuples(a, b, tolerance):
                                        return False
                                elif abs(a - b) > tolerance:
                                    return False
                            return True

                        def compare_tuples(tuple1, tuple2, tolerance=1e-6):
                            return all(abs(a - b) <= tolerance for a, b in zip(tuple1, tuple2))

                        checks = [
                            ('Volumen', abs(volume - reference_body['volume']) <= 1e-6),
                            ('Oberfläche', abs(surface_area - reference_body['surface_area']) <= 1e-6),
                            ('Schwerpunkt', compare_tuples(center_of_mass_tuple, reference_body['center_of_mass'])),
                            ('Material', material_name == reference_body['material']),
                            ('Masse', abs(mass - reference_body['mass']) <= 1e-6),
                            ('Trägheitsmomente', compare_tuples(inertia_tuple, reference_body['inertia'])),
                            ('Anzahl der Flächen', num_faces == reference_body['num_faces']),
                            ('Anzahl der Kanten', num_edges == reference_body['num_edges']),
                            ('Anzahl der Scheitelpunkte', num_vertices == reference_body['num_vertices']),
                            ('Flächenflächen', compare_lists(face_areas, reference_body['face_areas'])),
                            ('Kantenlängen', compare_lists(edge_lengths, reference_body['edge_lengths'])),
                            ('Scheitelpunktkoordinaten', compare_lists(vertex_coords, reference_body['vertex_coordinates']))
                        ]

                        # Ergebnisanzeige
                        results = [file.name]
                        discrepancies = []
                        for check in checks:
                            if check[1]:
                                results.append('Y')
                            else:
                                results.append('N')
                                discrepancies.append(check[0])
                        return results, discrepancies

            except:
                return [file.name, "Fehler beim Überprüfen der Datei", traceback.format_exc()], []
            finally:
                # Schließen des Dokuments
                if doc:
                    doc.close(False)

        # Protokollierung der Ergebnisse
        all_results = []
        headers = [
            'Dateiname', 'Volumen', 'Oberfläche', 'Schwerpunkt',
            'Material', 'Masse', 'Trägheitsmomente', 'Anzahl der Flächen',
            'Anzahl der Kanten', 'Anzahl der Scheitelpunkte', 'Flächenflächen',
            'Kantenlängen', 'Scheitelpunktkoordinaten'
        ]
        all_results.append(headers)
        discrepancies_list = []

        for file in files_to_check:
            result, discrepancies = check_file(file)
            all_results.append(result)
            if discrepancies:
                discrepancies_list.append((file.name, discrepancies))

        # Ergebnisse in einer CSV-Datei speichern
        output_file = os.path.join(os.path.expanduser('~'), 'Fusion360_Check_Results.csv')
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(all_results)

            # Fehlerhafte Dateien am Ende der CSV-Datei hinzufügen
            if discrepancies_list:
                csv_writer.writerow([])
                csv_writer.writerow(['In folgenden Dateien sind Fehler:'])
                for file_name, discrepancies in discrepancies_list:
                    csv_writer.writerow([file_name, ', '.join(discrepancies)])

        # Ausgabe der Ergebnisse
        ui.messageBox("Überprüfung abgeschlossen. Ergebnisse sind in der Datei gespeichert:\n" + output_file)

    except:
        if ui:
            ui.messageBox('Fehler: {}'.format(traceback.format_exc()))

# Das Skript ausführen
#run(None)