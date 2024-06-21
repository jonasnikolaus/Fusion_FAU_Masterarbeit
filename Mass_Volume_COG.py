import adsk.core, adsk.fusion, traceback
import csv
import os


# Vorgabewerte der Musterlösung
reference_body = {
    'name': 'Body1',
    'volume': 15.667333,
    'surface_area': 107.794992,
    'center_of_mass': (0.000000, -0.000000, 0.872634),
    'material': 'Steel',
    'mass': 0.122989,
    'inertia': (1.000000, 0.258368, 0.249897),
    'num_faces': 53,
    'num_edges': 147,
    'num_vertices': 99,
    'face_areas': [
        0.827724, 0.481703, 0.555941, 0.608162, 0.643765, 0.665429,
        13.052522, 0.643765, 0.608162, 0.555941, 0.481703, 0.827724,
        1.348999, 0.665429, 11.380419, 3.769911, 4.523893, 2.900945,
        2.918596, 0.537228, 1.768371, 1.978558, 0.346462, 2.189418,
        2.333266, 0.417757, 2.481045, 2.582479, 0.467555, 2.685749,
        2.754977, 0.502311, 2.822507, 2.864652, 0.525025, 2.900945,
        2.918596, 0.537228, 2.822507, 2.864652, 0.525025, 2.685749,
        2.754977, 0.502311, 2.481045, 2.582479, 0.467555, 2.189418,
        2.333266, 0.417757, 1.768371, 1.978558, 0.346462
    ],
    'edge_lengths': [
        2.700000, 2.895755, 0.210340, 3.059412, 0.210340, 3.354102,
        0.182171, 3.600000, 0.182171, 3.806573, 0.166503, 3.979950,
        0.166503, 4.124318, 0.157284, 4.242641, 0.157284, 4.337050,
        0.152159, 4.409082, 0.152159, 4.459821, 0.187188, 0.650473,
        0.650473, 0.187188, 0.650379, 0.650309, 0.155156, 0.650273,
        0.650240, 0.138608, 0.650222, 0.650207, 0.129009, 0.650196,
        0.650184, 0.123425, 0.650179, 0.650174, 0.120619, 0.650173,
        0.300223, 0.650173, 0.120619, 0.650174, 0.152159, 0.650179,
        0.123425, 0.650184, 0.157284, 0.650196, 0.129009, 0.650207,
        0.166503, 0.650222, 0.138608, 0.650240, 0.182171, 0.650273,
        0.155156, 0.650309, 0.210340, 0.650379, 0.187188, 0.650473,
        2.895755, 0.650473, 0.187188, 0.650379, 0.210340, 0.650309,
        0.155156, 0.650273, 0.182171, 0.650240, 0.138608, 0.650222,
        0.166503, 0.650207, 0.129009, 0.650196, 0.157284, 0.650184,
        0.123425, 0.650179, 0.152159, 0.650174, 0.120619, 0.650173,
        0.300223, 0.650173, 0.120619, 0.650174, 0.650179, 0.123425,
        0.650184, 0.650196, 0.129009, 0.650207, 0.650222, 0.138608,
        0.650240, 0.650273, 0.155156, 0.650309, 0.650379, 14.137167,
        4.337050, 4.242641, 4.124318, 3.979950, 3.806573, 3.600000,
        3.354102, 3.059412, 2.700000, 4.489989, 4.489989, 4.409082,
        4.459821, 7.539822, 7.539822, 4.463754, 4.487884, 2.739544,
        3.026731, 3.380695, 3.577303, 3.825324, 3.963975, 4.137282,
        4.231914, 4.345239, 4.402851, 4.463754, 4.487884, 4.345239,
        4.402851, 4.137282, 4.231914, 3.825324, 3.963975, 3.380695,
        3.577303, 2.739544, 3.026731
    ],
    'vertex_coordinates': [
        (1.350000, 1.800000, 1.600000), (-1.350000, 1.800000, 1.600000),
        (1.677051, 1.500000, 1.600000), (1.529706, 1.650000, 1.600000),
        (-1.529706, 1.650000, 1.600000), (-1.677051, 1.500000, 1.600000),
        (1.903287, 1.200000, 1.600000), (1.800000, 1.350000, 1.600000),
        (-1.800000, 1.350000, 1.600000), (-1.903287, 1.200000, 1.600000),
        (2.062159, 0.900000, 1.600000), (1.989975, 1.050000, 1.600000),
        (-1.989975, 1.050000, 1.600000), (-2.062159, 0.900000, 1.600000),
        (2.168525, 0.600000, 1.600000), (2.121320, 0.750000, 1.600000),
        (-2.121320, 0.750000, 1.600000), (-2.168525, 0.600000, 1.600000),
        (2.229910, 0.300000, 1.600000), (2.204541, 0.450000, 1.600000),
        (-2.204541, 0.450000, 1.600000), (-2.229910, 0.300000, 1.600000),
        (-1.513365, 1.665000, 0.950000), (-1.369772, 1.785000, 0.950000),
        (1.369772, 1.785000, 0.950000), (1.513365, 1.665000, 0.950000),
        (1.690348, 1.485000, 0.950000), (1.788652, 1.365000, 0.950000),
        (1.912662, 1.185000, 0.950000), (1.981988, 1.065000, 0.950000),
        (2.068641, 0.885000, 0.950000), (2.115957, 0.765000, 0.950000),
        (2.172619, 0.585000, 0.950000), (2.201426, 0.465000, 0.950000),
        (2.231877, 0.285000, 0.950000), (2.243942, 0.165000, 0.950000),
        (2.244994, 0.150000, 1.600000), (2.244994, -0.150000, 1.600000),
        (2.243942, -0.165000, 0.950000), (2.231877, -0.285000, 0.950000),
        (2.229910, -0.300000, 1.600000), (2.204541, -0.450000, 1.600000),
        (2.201426, -0.465000, 0.950000), (2.172619, -0.585000, 0.950000),
        (2.168525, -0.600000, 1.600000), (2.121320, -0.750000, 1.600000),
        (2.115957, -0.765000, 0.950000), (2.068641, -0.885000, 0.950000),
        (2.062159, -0.900000, 1.600000), (1.989975, -1.050000, 1.600000),
        (1.981988, -1.065000, 0.950000), (1.912662, -1.185000, 0.950000),
        (1.903287, -1.200000, 1.600000), (1.800000, -1.350000, 1.600000),
        (1.788652, -1.365000, 0.950000), (1.690348, -1.485000, 0.950000),
        (1.677051, -1.500000, 1.600000), (1.529706, -1.650000, 1.600000),
        (1.513365, -1.665000, 0.950000), (1.369772, -1.785000, 0.950000),
        (1.350000, -1.800000, 1.600000), (-1.350000, -1.800000, 1.600000),
        (-1.369772, -1.785000, 0.950000), (-1.513365, -1.665000, 0.950000),
        (-1.529706, -1.650000, 1.600000), (-1.677051, -1.500000, 1.600000),
        (-1.690348, -1.485000, 0.950000), (-1.788652, -1.365000, 0.950000),
        (-1.800000, -1.350000, 1.600000), (-1.903287, -1.200000, 1.600000),
        (-1.912662, -1.185000, 0.950000), (-1.981988, -1.065000, 0.950000),
        (-1.989975, -1.050000, 1.600000), (-2.062159, -0.900000, 1.600000),
        (-2.068641, -0.885000, 0.950000), (-2.115957, -0.765000, 0.950000),
        (-2.121320, -0.750000, 1.600000), (-2.168525, -0.600000, 1.600000),
        (-2.172619, -0.585000, 0.950000), (-2.201426, -0.465000, 0.950000),
        (-2.204541, -0.450000, 1.600000), (-2.229910, -0.300000, 1.600000),
        (-2.231877, -0.285000, 0.950000), (-2.243942, -0.165000, 0.950000),
        (-2.244994, -0.150000, 1.600000), (-2.244994, 0.150000, 1.600000),
        (-2.243942, 0.165000, 0.950000), (-2.231877, 0.285000, 0.950000),
        (-2.201426, 0.465000, 0.950000), (-2.172619, 0.585000, 0.950000),
        (-2.115957, 0.765000, 0.950000), (-2.068641, 0.885000, 0.950000),
        (-1.981988, 1.065000, 0.950000), (-1.912662, 1.185000, 0.950000),
        (-1.788652, 1.365000, 0.950000), (-1.690348, 1.485000, 0.950000),
        (0.000000, 2.250000, 0.500000), (0.000000, 1.200000, 0.500000),
        (0.000000, 1.200000, 0.000000)
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
                    return f"Die Datei enthält kein gültiges Design: {file.name}"

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
                            ('Körpername', body.name == reference_body['name']),
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
                        discrepancies = [check[0] for check in checks if not check[1]]

                        if discrepancies:
                            return f"Datei: {file.name}\nDie folgenden Eigenschaften stimmen nicht überein:\n" + "\n".join(discrepancies)
                        else:
                            return f"Datei: {file.name}\nAlle Eigenschaften stimmen mit der Musterlösung überein."

            except:
                return f"Fehler beim Überprüfen der Datei: {file.name}\nFehler: {traceback.format_exc()}"
            finally:
                # Schließen des Dokuments
                if doc:
                    doc.close(False)

        # Protokollierung der Ergebnisse
        results = []
        for file in files_to_check:
            result = check_file(file)
            results.append(result)

        # Ergebnisse in einer CSV-Datei speichern
        output_file = os.path.join(os.path.expanduser('~'), 'Fusion360_Check_Results.csv')
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Dateiname', 'Ergebnis'])
            for result in results:
                csv_writer.writerow([result.split('\n')[0], result])

        # Ausgabe der Ergebnisse
        ui.messageBox("Überprüfung abgeschlossen. Ergebnisse sind in der Datei gespeichert:\n" + output_file)

    except:
        if ui:
            ui.messageBox('Fehler: {}'.format(traceback.format_exc()))

# Das Skript ausführen
#run(None)
