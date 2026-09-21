"""Weather-station observation reader and analyzer."""

import csv
import sys
import unittest
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"


def read_observations(filename):
    """Read *filename* and return ``(observations, errors)``.

    Each observation is kept as ``(date_string, temperature)``.  Date strings
    are parsed with :class:`datetime` for validation and chronological sorting.
    """
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.reader(input_file)
        for line_number, row in enumerate(reader, start=1):
            if len(row) != 3:
                errors.append((line_number, "malformed line"))
                continue

            station, date, temperature_text = (field.strip() for field in row)
            if not station or not date or not temperature_text:
                errors.append((line_number, "malformed line"))
                continue

            try:
                parsed_date = datetime.strptime(date, DATE_FORMAT)
            except ValueError:
                errors.append((line_number, "invalid date"))
                continue

            try:
                temperature = float(temperature_text)
            except ValueError:
                errors.append((line_number, "invalid temperature"))
                continue

            if not -100.0 <= temperature <= 150.0:
                errors.append((line_number, "temperature out of range"))
                continue

            key = (station, date)
            if key in seen:
                errors.append((line_number, "duplicate station/date observation"))
                continue

            seen.add(key)
            observations.setdefault(station, []).append((date, temperature, parsed_date))

    for station in observations:
        observations[station].sort(key=lambda observation: observation[2])
        observations[station] = [
            (date, temperature) for date, temperature, _ in observations[station]
        ]
    return observations, errors


def station_statistics(observations):
    """Return ``station -> (minimum, maximum, mean)`` temperature data."""
    return {
        station: (
            min(temperature for _, temperature in readings),
            max(temperature for _, temperature in readings),
            sum(temperature for _, temperature in readings) / len(readings),
        )
        for station, readings in observations.items()
        if readings
    }


def station_outliers(observations):
    """Return stations whose latest temperature exceeds their mean temperature."""
    statistics = station_statistics(observations)
    return {
        station: (readings[-1][0], readings[-1][1], statistics[station][2])
        for station, readings in observations.items()
        if readings and readings[-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    """Write statistics in lexicographic station order."""
    with open(filename, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            writer.writerow((station, f"{minimum:.1f}", f"{maximum:.1f}", f"{mean:.1f}"))


def main():
    """Read input/output filenames from the command line and report results."""
    if len(sys.argv) != 3:
        print(f"Usage: {Path(sys.argv[0]).name} observations_file statistics_file")
        return

    try:
        observations, errors = read_observations(sys.argv[1])
        statistics = station_statistics(observations)
        outliers = station_outliers(observations)
        write_statistics(sys.argv[2], statistics)
    except OSError as error:
        print(f"File access error: {error}")
        return

    print("Statistics:")
    for station in sorted(statistics):
        minimum, maximum, mean = statistics[station]
        print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")
    print("Outliers:")
    for station in sorted(outliers):
        date, temperature, mean = outliers[station]
        print(f"{station}: ({date}, {temperature:.1f}, {mean:.1f})")
    if errors:
        print("Input errors:")
        for line_number, message in errors:
            print(f"line {line_number}: {message}")


class WeatherStationTests(unittest.TestCase):
    """Tests for normal data, validation, calculations, sorting, and files."""

    def make_file(self, contents):
        file_path = Path(self.temp_directory.name) / "observations.csv"
        file_path.write_text(contents, encoding="utf-8")
        return file_path

    def setUp(self):
        self.temp_directory = TemporaryDirectory()

    def tearDown(self):
        self.temp_directory.cleanup()

    def test_multiple_stations_and_negative_temperatures(self):
        data = "North,01:00:00 AM 01/02/2026,-5.5\nSouth,01:00:00 AM 01/02/2026,80\n"
        observations, errors = read_observations(self.make_file(data))
        self.assertEqual(errors, [])
        self.assertEqual(observations["North"], [("01:00:00 AM 01/02/2026", -5.5)])
        self.assertEqual(observations["South"][0][1], 80.0)

    def test_observations_are_sorted_by_date(self):
        data = "A,01:00:00 AM 01/03/2026,2\nA,01:00:00 AM 01/01/2026,1\n"
        observations, _ = read_observations(self.make_file(data))
        self.assertEqual([temperature for _, temperature in observations["A"]], [1.0, 2.0])

    def test_duplicate_observation_is_rejected(self):
        data = "A,01:00:00 AM 01/01/2026,1\nA,01:00:00 AM 01/01/2026,2\n"
        observations, errors = read_observations(self.make_file(data))
        self.assertEqual(len(observations["A"]), 1)
        self.assertEqual(errors, [(2, "duplicate station/date observation")])

    def test_invalid_ranges_are_rejected(self):
        data = "A,01:00:00 AM 01/01/2026,-100.1\nB,01:00:00 AM 01/01/2026,150.1\n"
        observations, errors = read_observations(self.make_file(data))
        self.assertEqual(observations, {})
        self.assertEqual([message for _, message in errors], ["temperature out of range"] * 2)

    def test_calculated_statistics_and_outliers(self):
        observations = {"A": [("old", -10.0), ("new", 20.0)], "B": [("only", 5.0)]}
        self.assertEqual(station_statistics(observations), {"A": (-10.0, 20.0, 5.0), "B": (5.0, 5.0, 5.0)})
        self.assertEqual(station_outliers(observations), {"A": ("new", 20.0, 5.0)})

    def test_statistics_file_is_sorted_and_formatted(self):
        output = Path(self.temp_directory.name) / "statistics.csv"
        write_statistics(output, {"Zulu": (1, 3, 2), "Alpha": (-2.25, 4, 0.875)})
        self.assertEqual(output.read_text(encoding="utf-8"), "Alpha,-2.2,4.0,0.9\nZulu,1.0,3.0,2.0\n")

    def test_missing_file_raises_file_error(self):
        with self.assertRaises(FileNotFoundError):
            read_observations(Path(self.temp_directory.name) / "missing.csv")


if __name__ == "__main__":
    main()
