import subprocess

def get_device_characteristics():
    # Führe den Befehl "wmic path Win32_PNPEntity get DeviceID, Name" aus und speichere das Ergebnis in der Variablen "output"
    output = subprocess.run(["wmic", "path", "Win32_PNPEntity", "get", "DeviceID, Name"], stdout=subprocess.PIPE).stdout.decode()

    # Trenne den Befehlsausgabe an jedem Zeilenumbruch auf und speichere das Ergebnis in der Liste "lines"
    lines = output.split("\n")

    # Iteriere über jede Zeile in der Liste
    for line in lines:
        # Wenn die Zeile leer ist oder mit "Name" beginnt, überspringe sie
        if line == "" or line.startswith("Name"):
            continue

        # Splitte die Zeile an den Doppelpunkten auf und speichere die Teile in der Liste "parts"
        parts = line.split(":")

        # Wenn es weniger als zwei Teile gibt, ist die Zeile ungültig und kann übersprungen werden
        if len(parts) < 2:
            continue

        # Der erste Teil ist der Gerätetyp (z.B. "ACPI", "CPU", "SCSI")
        device_type = parts[0]

        # Der zweite Teil ist das Gerätename (z.B. "Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz")
        device_name = parts[1]

        # Gebe das Gerätetyp und den Gerätenamen aus
        print(f"Gerätetyp: {device_type}")
        print(f"Gerätename: {device_name}")

# Rufe die Funktion auf
get_device_characteristics()
