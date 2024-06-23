
# Fusion 360 Prüf-Skript

Dieses Skript dient zur Überprüfung der physischen Eigenschaften von 3D-Modellen in Autodesk Fusion 360. Es vergleicht die Eigenschaften der hochgeladenen Modelle mit vorgegebenen Referenzwerten und generiert eine CSV-Datei mit den Ergebnissen der Überprüfung.
Das Skript funktioniert aktuell für:
- Grundlagenübung 1
- Grundlagenübung 2
- Vertiefungsübung 1
- Vertiefungsübung 2

## Voraussetzungen

- Autodesk Fusion 360
- Python-Skriptunterstützung in Fusion 360

## Schritt-für-Schritt-Anleitung

### 1. Erstellen eines neuen Projekts

1. Öffnen Sie Autodesk Fusion 360.
2. Gehen Sie zu Ihrem **Datenpanel** (links oben).
3. Klicken Sie auf **Neues Projekt**.
4. Benennen Sie das Projekt **NXtest**.

### 2. Hochladen der .PRT-Dateien

1. Öffnen Sie das Projekt **NXtest**.
2. Klicken Sie auf das **Upload**-Symbol.
3. Klicken Sie auf **Select Files** und wählen Sie alle .PRT-Dateien im gewünschten Ordner aus.
4. Setzen Sie einen Haken bei **.PRT Files are not Assembly Files**.
5. Stellen Sie sicher, dass die **Location** auf **NXtest** gesetzt ist.
6. Klicken Sie auf **Upload** und warten Sie, bis der Upload abgeschlossen ist.

### 3. Ausführen des Skripts

1. Gehen Sie zu **UTILITIES** > **Add-Ins** > **Scripts and Add-Ins**.
2. Wählen Sie den Tab **Scripts**.
3. Klicken Sie auf **Add**.
4. Navigieren Sie zu dem Verzeichnis, in dem das Skript gespeichert ist, und wählen Sie es aus.
5. Das Skript erscheint nun in der Liste. Wählen Sie es aus und klicken Sie auf **Run**.

### Skript-Erklärung

Das Skript führt folgende Schritte aus:

1. **Initialisierung**: Es greift auf die aktuelle Anwendung und Benutzeroberfläche von Fusion 360 zu.
2. **Projektzugriff**: Es überprüft, ob das Projekt **NXtest** existiert und greift auf den Root-Ordner zu.
3. **Dateiprüfung**: Es durchsucht den Root-Ordner nach Dateien mit der Endung `.f3d`.
4. **Eigenschaftsüberprüfung**: Für jede Datei wird ein Dokument geöffnet und die physischen Eigenschaften des 3D-Modells ausgelesen:
   - Volumen
   - Oberfläche
   - Schwerpunkt
   - Material
   - Masse
   - Trägheitsmomente
   - Anzahl der Flächen, Kanten und Scheitelpunkte
   - Flächeninformationen
   - Kanteninformationen
   - Scheitelpunktkoordinaten
5. **Vergleich mit Referenzwerten**: Die ausgelesenen Eigenschaften werden mit den vorgegebenen Referenzwerten verglichen.
6. **Ergebnisprotokollierung**: Die Ergebnisse der Überprüfung werden in einer CSV-Datei gespeichert und im Home-Verzeichnis des Benutzers abgelegt.

### Beispielhafte Referenzwerte

```python
reference_body = {
    'name': 'Body1',
    'volume': 1064.070364,
    'surface_area': 3622.932909,
    'center_of_mass': (-0.000110, -0.000100, -9.325000),
    'material': 'Steel',
    'mass': 8.352952,
    'inertia': (1.000000, 1540.329128, 1711.729224),
    'num_faces': 12,
    'num_edges': 20,
    'num_vertices': 18,
    'face_areas': [51.525886, 1714.791883, 125.240700, 1586.386659, 121.237341, 6.785840, 1.696460, 3.392920, 1.696460, 3.392920, 3.392920, 3.392920],
    'edge_lengths': [86.571964, 82.749960, 22.392609, 44.488456, 5.654867, 5.654867, 5.654867, 2.827433, 5.654867, 2.827433, 11.309734, 43.940698, 21.527194, 5.654867, 5.654867, 5.654867, 2.827433, 5.654867, 2.827433, 11.309734],
    'vertex_coordinates': [(15.000000, -0.000000, -20.000000), (-14.393377, -0.000000, -20.000000), (8.500000, 0.000000, 0.000000), (-1.925000, -4.893044, 0.000000), (3.275000, -4.113621, 0.000000), (1.925000, 4.893044, 0.000000), (5.200000, -0.000000, 0.000000), (-3.275000, 4.113621, 0.000000), (-5.200000, 0.000000, 0.000000), (-1.800000, 0.000000, 0.000000), (-8.422000, -0.000000, -0.600000), (-3.275000, -4.113621, -0.600000), (1.475000, -4.113621, -0.600000), (1.475000, 4.113621, -0.600000), (4.300000, -0.000000, -0.600000), (-3.275000, 4.113621, -0.600000), (-5.200000, 0.000000, -0.600000), (-1.800000, 0.000000, -0.600000)]
}
```

## Ausgabe

Nach Abschluss der Überprüfung erstellt das Skript eine CSV-Datei namens `Fusion360_Check_Results.csv` im Home-Verzeichnis des Benutzers. Diese Datei enthält die Ergebnisse der Überprüfung und eine Liste der Dateien, die Fehler aufweisen.

## Fehlerbehebung

Falls während der Ausführung des Skripts Fehler auftreten, werden diese in einer Meldung ausgegeben. Überprüfen Sie die Datei und stellen Sie sicher, dass alle Schritte korrekt durchgeführt wurden.
