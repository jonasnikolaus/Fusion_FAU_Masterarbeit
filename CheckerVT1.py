import adsk.core, adsk.fusion, traceback
import csv
import os

# Vorgabewerte der Musterlösung
reference_body = {
    'name': 'Body1',
    'volume': 649.036998,
    'surface_area': 686.027620,
    'center_of_mass': (-0.000000, 25.126535, -0.009154),
    'material': 'Steel',
    'mass': 5.094940,
    'inertia': (1.000000, 3867.547960, 13.321123),
    'num_faces': 48,
    'num_edges': 101,
    'num_vertices': 73,
    'face_areas': [
        92.430572, 7.622553, 11.945906, 6.126106, 0.620465, 21.362830, 
        3.337942, 85.925820, 7.853982, 20.734512, 4.123340, 267.035376, 
        7.068583, 22.619467, 0.620465, 25.729644, 2.324779, 10.995574, 
        0.541925, 1.358855, 1.087060, 1.358855, 1.087060, 5.879380, 
        2.702484, 7.058351, 2.702484, 0.242775, 2.702484, 7.058351, 
        2.702484, 0.242775, 2.702484, 7.058351, 2.702484, 0.242775, 
        2.702484, 7.058351, 2.702484, 0.242775, 2.702484, 7.058351, 
        2.702484, 0.242775, 2.702484, 7.058351, 2.702484, 0.242775
    ],
    'edge_lengths': [
        10.681415, 0.807572, 8.700000, 0.972664, 8.700000, 0.807572, 
        8.700000, 0.972664, 8.700000, 0.807572, 8.700000, 0.972664, 
        8.700000, 0.807572, 8.700000, 0.972664, 8.700000, 0.807572, 
        8.700000, 0.972664, 8.700000, 0.807572, 8.700000, 0.972664, 
        8.700000, 0.310630, 0.310630, 0.811305, 0.310630, 0.310630, 
        0.811305, 0.310630, 0.310630, 0.811305, 0.310630, 0.310630, 
        0.811305, 0.310630, 0.310630, 0.811305, 0.310630, 0.310630, 
        0.811305, 12.252211, 12.252211, 12.566371, 12.566371, 14.137167, 
        2.212704, 3.100000, 2.212704, 3.100000, 14.137167, 17.278760, 
        17.278760, 15.707963, 15.707963, 12.566371, 12.566371, 12.252211, 
        12.252211, 10.995574, 10.995574, 0.438340, 3.100000, 0.438340, 
        0.438340, 2.199115, 0.438340, 3.100000, 2.199115, 8.700000, 
        0.310630, 8.700000, 0.811305, 0.310630, 8.700000, 0.310630, 
        8.700000, 0.811305, 0.310630, 8.700000, 0.310630, 8.700000, 
        0.811305, 0.310630, 8.700000, 0.310630, 8.700000, 0.811305, 
        0.310630, 8.700000, 0.310630, 8.700000, 0.811305, 0.310630, 
        8.700000, 0.310630, 8.700000, 0.811305, 0.310630
    ],
    'vertex_coordinates': [
        (0.000000, 12.600000, 1.700000), (-1.630909, 8.700000, 0.479725),
        (-1.230909, 8.700000, 1.172546), (-1.230909, 0.000000, 1.172546),
        (-0.400000, 0.000000, 1.652271), (-0.400000, 8.700000, 1.652271),
        (0.400000, 8.700000, 1.652271), (0.400000, 0.000000, 1.652271),
        (1.230909, 0.000000, 1.172546), (1.230909, 8.700000, 1.172546),
        (1.630909, 8.700000, 0.479725), (1.630909, 0.000000, 0.479725),
        (1.630909, 0.000000, -0.479725), (1.630909, 8.700000, -0.479725),
        (1.230909, 8.700000, -1.172546), (1.230909, 0.000000, -1.172546),
        (0.400000, 0.000000, -1.652271), (0.400000, 8.700000, -1.652271),
        (-0.400000, 8.700000, -1.652271), (-0.400000, 0.000000, -1.652271),
        (-1.230909, 0.000000, -1.172546), (-1.230909, 8.700000, -1.172546),
        (-1.630909, 8.700000, -0.479725), (-1.630909, 0.000000, -0.479725),
        (-1.630909, 0.000000, 0.479725), (-1.361895, 0.000000, 0.324410),
        (-1.361895, 0.000000, -0.324410), (-0.961895, 0.000000, -1.017231),
        (-0.400000, 0.000000, -1.341641), (0.400000, 0.000000, -1.341641),
        (0.961895, 0.000000, -1.017231), (1.361895, 0.000000, -0.324410),
        (1.361895, 0.000000, 0.324410), (0.961895, 0.000000, 1.017231),
        (0.400000, 0.000000, 1.341641), (-0.400000, 0.000000, 1.341641),
        (-0.961895, 0.000000, 1.017231), (0.000000, 44.400000, 1.950000),
        (0.000000, 43.900000, 1.950000), (0.000000, 43.900000, 2.000000),
        (0.000000, 42.200000, 2.000000), (0.000000, 42.200000, 2.250000),
        (-0.700000, 39.750000, 2.138340), (0.700000, 39.750000, 2.138340),
        (0.700000, 36.650000, 2.138340), (-0.700000, 36.650000, 2.138340),
        (0.000000, 35.700000, 2.250000), (0.000000, 35.700000, 2.750000),
        (0.000000, 34.500000, 2.750000), (0.000000, 34.500000, 2.500000),
        (0.000000, 17.500000, 2.500000), (0.000000, 17.500000, 2.000000),
        (0.000000, 15.700000, 2.000000), (0.000000, 15.700000, 1.950000),
        (0.000000, 13.600000, 1.950000), (0.000000, 13.600000, 1.750000),
        (0.000000, 12.600000, 1.750000), (-0.700000, 36.650000, 1.700000),
        (-0.700000, 39.750000, 1.700000), (0.700000, 36.650000, 1.700000),
        (0.700000, 39.750000, 1.700000), (-0.400000, 8.700000, 1.341641),
        (0.400000, 8.700000, 1.341641), (0.961895, 8.700000, 1.017231),
        (1.361895, 8.700000, 0.324410), (1.361895, 8.700000, -0.324410),
        (0.961895, 8.700000, -1.017231), (0.400000, 8.700000, -1.341641),
        (-0.400000, 8.700000, -1.341641), (-0.961895, 8.700000, -1.017231),
        (-1.361895, 8.700000, -0.324410), (-1.361895, 8.700000, 0.324410),
        (-0.961895, 8.700000, 1.017231)
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