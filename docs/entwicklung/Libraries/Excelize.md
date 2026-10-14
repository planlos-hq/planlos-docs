# Excelize

Excelize ist eine Go Library zum Lesen und Schreiben von Excel Spreadsheet XML Dateien (.XLSX).
In diesem Projekt wird sie eingesetzt, um Ressourcen aus XLSX Dateien für den Import auszulesen,
sowie einen XLSX Export dieser Ressourcen als Alternative zum CSV Export zu ermöglichen.
Die entsprechenden Endpunkte (`/import/xlsx`, `/export/xlsx`) sind unter planlos-server/apiserver/import_export_csv.go zu finden.

[Excelize GitHub](https://github.com/qax-os/excelize)

# Warum Excelize?

- Pure Go-Biblbiothek
- Am weitesten verbreitete Library für XLSX Dateien (nach Imports auf pkg.go.dev)
- Aktivere Weiterentwicklung als Alternative ("XLSX")
- Direktes Arbeiten mit XLSX Dateien nicht trivial

# Verwendung (Limitiert auf relevante Funktionalitäten)

Excelize unterstützt zahlreiche Excel Funktionalitäten, wie Formeln, Formatierungen, Diagramme, etc.,
jedoch nutzen wir aktuell nur einfache Lese- und Schreiboperationen, um eine Umwandlung von XLSX zu CSV und anders herum zu ermöglichen.
Somit konnte die bestehende CSV Logik weitestgehend wiederverwendet werden.
Die verwendeten Operationen werden nachfolgend anhand von aufeinander aufbauenden Beispielen erklärt:

## XLSX mit io.Reader einlesen
```go
// ...
// Enthält die XLSX Datei als Byte-Array
var buf bytes.Buffer // Implementiert io.Reader
// ...
ex, err := excelize.OpenReader(&buf)
defer ex.Close()
if err != nil { /*...*/ }
```

## Sheet Namen auslesen
```go
sheets := ex.GetSheetList() // liefert []string
firstSheet := sheets[0]
```

## XLSX zeilenweise auslesen
```go
rows, err := ex.Rows(firstSheet)
if err != nil { /*...*/ }
defer rows.Close()

for rows.Next() {
    row, err := rows.Columns() // Werte der Zellen dieser Zeile (als []string)
    if err != nil { /*...*/ }
    // ...
}
```

## XLSX zeilenweise schreiben
```go
ex.SetSheetRow("Sheet1", "A1", &[]string{"Name", "Alter"})
ex.SetSheetRow("Sheet1", "A1", &[]int32{123, 456, 789})
```

## Koordinaten (z.B. 1,1) in Excel Koordinaten (z.B. A1) umwandeln
```go
cell, _ := excelize.CoordinatesToCellName(1, 1) // "A1"
```

## Neue XLSX erstellen
```go
ex2 := excelize.NewFile()
defer ex2.Close()

```

## Abspeichern / Schreiben
```go
// Schreiben mit io.Writer
var buf2 bytes.Buffer
ex2.Write(&buf2)
// Schreiben in Datei
ex2.SaveAs("output.xlsx")
// Quelldatei überschreiben
ex.Save()
```

## Zelle schreiben / lesen
```go
// Schreiben
ex2.SetCellValue("Sheet1", cell /*"A1"*/, "Los Planos") // Gibt Referenz zur Datei zurück für Chaining
// Lesen
cell, err := f.GetCellValue("Sheet1", "B2") // Rückgabe als string
if err != nil { /*...*/ }
```

# Bemerkungen

Während der XLSX Import / Export Tests gab es teilweise Probleme mit älteren Dateiversionen, jedoch ist nicht abschließend geklärt, ob Excelize das Problem verursacht hat.
Bei modernen Dateiversionen funktioniert Excelize problemlos und sollte alle Dateiversionen ab Excel 2007 unterstützen.
